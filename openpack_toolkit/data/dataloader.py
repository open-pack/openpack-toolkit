"""``dataloader`` provide utility function to load files saved in OpenPack dataset format.
"""
import json
from logging import getLogger
from pathlib import Path
from typing import List, Tuple, Union

import numpy as np
import pandas as pd

from ..activity import ActSet

logger = getLogger(__name__)


def load_annotation(
    path: Path,
    unixtimes_ms: np.ndarray,
    classes: ActSet,
    label_col: str = None,
) -> pd.DataFrame:
    """Load annotation data and resample them according to unixtime sequence ``T``.
    If there are no annotation records for the given timestamp, that records is treated
    as NULL class.

    Args:
        path (Path): path to annotation CSV file.
        unixitmes (np.ndarray): unixtime seqeuence (milli-scond precision).
    Returns:
        pd.DataFrame: -
    """
    null_class_id = classes.get_ignore_class_id()
    if isinstance(null_class_id, tuple):
        null_class_id = null_class_id[-1]

    df = pd.read_csv(path)
    ut_min, ut_max = df["unixtime"].min(), df["unixtime"].max()

    null_record = df.head(1).copy()
    null_record["unixtime"] = 0
    null_record["box"] = 0
    null_record[label_col] = null_class_id
    df = pd.concat([df, null_record], axis=0, ignore_index=True)

    # unixtime with second precision.
    unixtimes_sec = unixtimes_ms - (unixtimes_ms % 1000)
    # Assing 0 to non-annotated sequence.
    unixtimes_sec[unixtimes_sec < ut_min] = 0
    unixtimes_sec[unixtimes_sec > ut_max] = 0

    df = df.rename(columns={"unixtime": "annot_time"}).set_index("annot_time")
    df = df.loc[unixtimes_sec, :].reset_index(drop=False)
    df["unixtime"] = unixtimes_ms

    df["act_id"] = df[label_col]
    df["act_idx"] = classes.convert_id_to_index(df["act_id"].values)

    cols = [
        "unixtime",
        "annot_time",
        "user",
        "session",
        "box",
        "act_id",
        "act_idx"]
    return df[cols]


def load_and_resample_operation_labels(
    path: Path,
    unixtimes_ms: np.ndarray,
    classes: ActSet,
) -> pd.DataFrame:
    return load_annotation(path, unixtimes_ms, classes, label_col="operation")


def load_keypoints(path: Path) -> Tuple[np.ndarray, np.ndarray]:
    """Load keypoints from JSON.

    Args:
        path (Path): path to a target JSON file.
    Returns:
        Tuple[np.ndarray, np.ndarray]:
            * T (np.ndarray): unixtime for each frame.
            * X (np.ndarray): xy-cordinates of keypoints. and the score of corresponding
                prediction. shape=(3, FRAMES, NODE). The first dim is corresponding to
                [x-cordinate, y-cordinate, score].
    Todo:
        * Handle the JSON file that contains keypoints from multiple people.
    """
    with open(path, "r") as f:
        data = json.load(f)

    T, X = [], []
    for i, d in enumerate(data["annotations"][:]):
        ut = d.get("image_id", -1)
        kp = np.array(d.get("keypoints", []))

        X.append(kp.T)
        T.append(ut)

    T = np.array(T)
    X = np.stack(X, axis=1)

    return T, X


def load_imu(
    paths: Union[Tuple[Path, ...], List[Path]],
    use_acc: bool = True,
    use_gyro: bool = False,
    use_quat: bool = False,
    th: int = 10,
) -> Tuple[np.ndarray, np.ndarray]:
    """Load IMU data from CSVs.

    Args:
        paths (Union[Tuple[Path, ...], List[Path]]): list of paths to target CSV.
            (e.g., [**/atr01/S0100.csv])
        use_acc (bool, optional): include acceleration signal (e.g., ``acc_x, acc_y, acc_z``).
            Defaults to True.
        use_gyro (bool, optional): include gyro scope signal (e.g., ``gyro_x, gyro_y, gyro_z``).
            Defaults to False.
        use_quat (bool, optional): include quaternion data(e.g.,
            ``quat_w, quat_x, quat_y, quat_z``). Defaults to False.
        th (int, optional): threshold of timestamp difference. [ms]
    Returns:
        Tuple[np.ndarray, np.ndarray]: unixtime and loaded sensor data.
    """
    assert isinstance(paths, (tuple, list)), (
        f"the first argument `paths` expects tuple of Path, not {type(paths)}."
    )

    channels = []
    if use_acc:
        channels += ["acc_x", "acc_y", "acc_z"]
    if use_gyro:
        channels += ["gyro_x", "gyro_y", "gyro_z"]
    if use_quat:
        channels += ["quat_w", "quat_x", "quat_y", "quat_z"]

    ts_ret, x_ret, ts_list = None, [], []
    for path in paths:
        df = pd.read_csv(path)
        logger.debug(f"load IMU data from {path} -> df={df.shape}")
        assert set(channels) < set(df.columns)

        ts = df["unixtime"].values
        x = df[channels].values.T

        ts_list.append(ts)
        x_ret.append(x)

    min_len = min([len(ts) for ts in ts_list])
    ts_ret = None
    for i in range(len(paths)):
        x_ret[i] = x_ret[i][:, :min_len]
        ts_list[i] = ts_list[i][:min_len]

        if ts_ret is None:
            ts_ret = ts_list[i]
        else:
            # Check whether the timestamps are equal or not.
            assert np.abs(ts_list[i] - ts_ret).max() < th

    x_ret = np.concatenate(x_ret, axis=0)
    return ts_ret, x_ret
