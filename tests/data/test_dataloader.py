from pathlib import Path

import numpy as np
import pandas as pd
import pytest
from omegaconf import DictConfig, OmegaConf, open_dict

import openpack_toolkit as optk
from openpack_toolkit import OPENPACK_OPERATIONS, ActSet
from openpack_toolkit.data.dataloader import (
    load_and_resample_operation_labels,
    load_and_resample_scan_log,
    load_imu,
    load_keypoints,
)


@pytest.fixture()
def cfg() -> DictConfig:
    rootdir = Path(__file__).parents[2] / "samples/openpack/${.version}"

    config = OmegaConf.create(
        {
            "user": optk.configs.users.U0209,
            "session": "S0500",
            "path": {
                "openpack": {
                    "version": optk.SAMPLE_DATASET_VERSION,
                    "rootdir": str(rootdir),
                }
            },
        }
    )
    return config


def test_load_and_resample_operation_labels__01(cfg):
    with open_dict(cfg):
        cfg.dataset = {
            "annotation": optk.configs.datasets.annotations.OPENPACK_OPERATIONS_1HZ_ANNOTATION
        }

    path = Path(
        cfg.dataset.annotation.path.dir,
        cfg.dataset.annotation.path.fname,
    )
    print(f"input path: {path} (exists={path.exists()})")

    unixtimes = np.array(
        [
            1648531522000,
            1648531522200,  # Resampling 1
            1648531522400,  # Resampling 2
            1648531522600,  # Resampling 3
            1648531522800,  # Resampling 4
            1648531523000,
        ]
    )

    expect = pd.DataFrame(
        [
            [1648531522000, 1648531522000, "U0209", "S0500", 1, 100, 0],
            [1648531522200, 1648531522000, "U0209", "S0500", 1, 100, 0],
            [1648531522400, 1648531522000, "U0209", "S0500", 1, 100, 0],
            [1648531522600, 1648531522000, "U0209", "S0500", 1, 100, 0],
            [1648531522800, 1648531522000, "U0209", "S0500", 1, 100, 0],
            [1648531523000, 1648531523000, "U0209", "S0500", 1, 100, 0],
        ],
        columns=["unixtime", "annot_time", "user", "session", "box", "act_id", "act_idx"],
    )

    df_annot = load_and_resample_operation_labels(
        path, unixtimes, classes=ActSet(OPENPACK_OPERATIONS)
    )
    print(df_annot)
    pd.testing.assert_frame_equal(df_annot.iloc[:, 2:], expect.iloc[:, 2:])


def test_load_keypoints__01(cfg):
    with open_dict(cfg):
        cfg.dataset = {"stream": optk.configs.datasets.streams.KINECT_2D_KPT_STREAM}

    path = Path(
        cfg.dataset.stream.path.dir,
        cfg.dataset.stream.path.fname,
    )
    print(f"input path: {path} (exists={path.exists()})")

    T, X = load_keypoints(path)
    np.testing.assert_array_equal(T.shape, (21376,))
    np.testing.assert_array_equal(X.shape, (3, 21376, 17))


@pytest.mark.parametrize(
    "stream, expected_ch",
    (
        (optk.configs.datasets.streams.ATR_ACC_STREAM, 3),
        (optk.configs.datasets.streams.ATR_QAGS_STREAM, 10),
    ),
)
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


def test_load_and_resample_scan_log__01(cfg):
    with open_dict(cfg):
        cfg.dataset = {"stream": optk.configs.datasets.streams.SYSTEM_HT_ORIGINAL_STREAM}

    path = Path(
        cfg.dataset.stream.path.dir,
        cfg.dataset.stream.path.fname,
    )
    print(f"input path: {path} (exists={path.exists()})")

    unixtimes = np.array(
        [
            1648531582600,
            1648531582800,
            1648531583000,  # =1 (1st item)
            1648531583200,  # =1
            1648531583400,  # =1
            1648531583600,  # =1
            1648531583800,  # =1
            1648531583900,  # =1 (2nd item)
            1648531583920,  # =1
            1648531583940,  # =1
        ]
    )

    expect = np.array([0, 0, 1, 1, 1, 1, 1, 1, 1, 1])

    actual = load_and_resample_scan_log(path, unixtimes)
    print(actual)
    np.testing.assert_array_equal(actual, expect)
