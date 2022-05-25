"""Evaluation codes for Work-process Semantic Segmentation Task

This task is aimed to recognize 9 work-procsses in the mabual packing activity.
F1-measure with macro average is used as metrics.

Note:
    OpenPack Challenge uses `eval_workprocess_segmentation()` in `eval.py` for evaluation.

Todo:
    * Add task desciption.
    * Add usage (data format)
    * Add detail desciption of evaluation format.
"""
from .eval import eval_workprocess_segmentation
from .utils import (
    construct_submission_dict,
    eval_workprocess_segmentation_wrapper,
    make_submission_zipfile,
)

__all__ = [
    "construct_submission_dict",
    "eval_workprocess_segmentation",
    "eval_workprocess_segmentation_wrapper",
    "make_submission_zipfile",
]
