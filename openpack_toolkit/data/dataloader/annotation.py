from logging import getLogger
from pathlib import Path

import numpy as np
import pandas as pd

from openpack_toolkit.activity import ActSet
from openpack_toolkit.data.const import (
    CLASS_ID_KEY_NAME,
    END_ISO_TIMESTMAP_KEY_NAME,
    END_UNIX_TIME_KEY_NAME,
    NULL_OPERATION_CLASS_ID,
    START_ISO_TIMESTMAP_KEY_NAME,
    START_UNIX_TIME_KEY_NAME,
    TIMESTAMP_KEY_NAME,
)
from openpack_toolkit.utils.time import convert_iso_timestamp_to_unixttime

OPERATION_LABEL_KEY_NAME = "operation"
ACTION_LABEL_KEY_NAME = "action"

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


def add_label_cols_to_dataframe(
    df_data: pd.DataFrame,
    df_label: pd.DataFrame,
    src_label_col_name: str = CLASS_ID_KEY_NAME,
    new_label_col_name: str = OPERATION_LABEL_KEY_NAME,
    null_label_class_id: int = NULL_OPERATION_CLASS_ID,
) -> pd.DataFrame:
    """Add label columns to the df_data.
    Default params are set to add the work operation labels.

    Args:
        df_data: DataFrame with unixtime for each record.
        df_labels: DataFrame of the work operation labels.
        src_label_col_name: column name of the label IDs in the df_label.
        new_label_col_name: new column name of the label IDs in the df_data.
        null_label_class_id: class ID for the null label.
    """
    assert TIMESTAMP_KEY_NAME in df_data.columns
    assert (START_UNIX_TIME_KEY_NAME in df_label.columns) and (
        END_UNIX_TIME_KEY_NAME in df_label.columns
    )

    df_data.insert(loc=1, column=new_label_col_name, value=null_label_class_id)
    for _, row in df_label.iterrows():
        timestamp_start = row[START_UNIX_TIME_KEY_NAME]
        timestamp_end = row[END_UNIX_TIME_KEY_NAME]
        operation_id = row[src_label_col_name]

        indices = df_data[
            (df_data[TIMESTAMP_KEY_NAME] >= timestamp_start)
            & (df_data[TIMESTAMP_KEY_NAME] < timestamp_end)
        ].index
        df_data.loc[indices, new_label_col_name] = operation_id
    return df_data
