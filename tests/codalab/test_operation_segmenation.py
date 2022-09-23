"""
Note:
    This example is from https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_fscore_support.html
"""
import time
from pathlib import Path

import numpy as np
import pandas as pd
import pytest
from omegaconf import OmegaConf

import openpack_toolkit as optk
from openpack_toolkit import OPENPACK_OPERATIONS
from openpack_toolkit.codalab.operation_segmentation.eval import (
    calc_avg_metrics,
    calc_class_metrics,
    drop_ignore_class,
    eval_operation_segmentation,
)
from openpack_toolkit.codalab.operation_segmentation.utils import (  # crop_seq_with_user_config,
    eval_operation_segmentation_wrapper,
    resample_prediction_1Hz,
)


@pytest.fixture
def example_01():
    classes = (
        (100, "cat"),
        (200, "dog"),
        (300, "pig"),
    )
    class_ids = tuple([t[0] for t in classes])
    t = np.array([100, 200, 300, 100, 200, 300, ])
    y = np.array([100, 300, 200, 100, 100, 200, ])

    return {
        "classes": classes,
        "class_ids": class_ids,
        "t": t,
        "y": y,
    }


""" eval.py
"""


def test_calc_metrics_for_each_class__01(example_01):
    classes = example_01["classes"]
    t = example_01["t"]
    y = example_01["y"]

    expect = pd.DataFrame({
        "id": [100, 200, 300],  # class ID
        "name": ["cat", "dog", "pig"],
        "precision": [2. / 3., 0., 0.],  # = TP / (TP+FP)
        "recall": [2. / 2., 0., 0., ],  # = TP / (TP+FN)
        "f1": [0.8, 0., 0., ],
        "support": [2, 2, 2]  # = the number of True sample; TP+FN
    })

    df_scores = calc_class_metrics(t, y, classes)
    print("df_scoers:", df_scores.shape)
    print(df_scores)

    pd.testing.assert_frame_equal(df_scores, expect)


def test_drop_ignore_class__01():
    ignore_class_id = 500
    t_id = np.array([100, 200, 300, 400, 500, 600, 700, 800, 900])
    # NOTE: index 6 cause warning. (ignore_class exists in y_id)
    y_id = np.array([100, 200, 300, 400, 500, 600, 700, 800, 900])

    expect1 = np.array([100, 200, 300, 400, 600, 700, 800, 900])
    expect2 = np.array([100, 200, 300, 400, 600, 700, 800, 900])

    actual1, actual2 = drop_ignore_class(t_id, y_id, ignore_class_id)
    np.testing.assert_array_equal(actual1, expect1)
    np.testing.assert_array_equal(actual2, expect2)


def test_calc_avg_metrics__01(example_01):
    """ average = macro
    """
    classes = example_01["classes"]
    t_id = example_01["t"]
    y_id = example_01["y"]

    expect = pd.DataFrame({
        "id": [-1],
        "name": ["avg/macro"],
        "precision": [0.2222222],
        "recall": [0.3333333],
        "f1": [0.2666667],
        "support": [None],
    })

    df = calc_avg_metrics(t_id, y_id, classes, average="macro")
    print("df:")
    print(df)

    pd.testing.assert_frame_equal(df, expect)


def test_calc_avg_metrics__02(example_01):
    """average = weighted
    """
    classes = example_01["classes"]
    t_id = example_01["t"]
    y_id = example_01["y"]

    expect = pd.DataFrame({
        "id": [-1],
        "name": ["avg/weighted"],
        "precision": [0.2222222],
        "recall": [0.3333333],
        "f1": [0.2666667],
        "support": [None],
    })

    df = calc_avg_metrics(t_id, y_id, classes, average="weighted")
    print("df:")
    print(df)

    pd.testing.assert_frame_equal(df, expect)


def test_eval_operation_segmentation__01(example_01):
    classes = example_01["classes"]
    t = example_01["t"]
    y = example_01["y"]

    expect = pd.DataFrame({
        "name": ["avg/macro", "avg/weighted"],
        "id": [-1, -1],
        "precision": [0.222222, 0.222222],
        "recall": [0.333333, 0.333333],
        "f1": [0.266667, 0.266667],
        "support": [None, None]
    }).set_index("name")

    df_scores = eval_operation_segmentation(t, y, classes, mode="final")
    print(f"df_scores[final] = {df_scores.shape}")
    print(df_scores)

    pd.testing.assert_frame_equal(df_scores, expect)


