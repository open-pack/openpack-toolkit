import argparse
from pathlib import Path

import pandas as pd
from loguru import logger

from openpack_toolkit.data.const import (
    CLASS_ID_KEY_NAME,
    END_UNIX_TIME_KEY_NAME,
    NULL_ACTION_CLASS_ID,
    NULL_OPERATION_CLASS_ID,
    START_UNIX_TIME_KEY_NAME,
    TIMESTAMP_KEY_NAME,
)
from openpack_toolkit.data.dataloader import load_keypoints
from openpack_toolkit.data.dataloader.annotation import load_annotation_csv
from openpack_toolkit.data.dataloader.keypoint import convert_keypoints_array_to_dataframe

OPERATION_LABEL_KEY_NAME = "operation"
ACTION_LABEL_KEY_NAME = "action"


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


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Merge 2D keypoints with operation labels")
    parser.add_argument(
        "--kinect-2d-keypoints-path", type=Path, required=True, help="Path to the 2D keypoints"
    )
    parser.add_argument(
        "--operation-labels-path", type=Path, required=True, help="Path to the operation labels"
    )
    parser.add_argument(
        "--action-labels-path", type=Path, required=True, help="Path to the action labels"
    )
    parser.add_argument("--output-path", type=Path, required=True, help="Path to the output file")
    return parser


def main(args: argparse.Namespace):
    # Load input data
    timestamps, keypoints = load_keypoints(args.kinect_2d_keypoints_path)
    df_data = convert_keypoints_array_to_dataframe(timestamps=timestamps, keypoints=keypoints)
    df_operation_label = load_annotation_csv(args.operation_labels_path)
    df_action_label = load_annotation_csv(args.action_labels_path)

    # Merge data and labels
    df_data = add_label_cols_to_dataframe(
        df_data,
        df_action_label,
        src_label_col_name=CLASS_ID_KEY_NAME,
        new_label_col_name=ACTION_LABEL_KEY_NAME,
        null_label_class_id=NULL_ACTION_CLASS_ID,
    )
    df_data = add_label_cols_to_dataframe(df_data, df_operation_label)

    # Write dataset
    df_data.to_csv(args.output_path, index=False)
    logger.info(f"Save the merged data to {args.output_path}")


if __name__ == "__main__":
    args = make_parser().parse_args()
    main(args)
