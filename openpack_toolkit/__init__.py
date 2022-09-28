"""
.. include:: ../README.md
"""

__version__ = '0.6.0'
from . import codalab, configs, data, download, utils
from .activity import ActClass, ActSet
from .configs.datasets.annotations import OPENPACK_OPERATIONS

DATASET_VERSION = "v0.3.0"

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
