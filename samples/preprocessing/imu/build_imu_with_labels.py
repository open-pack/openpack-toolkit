import argparse
from pathlib import Path

import numpy as np
import pandas as pd
from loguru import logger

from openpack_toolkit.data.const import CLASS_ID_KEY_NAME, NULL_ACTION_CLASS_ID, TIMESTAMP_KEY_NAME
from openpack_toolkit.data.dataloader.annotation import (
    add_label_cols_to_dataframe,
    load_annotation_csv,
)
from openpack_toolkit.data.dataloader.imu import load_imu

OPERATION_LABEL_KEY_NAME = "operation"
ACTION_LABEL_KEY_NAME = "action"
UNIXTIME_KEY_NAME = "unixtime"


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Merge 3D keypoints with operation labels")
    parser.add_argument(
        "--atr-root-dir",
        type=Path,
        required=True,
        help="Path to a root directory of atr. (e.g., `openpack/v1.0.0/U0209/atr/`)",
    )
    parser.add_argument(
        "--device",
        nargs="*",
        default=["atr01", "atr02", "atr03", "atr04"],
        help="Device name (e.g., atr01)",
    )
    parser.add_argument("--session", type=str, required=True, help="session ID (e.g., S0100)")
    parser.add_argument(
        "--operation-labels-path", type=Path, required=True, help="Path to the operation labels"
    )
    parser.add_argument(
        "--action-labels-path", type=Path, required=True, help="Path to the action labels"
    )
    parser.add_argument("--output-path", type=Path, required=True, help="Path to the output file")
    return parser


def load_imu_data(atr_root_dir: Path, devices: list[str], session_id: str) -> pd.DataFrame:
    """Load IMU data from CSVs and concatenate data from 4 devices into a single dataframe."""
    df_data = None
    paths = [atr_root_dir / device / f"{session_id}.csv" for device in devices]
    timestamps, data = load_imu(paths, use_acc=True, use_gyro=True, use_quat=True)

    # Make DataFrame
    df_data = pd.concat(
        [
            pd.DataFrame(np.expand_dims(timestamps, axis=1)),
            pd.DataFrame(data.T),
        ],
        ignore_index=True,
        axis=1,
    )

    # add columns
    axis_list = [
        "acc_x",
        "acc_y",
        "acc_z",
        "gyro_x",
        "gyro_y",
        "gyro_z",
        "quat_w",
        "quat_x",
        "quat_y",
        "quat_z",
    ]
    cols = [TIMESTAMP_KEY_NAME] + [f"{device}/{axis}" for device in devices for axis in axis_list]
    df_data.columns = cols
    return df_data


def main(args: argparse.Namespace):
    # Load input data
    df_data = load_imu_data(args.atr_root_dir, args.device, args.session)
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
