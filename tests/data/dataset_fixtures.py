from pathlib import Path

import pytest

_SAMPLE_DATASET_ROOTDIR = Path(__file__).parents[2] / "samples/openpack/v1.0.0"


@pytest.fixture
def operation_labels_path() -> Path:
    return Path(_SAMPLE_DATASET_ROOTDIR, "U0209/annotation/openpack-operations/S0500.csv")


@pytest.fixture
def kinect_2d_keypoint_path() -> Path:
    return Path(
        _SAMPLE_DATASET_ROOTDIR,
        "U0209/kinect/2d-kpt",
        "mmpose-hrnet-w48-posetrack18-384x288-posewarper-stage2/single",
        "S0500.json",
    )
