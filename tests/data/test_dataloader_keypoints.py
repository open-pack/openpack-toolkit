import numpy as np

from samples.preprocessing.keypoints.build_kinect_2d_kpt_with_labels import (
    TIMESTAMP_KEY_NAME,
    convert_keypoints_array_to_dataframe,
)


def test_convert_keypoints_array_to_dataframe():
    n_dim, n_frames, n_joints = 3, 10, 17
    timestamps = np.arange(n_frames)
    keypoints = np.random.randint(0, 100, size=(n_dim, n_frames, n_joints))

    df = convert_keypoints_array_to_dataframe(timestamps, keypoints)

    assert df.shape[0] == n_frames
    assert df.shape[1] == 1 + n_joints * n_dim
    assert df[TIMESTAMP_KEY_NAME].dtype == int
