from pathlib import Path

from openpack_toolkit.data.const import (
    CLASS_ID_KEY_NAME,
    END_UNIX_TIME_KEY_NAME,
    START_UNIX_TIME_KEY_NAME,
    TIMESTAMP_KEY_NAME,
)
from openpack_toolkit.data.dataloader import load_keypoints
from openpack_toolkit.data.dataloader.annotation import load_annotation_csv
from openpack_toolkit.data.dataloader.keypoint import convert_keypoints_array_to_dataframe
from samples.preprocessing.keypoints.build_kinect_2d_kpt_with_labels import (
    OPERATION_LABEL_KEY_NAME,
    add_label_cols_to_dataframe,
)

pytest_plugins = "tests.data.dataset_fixtures"


def test_load_annotation_csv(operation_labels_path: Path):
    df = load_annotation_csv(operation_labels_path)

    assert START_UNIX_TIME_KEY_NAME in df.columns
    assert END_UNIX_TIME_KEY_NAME in df.columns
    assert CLASS_ID_KEY_NAME in df.columns


def test_add_labels_to_keypoints_dataframe(
    kinect_2d_keypoint_path: Path,
    operation_labels_path: Path,
):
    # Load data
    timestamps, keypoints = load_keypoints(kinect_2d_keypoint_path)
    df_data = convert_keypoints_array_to_dataframe(timestamps=timestamps, keypoints=keypoints)
    df_op = load_annotation_csv(operation_labels_path)
    # Test data
    label_ids_expect = {100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 8100}

    df_data = add_label_cols_to_dataframe(df_data, df_op)
    label_set_actual = set(df_data[OPERATION_LABEL_KEY_NAME])

    assert df_data[TIMESTAMP_KEY_NAME].dtype == int
    assert OPERATION_LABEL_KEY_NAME in df_data.columns
    assert (
        label_set_actual == label_ids_expect
    ), f"Actual: {label_set_actual}, Expect: {label_ids_expect}"
