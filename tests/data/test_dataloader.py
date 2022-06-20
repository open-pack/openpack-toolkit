from pathlib import Path

import numpy as np
import pandas as pd
import pytest
from omegaconf import DictConfig, OmegaConf, open_dict

import openpack_toolkit as optk
from openpack_toolkit import OPENPACK_OPERATIONS
from openpack_toolkit.data.dataloader import (
    load_and_resample_operation_labels,
    load_imu,
    load_keypoints,
)


@pytest.fixture()
def cfg() -> DictConfig:
    rootdir = Path(__file__).parents[2] / "samples/openpack/vX.X.X"

    config = OmegaConf.create({
        "user": optk.configs.users.U0102,
        "session": "S0500",
        "path": {
            "openpack": {
                "rootdir": str(rootdir),
            }
        }
    })
    return config


def test_load_annotatation__01(cfg):
    with open_dict(cfg):
        cfg.dataset = {
            "annotation": optk.configs.datasets.annotations.OPENPACK_OPERATIONS_ANNOTATION}

    path = Path(
        cfg.dataset.annotation.path.dir,
        cfg.dataset.annotation.path.fname,
    )
    print(f"input path: {path} (exists={path.exists()})")

    unixtimes = np.array([
        1634885794000,
        1634885794200,  # Resampling 1
        1634885794400,  # Resampling 2
        1634885794600,  # Resampling 3
        1634885794800,  # Resampling 4
        1634885795000,
        1634885796000,
        1634885798000,  # Next Action
    ])

    expect = pd.DataFrame([
        [1634885794000, 1634885794000, 102, 500, 1, 100, 0],
        [1634885794200, 1634885794000, 102, 500, 1, 100, 0],
        [1634885794400, 1634885794000, 102, 500, 1, 100, 0],
        [1634885794600, 1634885794000, 102, 500, 1, 100, 0],
        [1634885794800, 1634885794000, 102, 500, 1, 100, 0],
        [1634885795000, 1634885795000, 102, 500, 1, 100, 0],
        [1634885796000, 1634885796000, 102, 500, 1, 200, 1],
        [1634885798000, 1634885798000, 102, 500, 1, 200, 1],
    ], columns=["unixtime", "annot_time", "user", "session", "box", "act_id", "act_idx"])

    df_annot = load_and_resample_operation_labels(
        path, unixtimes, classes=OPENPACK_OPERATIONS)
    print(df_annot)
    pd.testing.assert_frame_equal(df_annot, expect)


def test_load_keypoints__01(cfg):
    with open_dict(cfg):
        cfg.dataset = {
            "stream": optk.configs.datasets.streams.KINECT_2D_KPT_STREAM}

    path = Path(
        cfg.dataset.stream.path.dir,
        cfg.dataset.stream.path.fname,
    )
    print(f"input path: {path} (exists={path.exists()})")

    T, X = load_keypoints(path)
    np.testing.assert_array_equal(T.shape, (29423,))
    np.testing.assert_array_equal(X.shape, (3, 29423, 17))


@pytest.mark.parametrize("stream, expected_ch", (
    (optk.configs.datasets.streams.ATR_ACC_STREAM, 3),
    (optk.configs.datasets.streams.ATR_QAGS_STREAM, 10),
))
def test_load_imu__01(cfg, stream, expected_ch):
    with open_dict(cfg):
        cfg.dataset = {"stream": stream}
        cfg.device = "atr01"

    path = Path(
        cfg.dataset.stream.path.dir,
        cfg.dataset.stream.path.fname,
    )
    print(f"input path: {path} (exists={path.exists()})")

    T, X = load_imu(
        [path],
        use_acc=cfg.dataset.stream.acc,
        use_gyro=cfg.dataset.stream.gyro,
        use_quat=cfg.dataset.stream.quat,
    )
    assert T.shape[0] == X.shape[1]
    assert X.shape[0] == expected_ch