def test_eval_operation_segmentation__02(example_01):
    classes = example_01["classes"]
    t = example_01["t"]
    y = example_01["y"]

    expect = pd.DataFrame({
        "name": ["avg/macro", "avg/weighted", "cat", "dog", "pig"],
        "id": [-1, -1, 100, 200, 300],
        "precision": [0.222222, 0.222222, 0.666667, 0.0, 0.0],
        "recall": [0.333333, 0.333333, 1.0, 0.0, 0.0],
        "f1": [0.266667, 0.266667, 0.8, 0.0, 0.0],
        "support": [None, None, 2, 2, 2]
    }).set_index("name")

    df_scores = eval_operation_segmentation(t, y, classes, mode="feedback")
    print(f"df_scores[feedback] = {df_scores.shape}")
    print(df_scores)

    df_scores["support"] = df_scores["support"].astype(np.float64)
    pd.testing.assert_frame_equal(df_scores, expect)


""" utils.py
"""


def test_resample_prediction_1Hz__01():
    ts_unix = np.array([
        1000000, 1000500, 1001000, 1001500, 1002000, 1002500, 1003000,
    ])
    labels = np.array([
        100, 100, 100, 200, 300, 300, 400,
    ])

    expect_ts_unix = np.array([
        1000000, 1001000, 1002000, 1003000,
    ])
    expect_labels = np.array([
        100, 200, 300, 400,
    ])

    actual_ts_unix, actual_labels = resample_prediction_1Hz(ts_unix, labels)
    print("labels:")
    print(actual_labels)
    print("ts_unix:")
    print(actual_ts_unix)

    np.testing.assert_array_equal(actual_ts_unix, expect_ts_unix)
    np.testing.assert_array_equal(actual_labels, expect_labels)


def test_resample_prediction_1Hz__02():
    """Check computation time.
    """
    T = int(1e6)
    class_ids = (100, 200, 300, 400, 500)
    ts_unix = np.arange(0, T * 10, 10) + 1000000
    t_id = np.random.choice(class_ids, size=T)
    print(f"T={T}, t_id={t_id.shape}, ts_unix={ts_unix.shape}")

    ts_start = time.time()
    ts_unix_out, t_id_out = resample_prediction_1Hz(ts_unix, t_id)
    elapsed_time = time.time() - ts_start
    print(f"elapsed time: {elapsed_time:.5f} sec")

    assert elapsed_time < 1.0


@pytest.mark.parametrize("mode", ("test",))
def test_eval_operation_segmentation_wrapper__01(mode):
    T = int(30 * 60 * 50)
    W = 30 * 60
    class_ids = OPENPACK_OPERATIONS.get_ids()
    print(class_ids)

    rootdir = Path(__file__).parents[2] / "samples/openpack/${.version}"
    cfg = OmegaConf.create({
        "mode": mode,
        "user": optk.configs.users.U0102,
        "session": "S0500",
        "path": {
            "openpack": {
                "version": optk.DATASET_VERSION,
                "rootdir": str(rootdir),
            }
        },
        "dataset": {
            "stream": None,
            "annotation": optk.configs.datasets.annotations.ACTIVITY_1S_ANNOTATION,
        }
    })

    t_idx = np.random.choice(len(class_ids), size=T).reshape(T // W, W)
    y = np.random.uniform(size=(T // W, len(class_ids) - 1, W))
    ts_unix = np.arange(0, T) * 100 + 1634885786000
    print(f"t_idx={t_idx.shape}, y={y.shape}")
    print("ts_unix:", ts_unix[:100])

    outputs = {
        "U0102-S0500": {
            "ground_truth": t_idx, "y": y, "unixtime": ts_unix,
        }
    }
    df_score = eval_operation_segmentation_wrapper(cfg, outputs)
    print(df_score)

    # NOTE: 26 = (len(classes) - ignore_class + 2) * (num_sessions + 1)
    np.testing.assert_array_equal(df_score.shape, (24, 7))
