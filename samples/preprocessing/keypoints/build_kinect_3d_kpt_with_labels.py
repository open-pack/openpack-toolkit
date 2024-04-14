import argparse
from pathlib import Path

import pandas as pd
from loguru import logger

from openpack_toolkit.data.const import CLASS_ID_KEY_NAME, NULL_ACTION_CLASS_ID, TIMESTAMP_KEY_NAME
from openpack_toolkit.data.dataloader.annotation import (
    add_label_cols_to_dataframe,
    load_annotation_csv,
)

OPERATION_LABEL_KEY_NAME = "operation"
ACTION_LABEL_KEY_NAME = "action"
UNIXTIME_KEY_NAME = "unixtime"


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Merge 3D keypoints with operation labels")
    parser.add_argument(
        "--kinect-3d-keypoints-path", type=Path, required=True, help="Path to the 3D keypoints"
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
    df_data = pd.read_csv(args.kinect_3d_keypoints_path)
    df_data.rename(columns={UNIXTIME_KEY_NAME: TIMESTAMP_KEY_NAME}, inplace=True)
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
    Path(args.output_path).parent.mkdir(parents=True, exist_ok=True)
    df_data.to_csv(args.output_path, index=False)
    logger.info(f"Save the merged data to {args.output_path}")


if __name__ == "__main__":
    args = make_parser().parse_args()
    main(args)
