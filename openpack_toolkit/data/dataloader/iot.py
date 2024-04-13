from logging import getLogger
from pathlib import Path

import numpy as np
import pandas as pd

logger = getLogger(__name__)


def load_and_resample_scan_log(
    path: Path,
    unixtimes_ms: np.ndarray,
) -> np.ndarray:
    """Load scan log data such as HT, and make binary vector for given timestamps.
    Elements that have the same timestamp in second precision are marked as 1.
    Other values are set to 0.

    Args:
        path (Path): path to a scan log CSV file.
        unixtimes_ms (np.ndarray):  unixtime seqeuence (milli-scond precision).
            shape=(T,).

    Returns:
        np.ndarray: binary 1d vector.
    """
    assert unixtimes_ms.ndim == 1
    df = pd.read_csv(path)
    logger.info(f"load scan log from {path} -> df={df.shape}")

    unixtimes_sec = unixtimes_ms // 1000

    X_log = np.zeros(len(unixtimes_ms)).astype(np.int32)
    for utime_ms in df["unixtime"].values:
        utime_sec = utime_ms // 1000
        ind = np.where(unixtimes_sec == utime_sec)[0]
        X_log[ind] = 1

    return X_log
