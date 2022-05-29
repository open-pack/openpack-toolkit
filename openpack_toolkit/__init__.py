"""
.. include:: ../README.md
"""

__version__ = '0.2.0'
from . import codalab, data, utils
from .activity import OPENPACK_OPERATIONS, ActClass, ActSet

__all__ = [
    "ActClass", "ActSet", "codalab", "data", "OPENPACK_OPERATIONS", "utils",
]
