"""
Todo:
    - Make Unit-Test.
    - Refactoring is needed!
"""
import json
import os
import zipfile
from logging import getLogger
from pathlib import Path
from typing import Dict, Optional, Tuple

import numpy as np
import pandas as pd
from omegaconf import DictConfig, open_dict

from ...activity import ActSet
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


def ffill_missing_elements(
    unixtime_gt: np.ndarray,
    unixtime_pred: np.ndarray,
    prediction: np.ndarray,
):
    missing_timestep = sorted(
        list(set(unixtime_gt.tolist()) - set(unixtime_pred.tolist())))
    if len(missing_timestep) == 0:
        return unixtime_pred, prediction
    logger.warning(
        f"{len(missing_timestep)} elements are missing from prediction.: {missing_timestep}")

    for ts in missing_timestep:
        ind = np.where(unixtime_gt == ts)[0][0]

        val = prediction[ind - 1] if ind > 0 else -1
        unixtime_pred = np.insert(unixtime_pred, ind, ts)
        prediction = np.insert(prediction, ind, val)

        logger.warning(
            f"fill missing element at ts={ts} (ind={ind}) with {val}.")

        # DEBUG: Remove before merge
        delta = set(unixtime_gt[:ind]) - set(unixtime_pred[:ind])
        assert len(delta) == 0, delta

    assert len(unixtime_pred) == len(unixtime_gt), (
        f"unixtime_pred={unixtime_pred.shape}, unixtime_gt={unixtime_gt.shape}"
    )
    assert len(prediction) == len(unixtime_gt), (
        f"prediction={prediction.shape}, unixtime_gt={unixtime_gt.shape}"
    )
    return unixtime_pred, prediction


def crop_prediction_sequence(
    unixtime_gt: np.ndarray,
    unixtime_pred: np.ndarray,
    prediction: np.ndarray,
):
    """Crop prediction array to have the same timestamp as reference data.
    Args:
        unixtime_gt (np.ndarray): unixtimes of the ground truth sequence
        unixtime_pred (np.ndarray): unixtimes of the prediction sequence
        prediction (np.ndarray): -
    """
    ts_head, ts_tail = unixtime_gt[0], unixtime_gt[-1]
    logger.debug(f"ground truth: ts_head={ts_head}, ts_tail={ts_tail}")
    logger.debug(
        f"prediction  : ts_head={int(unixtime_pred[0])}, ts_tail={int(unixtime_pred[-1])}")

    ind = np.where((unixtime_pred >= ts_head) & (unixtime_pred <= ts_tail))[0]
    logger.debug(
        f"ind={ind.shape}, unixtime_pred={unixtime_pred.shape}, prediction={prediction.shape}")

    unixtime_pred = unixtime_pred[ind]
    prediction = prediction[ind]

    unixtime_pred, prediction = ffill_missing_elements(
        unixtime_gt,
        unixtime_pred,
        prediction,
    )

    return unixtime_pred, prediction


def construct_submission_dict(
    outputs: Dict[str, Dict[str, np.ndarray]],
    act_set: ActSet,
    include_ground_truth: Optional[bool] = False,
    cfg: Optional[DictConfig] = None,
) -> Dict:
    """Make dict that can be used for submission and `eval_workprocess_segmentation()` func.
    Args:
        outputs (Dict[str, Dict[str, np.ndarray]]): key is expected to be a pair of user and
            session. e.g., "U0102-S0100".
        act_set (ActSet): -
        include_ground_truth (bool, optional): If True, ground truth labels are included
            in the submission dict. Set True when you calculate scores.
        cfg (DictConfig, optional): config dict.
    Returns:
        Dict: submission dict
    """
    submission = dict()

    keys = sorted(outputs.keys())
    for key in keys:
        d = outputs[key]
        record = dict()
        user, session = key.split("-")

        assert d["y"].ndim == 3
        assert d["unixtime"].dtype == np.int64, (
            "unixtime must be np.int64, but got {}".format(d["unixtime"].dtype)
        )

        prediction_sess = act_set.convert_index_to_id(
            np.argmax(d["y"], axis=1).ravel())
        unixtime_pred_sess, prediction_sess = resample_prediction_1Hz(
            ts_unix=d["unixtime"].copy().ravel(), arr=prediction_sess)

        if include_ground_truth:
            with open_dict(cfg):
                cfg.user = {"name": user}
                cfg.session = session

            # TODO: Move to new function ( load_ground_truth() )
            if hasattr(cfg.dataset.annotation, "spec"):
                path = Path(
                    cfg.dataset.annotation.spec.path.dir,
                    cfg.dataset.annotation.spec.path.fname
                )
            else:
                path = Path(
                    cfg.dataset.annotation.path.dir,
                    cfg.dataset.annotation.path.fname
                )
            df_label = pd.read_csv(path)

            label_format = cfg.dataset.annotation.metadata.labels.get(
                "label_format", "")
            if label_format == "soft-target":
                cols = [c for c in df_label.columns if c.startswith("ID")]
                index_to_id = {i: int(c.replace("ID", ""))
                               for i, c in enumerate(cols)}
                df_label["index"] = np.argmax(df_label[cols].values, axis=1)
                df_label["id"] = df_label["index"].apply(
                    lambda ind: index_to_id[ind])

            unixtime_gt_sess = df_label["unixtime"].values
            ground_truth_sess = df_label["id"].values

            # check timestamp
            unixtime_pred_sess, prediction_sess = crop_prediction_sequence(
                unixtime_gt_sess, unixtime_pred_sess, prediction_sess)
            np.testing.assert_array_equal(unixtime_pred_sess, unixtime_gt_sess)

            record["ground_truth"] = ground_truth_sess.copy()

        record["unixtime"] = unixtime_pred_sess.copy()
        record["prediction"] = prediction_sess.copy()
        submission[key] = record

    return submission


def make_submission_zipfile(
        submission: Dict,
        logdir: Path,
        metadata: dict = None) -> None:
    """Check dict contents and generate zip file for codalab submission.

    Args:
        submission (Dict): submission dict
        logdir (Path): path to the output directory
        metadata (dict): dict of additional information that is included in
            ``submission.json``. We recommend to include a data split name.
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

    # Add meta data
    if metadata is not None:
        submission_clean["meta"] = metadata

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
    cfg: DictConfig,
    outputs: Dict[str, Dict[str, np.ndarray]],
    act_set: ActSet = ActSet(OPENPACK_OPERATIONS),
    exclude_ignore_class=True,
) -> pd.DataFrame:
    """ Compute evaluation metrics from model outputs (predicted probability).
    Args:
        cfg (DictConfig): config dict.
        outputs (Dict[str, Dict[str, np.ndarray]]): dict object that contains t_idx and y.
            t_idx is a 2d array of target class index with shape=(BATCH_SIZE, WINDOW).
            y is a 3d array of predction probabilities with shape=(BATCH_SIZE, NUM_CLASSES, WINDOW).
        act_set (ActSete, optional): class definition.
        exclude_ignore_class (bool): If true, ignore classes are excluded. (default: True)
    Returns:
        pd.DataFrame
    """
    submission = construct_submission_dict(
        outputs, act_set, include_ground_truth=True, cfg=cfg)
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
