"""
.. include:: ../README.md
"""

__version__ = '0.3.0'
from . import codalab, configs, data, utils
from .activity import ActClass, ActSet
from .configs.datasets.annotations import OPENPACK_OPERATIONS

__all__ = [
    "ActClass",
    "ActSet",
    "codalab",
    "configs",
    "data",
    "OPENPACK_OPERATIONS",
    "utils",
]
