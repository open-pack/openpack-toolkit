"""
.. include:: ../README.md
"""

__version__ = '0.6.3'
from . import codalab, configs, data, download, utils
from .activity import ActClass, ActSet
from .configs.datasets.annotations import OPENPACK_OPERATIONS

DATASET_VERSION_LATEST = "v0.3.1"
DATASET_VERSION = DATASET_VERSION_LATEST
SAMPLE_DATASET_VERSION = "v0.3.0"


__all__ = [
    "ActClass",
    "ActSet",
    "codalab",
    "configs",
    "data",
    "download",
    "utils",
    "DATASET_VERSION",
    "OPENPACK_OPERATIONS",
]
