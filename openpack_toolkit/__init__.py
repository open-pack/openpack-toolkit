"""
.. include:: ../README.md
"""

__version__ = '0.5.0'
from . import codalab, configs, data, download, utils
from .activity import ActClass, ActSet
from .configs.datasets.annotations import OPENPACK_OPERATIONS

__all__ = [
    "ActClass",
    "ActSet",
    "codalab",
    "configs",
    "data",
    "download",
    "utils",
    "OPENPACK_OPERATIONS",
]
