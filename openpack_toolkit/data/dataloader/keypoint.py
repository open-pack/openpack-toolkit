import json
from logging import getLogger
from pathlib import Path
from typing import Tuple

import numpy as np
import pandas as pd

from openpack_toolkit.data.const import TIMESTAMP_KEY_NAME

logger = getLogger(__name__)

COORDINATE_KEY_NAME_TEMPLATE = "J{joint_idx:0=2}_D{dim_idx}"


def load_keypoints(path: Path) -> Tuple[np.ndarray, np.ndarray]:
    """Load keypoints from JSON.

    Args:
        path (Path): path to a target JSON file.
    Returns:
        Tuple[np.ndarray, np.ndarray]:
            * T (np.ndarray): unixtime for each frame.
            * X (np.ndarray): xy-cordinates of keypoints. and the score of corresponding
                prediction. shape=(3, FRAMES, NODE). The first dim is corresponding to
                [x-cordinate, y-cordinate, score].
    Todo:
        * Handle the JSON file that contains keypoints from multiple people.
    """
    with open(path, "r") as f:
        data = json.load(f)
    logger.debug(f"load keypoints from {path}")

    T, X = [], []
    for i, d in enumerate(data["annotations"][:]):
        ut = d.get("image_id", -1)
        kp = np.array(d.get("keypoints", []))

        X.append(kp.T)
        T.append(ut)

    T = np.array(T)
    X = np.stack(X, axis=1)

    return T, X


def convert_keypoints_array_to_dataframe(
    timestamps: np.ndarray, keypoints: np.ndarray
) -> pd.DataFrame:
    """
    Args:
        timestamp: unixt timestamp at millisecond precision, shape (n_frames,)
        keypoints: shape (3, n_frames, n_joints)
    Returns:
        DataFrame with columns [TIMESTAMP_KEY_NAME + J00_D0, J00_D1, J00_D2, J01_D0, ...]
        In the 2d keypoints, D0, D1 and D2 are x-axis, y-axis, and score, respectively.
    """
    assert keypoints.ndim == 3 and keypoints.shape[0] == 3
    assert timestamps.shape[0] == keypoints.shape[1]

    n_dim, n_frames, n_joints = keypoints.shape
    keypoints = keypoints.transpose(1, 2, 0).reshape(n_frames, n_joints * n_dim)

    df_timestamp = pd.DataFrame({TIMESTAMP_KEY_NAME: timestamps})
    columns = [
        COORDINATE_KEY_NAME_TEMPLATE.format(joint_idx=joint_idx, dim_idx=dim_idx)
        for joint_idx in range(n_joints)
        for dim_idx in range(n_dim)
    ]
    df_keypoints = pd.DataFrame(keypoints, columns=columns)
    df = pd.concat([df_timestamp, df_keypoints], axis=1)
    return df
