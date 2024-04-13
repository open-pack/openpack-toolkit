#!/usr/bin python
import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from loguru import logger
from matplotlib.gridspec import GridSpec, GridSpecFromSubplotSpec

from openpack_toolkit.data.const import TIMESTAMP_KEY_NAME

SAMPLE_INDEX_KEY_NAME = "sample_index"
OPERATION_LABEL_KEY_NAME = "operation"
ACTION_LABEL_KEY_NAME = "action"
ACC_AXIS_NAMES = ["acc_x", "acc_y", "acc_z"]
GYRO_AXIS_NAMES = ["gyro_x", "gyro_y", "gyro_z"]
QUAT_AXIS_NAMES = ["quat_w", "quat_x", "quat_y", "quat_z"]
DEVICE_NAMES = ["atr01", "atr02", "atr03", "atr04"]
MAX_NON_NULL_LABEL_ID = 1005


def plot_annotation(df: pd.DataFrame, ax0: plt.Axes, label_key_name: str, color: str):
    df_label = df[df[label_key_name] < MAX_NON_NULL_LABEL_ID]
    ax0.plot(
        df_label[SAMPLE_INDEX_KEY_NAME],
        df_label[label_key_name],
        label=label_key_name,
        color=color,
    )
    ax0.legend(loc="upper right")
    ax0.set_title(
        label_key_name.capitalize(),
        fontsize="large",
        fontweight="bold",
    )


def plot_atr_session(
    df: pd.DataFrame,
    title: str = "Preprocessed Dataset: IMU + Operation Label + Action Label ",
    figsize=(30, 20),
):
    sns.set_theme("notebook", "darkgrid")
    fig = plt.figure(figsize=figsize)
    gs_master = GridSpec(nrows=7, ncols=1, height_ratios=[1, 1, 1, 3, 3, 3, 3])

    # Plot timestamp
    ax0 = fig.add_subplot(gs_master[0])
    ax0.plot(
        df[SAMPLE_INDEX_KEY_NAME], df[TIMESTAMP_KEY_NAME], label=TIMESTAMP_KEY_NAME.capitalize()
    )
    ax0.legend(loc="upper right")
    ax0.set_title(
        TIMESTAMP_KEY_NAME.capitalize(),
        fontsize="large",
        fontweight="bold",
    )

    # Plot Operation/Action Label
    ax0 = fig.add_subplot(gs_master[1])
    plot_annotation(df, ax0, OPERATION_LABEL_KEY_NAME, "C1")

    ax0 = fig.add_subplot(gs_master[2])
    plot_annotation(df, ax0, ACTION_LABEL_KEY_NAME, "C2")

    # Plot IMU data
    for i, device in enumerate(DEVICE_NAMES):
        gs_imu = GridSpecFromSubplotSpec(
            nrows=3, ncols=1, subplot_spec=gs_master[i + 3], hspace=0.01
        )
        sensors = [ACC_AXIS_NAMES, GYRO_AXIS_NAMES, QUAT_AXIS_NAMES]
        for sensor_idx, sensor_axis_names in enumerate(sensors):
            # Acc
            ax0 = fig.add_subplot(gs_imu[sensor_idx])
            for j, axis in enumerate(sensor_axis_names):
                col = f"{device}/{axis}"
                ax0.plot(df[SAMPLE_INDEX_KEY_NAME], df[col], label=col, color=f"C{j}")
            ax0.legend(loc="upper right")
            ax0.tick_params(labelbottom=False)
            if sensor_idx == 0:
                ax0.set_title(f"Sensor: atr/{device}", fontsize="large", fontweight="bold")
            if sensor_idx != 2:
                ax0.tick_params(labelbottom=False)

    fig.suptitle(title, fontsize="xx-large", fontweight="bold")
    fig.tight_layout()
    return fig


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Plot IMU data with operation and action labels.")
    parser.add_argument(
        "-i",
        "--input",
        type=Path,
        required=True,
        help="path to the preprocessed IMU data (e.g., `build/imu-with-operation-action-labels/U0209-S0500.csv`)",
    )
    return parser


def main(args: argparse.Namespace):
    # Load data
    df = pd.read_csv(args.input)
    df = df.reset_index(drop=False)
    df.rename(columns={"index": SAMPLE_INDEX_KEY_NAME}, inplace=True)

    fig = plot_atr_session(df)
    output_path = args.input.with_suffix(".png")
    fig.savefig(output_path)
    logger.info(f"Save figure to {output_path}")


if __name__ == "__main__":
    args = make_parser().parse_args()
    main(args)
