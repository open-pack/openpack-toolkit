from typing import Tuple

import numpy as np
import pandas as pd
from sklearn.metrics import precision_recall_fscore_support

EVAL_METRICS = ("precision", "recall", "f1")


def verify_class_ids(
        y_id: np.ndarray, classes: Tuple[Tuple[int, str], ...]) -> bool:
    """Verify that y_id consists only of the desired class ID.
    Args:
        y_id (np.ndarray): predicted class IDs. shape=(T,)
        classes (Tuple[Tuple[int, str], ...]): class definition.
    Raises:
        ValueError: When y_id contains out of scope class id.
    Returns:
        bool: verification has passed.
    """
    class_ids = tuple([t[0] for t in classes])
    if set(y_id) <= set(class_ids):
        return True
    raise ValueError(f"y have invalid class ids[{set(class_ids) - set(y_id)}]")


def calc_class_metrics(t_id: np.ndarray, y_id: np.ndarray,
                       classes: Tuple[Tuple[int, str], ...]) -> pd.DataFrame:
    """
    Args:
        t_id (np.ndarray): ground truth class id. shape = (T,)
        y_id (np.ndarray): predicted class id. shape = (N_CLASSES, T)
        classes (Tuple): class definition.
    Returns:
        pd.DataFrame
    """
    class_ids = tuple([t[0] for t in classes])
    assert set(y_id) <= set(
        class_ids), f"y have invalid class ids[{set(class_ids) - set(y_id)}]"

    precision, recall, f1, support = precision_recall_fscore_support(
        t_id,
        y_id,
        average=None,
        labels=class_ids,
        zero_division=0,
    )

    df = []
    for i, (cls_id, cls_name) in enumerate(classes):
        df.append(
            {
                "id": cls_id,
                "name": cls_name,
                "precision": precision[i],
                "recall": recall[i],
                "f1": f1[i],
                "support": support[i],
            }
        )
    df = pd.DataFrame(df)
    return df


def calc_avg_metrics(t_id: np.ndarray, y_id: np.ndarray,
                     classes: Tuple[Tuple[int, str], ...], average: str = None) -> pd.DataFrame:
    """
    Args:
        t (np.ndarray): ground truth class id. shape = (N,)
        y (np.ndarray): predicted class id. shape = (N_CLASSES, N)
        classes (Tuple): class definition.
        average (str): this determines the type of averaging performed on the data.
            {macro, weighted}
    Returns:
        pd.DataFrame
    """
    assert average in ("macro", "weighted")

    class_ids = tuple([c[0] for c in classes])
    precision, recall, f1, support = precision_recall_fscore_support(
        t_id,
        y_id,
        average=average,
        labels=class_ids,
        zero_division=0,
    )

    df = pd.DataFrame([{
        "id": -1,
        "name": f"avg/{average}",
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "support": support,
    }])
    return df


def eval_workprocess_segmentation(
    t_id: np.ndarray = None,
    y_id: np.ndarray = None,
    classes: Tuple[Tuple[int, str], ...] = None,
    mode: str = "final",
) -> pd.DataFrame:
    """Compute metrics (i.e., precision, recall, f1, support) for the given sequence.
    Args:
        t_id (np.ndarray): unixtime and corresponding activity ID, shape=(T,)
        y_id (np.ndarray): unixtime and predicted activity ID, shape=(T,)
        classes (Tuple): class definition.
        mode (str): If final, only the macro score will be calculated. Otherwise,
            macro avg., weighted avg., and score for each class will be calculated.
    Returns:
        pd.DataFrame
    """
    assert t_id.ndim == 1
    assert y_id.ndim == 1
    verify_class_ids(y_id, classes)

    df_scores = [
        calc_avg_metrics(t_id, y_id, classes, average="macro"),
        calc_avg_metrics(t_id, y_id, classes, average="weighted"),
    ]
    if mode != "final":
        df_scores.append(
            calc_class_metrics(t_id, y_id, classes)
        )

    df_scores = pd.concat(
        df_scores,
        axis=0,
        ignore_index=True).set_index("name")
    return df_scores
