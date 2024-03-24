from logging import getLogger
from pathlib import Path

import numpy as np
import pandas as pd

from openpack_toolkit.activity import ActSet
from openpack_toolkit.data.const import (
    END_ISO_TIMESTMAP_KEY_NAME,
    END_UNIX_TIME_KEY_NAME,
    START_ISO_TIMESTMAP_KEY_NAME,
    START_UNIX_TIME_KEY_NAME,
)
from openpack_toolkit.utils.time import convert_iso_timestamp_to_unixttime

logger = getLogger(__name__)


def load_and_resample_annotation(
    path: Path,
    unixtimes_ms: np.ndarray,
    classes: ActSet,
    label_col: str = "id",
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
    logger.debug(f"load annotation data from {path} -> df={df.shape}")
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

    cols = ["unixtime", "annot_time", "user", "session", "box", "act_id", "act_idx"]
    return df[cols]


def load_and_resample_operation_labels(
    path: Path,
    unixtimes_ms: np.ndarray,
    classes: ActSet,
) -> pd.DataFrame:
    return load_and_resample_annotation(path, unixtimes_ms, classes, label_col="id")


def load_annotation_csv(path: Path) -> pd.DataFrame:
    """Load ground truth label CSV and convert start/end timestamp into unix time (millisecond precision)."""
    df = pd.read_csv(path)

    # Timestamps in annotation data are saved in ISO format (e.g., 2021-10-14 11:25:35.437000+09:00) for human
    # readability. So we have to convert them into unixtimestamp (milli-second precision) in advance.
    df[START_UNIX_TIME_KEY_NAME] = df[START_ISO_TIMESTMAP_KEY_NAME].apply(
        convert_iso_timestamp_to_unixttime
    )
    df[END_UNIX_TIME_KEY_NAME] = df[END_ISO_TIMESTMAP_KEY_NAME].apply(
        convert_iso_timestamp_to_unixttime
    )

    logger.info(f"Load annotation data from {path}")
    return df
