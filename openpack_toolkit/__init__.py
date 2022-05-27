"""
.. include:: ../README.md
"""

__version__ = '0.1.0'
from . import data
from .activity import OPENPACK_OPERATIONS, ActClass, ActSet

__all__ = [
    "OPENPACK_OPERATIONS", "ActClass", "ActSet", "data"
]
