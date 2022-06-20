"""
Todo:
    - Make Unit-Test.
    - Refactoring is needed!
"""
import datetime
import json
import os
import zipfile
from logging import getLogger
from pathlib import Path
from typing import Dict, Tuple

import numpy as np
import pandas as pd

from ...activity import ActSet
from ...configs import users as OPENPACK_USERS
from ...configs.datasets.annotations import OPENPACK_OPERATIONS
from .eval import eval_operation_segmentation

logger = getLogger(__name__)

# -----------------------------------------------------------------------------


def resample_prediction_1Hz(
    ts_unix: np.ndarray = None,
    arr: np.ndarray = None,
) -> Tuple[np.ndarray, np.ndarray]:
    """Change the sampling rate into 1 Hz.

    Args:
        ts_unix (np.ndarray): 1d array of unixtimestamp. Defaults to None.
        arr (np.ndarray): 1d array of class IDs. Defaults to None.

    Returns:
        Tuple[np.ndarray, np.ndarray]: arrays of unixtime and resampled class ids.
    """
    assert arr.ndim == 1
    assert ts_unix.ndim == 1
    assert len(arr) == len(
        ts_unix), f"ts_unix={ts_unix.shape}, arr={arr.shape}"

    tmp = ts_unix - (ts_unix % 1000)
    ts_unix_1hz = np.append(tmp, tmp[-1] + 1000)  # FIXME: write in one line

    delta = (ts_unix_1hz[1:] - ts_unix_1hz[:-1])
    assert delta.min() >= 0, (
        "values in array are expected to be monotonically increasing, "
        f"but the minium step is {delta.min()}."
    )

    arr_out, ts_unix_out = [], []
    cur_time = ts_unix_1hz[0]
    for r in range(len(ts_unix_1hz)):
        if cur_time != ts_unix_1hz[r]:
            arr_out.append(arr[r - 1])
            ts_unix_out.append(cur_time)
            cur_time = ts_unix_1hz[r]

    return (
        np.array(ts_unix_out),
        np.array(arr_out),
    )


def crop_seq_with_user_config(
        ts_unix: np.ndarray,
        seq: np.ndarray,
        user: str,
        session: str,
):
    """Extract valid segment from given sequence.

    Args:
        ts_unix (np.ndarray): 1d array of unixtimestamp.
        y_id_out (np.ndarray): _description_
        user_session (ster): e.g., "U0102-S0100"
    """
    assert ts_unix.ndim == 1
    assert seq.ndim

    if hasattr(OPENPACK_USERS, user):
        user_cfg = getattr(OPENPACK_USERS, user)
    else:
        logger.warning(
            f"unsupported user ID: {user}, skip cropping this sequence.")
        return ts_unix, seq

    ts_head = datetime.datetime.fromisoformat(user_cfg.sessions[session].start)
    ts_tail = datetime.datetime.fromisoformat(user_cfg.sessions[session].end)

    unixtime_head = int(ts_head.timestamp() * 1000)  # [ms] precision
    # FIXME: The last second is droped when I make release version CSV.
    # See detail in har-open-pack-codes/issues/31
    unixtime_tail = int(ts_tail.timestamp() * 1000) - 1000  # [ms] precision

    ind = np.where((ts_unix >= unixtime_head) & (ts_unix < unixtime_tail))[0]
    return ts_unix[ind], seq[ind]


