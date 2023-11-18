"""
.. include:: ../README.md
"""

__version__ = '1.0.1'
from . import codalab, configs, data, utils
from .activity import ActClass, ActSet
from .configs.datasets.annotations import OPENPACK_OPERATIONS

DATASET_VERSION_LATEST = "v1.0.0"
DATASET_VERSION = DATASET_VERSION_LATEST
SAMPLE_DATASET_VERSION = "v1.0.0"


__all__ = [
    "ActClass",
    "ActSet",
    "codalab",
    "configs",
    "data",
    "utils",
    "DATASET_VERSION",
    "OPENPACK_OPERATIONS",
]
