from logging import getLogger
from pathlib import Path
from typing import List, Tuple, Union

import numpy as np
import pandas as pd

logger = getLogger(__name__)


def load_imu(
    paths: Union[Tuple[Path, ...], List[Path]],
    use_acc: bool = True,
    use_gyro: bool = False,
    use_quat: bool = False,
    th: int = 30,
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
        th (int, optional): threshold of timestamp difference [ms].
            Default. 30 [ms] (<= 1 sample)
    Returns:
        Tuple[np.ndarray, np.ndarray]: unixtime and loaded sensor data.
    """
    assert isinstance(
        paths, (tuple, list)
    ), f"the first argument `paths` expects tuple of Path, not {type(paths)}."

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

        # NOTE: Error handling : ATR01 in U0101-S0500 has timestamp error.
        #       See an issue #87.
        if str(path).endswith("/U0101/atr/atr01/S0500.csv"):
            df = df.drop(0, axis=0)
            df = df.reset_index(drop=True)

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
            delta = np.abs(ts_list[i] - ts_ret)
            assert delta.max() < th, (
                f"max difference is {delta.max()} [ms], "
                f"but difference smaller than th={th} is allowed."
            )

    x_ret = np.concatenate(x_ret, axis=0)
    return ts_ret, x_ret