def construct_submission_dict(
        outputs: Dict[str, Dict[str, np.ndarray]], act_set: ActSet) -> Dict:
    """Make dict that can be used for submission and `eval_workprocess_segmentation()` func.

    Args:
        outputs (Dict[str, Dict[str, np.ndarray]]): key is expected to be a pair of user and
            session. e.g., "U0102-S0100".
        act_set (ActSet): _description_

    Returns:
        Dict: _description_
    """
    submission = dict()
    for key, d in outputs.items():
        record = dict()
        user, session = key.split("-")

        assert d["y"].ndim == 3
        y_id = act_set.convert_index_to_id(np.argmax(d["y"], axis=1).ravel())
        ts_unix_out, y_id_out = resample_prediction_1Hz(
            ts_unix=d["unixtime"].copy().ravel(), arr=y_id)

        ts_unix_out, y_id_out = crop_seq_with_user_config(
            ts_unix_out, y_id_out, user, session)

        record["unixtime"] = ts_unix_out.copy()
        record["prediction"] = y_id_out.copy()

        if "t_idx" in d.keys():
            assert d["t_idx"].ndim == 2
            t_id = act_set.convert_index_to_id(d["t_idx"]).ravel()
            ts_unix_out2, t_id_out = resample_prediction_1Hz(
                ts_unix=d["unixtime"].copy().ravel(), arr=t_id)
            ts_unix_out2, t_id_out = crop_seq_with_user_config(
                ts_unix_out2, t_id_out, user, session)
            np.testing.assert_array_equal(ts_unix_out, ts_unix_out2)

            record["ground_truth"] = t_id_out.copy()

        submission[key] = record

    return submission


def make_submission_zipfile(submission: Dict, logdir: Path) -> None:
    """Check dict contents and generate zip file for codalab submission.

    Args:
        submission (Dict): _description_
        logdir (Path): _description_
    Returns:
        None (make JSON & zip files)
    """
    # Check data format and convert into pure objects
    submission_clean = dict()
    for key, d in submission.items():
        assert isinstance(d, dict)

        record = dict()
        for arr_name, arr in d.items():
            if arr_name not in ("prediction", "unixtime"):
                logger.warning(
                    f"unexpected entry[{arr_name}] is found in submission dict.")
            assert isinstance(arr, np.ndarray)
            record[arr_name] = arr.tolist()
        submission_clean[key] = record

    # Write JSON file
    path_json = Path(logdir, "submission.json")
    if path_json.exists():
        os.remove(path_json)
    with open(path_json, "w") as f:
        json.dump(submission_clean, f)
    logger.info(f"write submission.json to {path_json}")

    # Make zip file
    path_zip = Path(logdir, "submission.zip")
    if path_zip.exists():
        os.remove(path_zip)
    with zipfile.ZipFile(path_zip, "w") as zf:
        zf.write(path_json, arcname="./submission.json")
    logger.info(f"write submission.zip to {path_zip}")


# -----------------------------------------------------------------------------

def eval_operation_segmentation_wrapper(
    outputs: Dict[str, Dict[str, np.ndarray]],
    act_set: ActSet = OPENPACK_OPERATIONS,
    exclude_ignore_class=True,
) -> pd.DataFrame:
    """ Compute evaluation metrics from model outputs (predicted probability).

    Args:
        outputs (Dict[str, Dict[str, np.ndarray]]): dict object that contains t_idx and y.
            t_idx is a 2d array of target class index with shape=(BATCH_SIZE, WINDOW).
            y is a 3d array of predction probabilities with shape=(BATCH_SIZE, NUM_CLASSES, WINDOW).
        classes (Tuple, optional): class definition.
    Returns:
        pd.DataFrame
    """
    submission = construct_submission_dict(outputs, act_set)
    classes = act_set.to_tuple()
    ignore_class_id = act_set.get_ignore_class_id()
    if isinstance(ignore_class_id, tuple):
        raise NotImplementedError()

    # Evaluate
    df_scores = []
    t_id_concat, y_id_concat = [], []
    for key, d in submission.items():
        t_id = d["ground_truth"]
        y_id = d["prediction"]

        t_id_concat.append(t_id.copy())
        y_id_concat.append(y_id.copy())

        df_tmp = eval_operation_segmentation(
            t_id,
            y_id,
            classes=classes,
            ignore_class_id=ignore_class_id,
            mode=None)
        df_tmp["key"] = key
        df_scores.append(df_tmp.reset_index(drop=False))

    # Overall Score
    df_tmp = eval_operation_segmentation(
        np.concatenate(t_id_concat, axis=0),
        np.concatenate(y_id_concat, axis=0),
        classes=classes,
        ignore_class_id=ignore_class_id,
        mode=None,
    )
    df_tmp["key"] = "all"
    df_scores.append(df_tmp.reset_index(drop=False))

    df_scores = pd.concat(df_scores, axis=0, ignore_index=True)
    return df_scores
