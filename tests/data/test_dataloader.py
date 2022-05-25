from pathlib import Path

import numpy as np
import pandas as pd

from openpack_toolkit.activity import OPENPACK_WORKPROCESS_CLASSES
from openpack_toolkit.data.dataloader import load_annotation, load_imu, load_keypoints


def test_load_annotatation__01():
    path = Path(__file__).parents[1] / "test_data/annotation_ex01.csv"
    unixtimes = np.array([
        1634869193000,
        1634869193500,
        1634869194000,
        1634869194500,
        1634869195000,
    ])

    expect = pd.DataFrame([
        [1634869193000, 1634869193000, 102, 100, 1, 100, 0],
        [1634869193500, 1634869193000, 102, 100, 1, 100, 0],
        [1634869194000, 1634869194000, 102, 100, 1, 100, 0],
        [1634869194500, 1634869194000, 102, 100, 1, 100, 0],
        [1634869195000, 1634869195000, 102, 100, 1, 100, 0],
    ], columns=["unixtime", "annot_time", "user", "session", "box", "act_id", "act_idx"])

    df_annot = load_annotation(
        path, unixtimes, classes=OPENPACK_WORKPROCESS_CLASSES)
    pd.testing.assert_frame_equal(df_annot, expect)


def test_load_keypoints__01():
    path = Path(__file__).parents[1] / "test_data/keypoints_ex01.json"

    T, X = load_keypoints(path)
    np.testing.assert_array_equal(T.shape, (100,))
    np.testing.assert_array_equal(X.shape, (3, 100, 17))


def test_load_imu__01():
    path = Path(__file__).parents[1] / "test_data/imu_ex01.csv"

    T, X = load_imu([path], use_acc=True, use_gyro=False, use_quat=False)
    np.testing.assert_array_equal(T.shape, (6000,))
    np.testing.assert_array_equal(X.shape, (3, 6000))
