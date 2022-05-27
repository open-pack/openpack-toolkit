"""Activity Set in Open Pack

* Work-process level annotation

"""
from dataclasses import dataclass
from logging import getLogger
from typing import Tuple, Union

import numpy as np

logger = getLogger(__name__)


@dataclass
class ActClass():
    id: int
    name: str
    is_ignore: bool = False


@dataclass
class ActSet():
    classes: Tuple[ActClass, ...]

    def __len__(self) -> int:
        return len(self.classes)

    def __iter__(self):
        self._current = 0
        return self

    def __next__(self):
        if self._current == len(self.classes):
            raise StopIteration
        cls = self.classes[self._current]
        self._current += 1
        return cls

    def to_tuple(
        self, keep_actclass: bool = False,
    ) -> Union[Tuple[Tuple[int, str], ...], Tuple[ActClass, ...]]:
        """Returns a activity classes as a tuple.

        Args:
            keep_actclass (bool, optional): If True, return a tuple of ActClass.
                Otherwise, return a pure tuple, i.e., ``Tuple[Tuple[id:int, name:str], ...]``.
                Defaults to False.

        Returns:
            Union[Tuple[Tuple[int, str], ...], Tuple[ActClass, ...]]
        """
        if keep_actclass:
            return self.classes

        classes = [(cls.id, cls.name) for cls in self.classes]
        return tuple(classes)

    def get_ids(self) -> Tuple[int]:
        """Returns a tuple of class IDs.

        Returns:
            Tuple[int]
        """
        return tuple([act.id for act in self.classes])

    def get_ignore_class_index(self) -> Union[int, Tuple]:
        """Return the index of ignore classes, i.e., ``is_ignore=True``.
        If there are only one ignore class, return the index as int.

        Returns:
            Union[int, Tuple]
        """
        index = tuple([i for i, act in enumerate(
            self.classes) if act.is_ignore])
        if len(index) == 1:
            return index[0]
        return index

    def get_ignore_class_id(self) -> Union[int, Tuple]:
        """Return the ID of ignore classes, i.e., ``is_ignore=True``.
        If there are only one ignore class, return the ID as int.

        Returns:
            Union[int, Tuple]
        """
        ids = tuple([act.id for act in self.classes if act.is_ignore])
        if len(ids) == 1:
            return ids[0]
        return ids

    def convert_id_to_index(self, ids: np.ndarray) -> np.ndarray:
        """Translate activity ID into activity index.

        Args:
            ids (np.ndarray): 1d array of activity IDs.

        Returns:
            np.ndarray: 1d array of activity index.
        """
        assert set(ids.ravel()) <= set(self.get_ids())

        index = np.full(ids.shape, -1)
        for i, cls in enumerate(self.classes):
            index[ids == cls.id] = i
        assert index.min() >= 0

        return index.astype(np.int64)

    def convert_index_to_id(self, index: np.ndarray) -> np.ndarray:
        """Translate activity index into activity ID.

        Args:
            index (np.ndarray): 1d array of activity index.

        Returns:
            np.ndarray: 1d array of activity IDs.
        """
        assert min(self.get_ids()) >= 0
        assert (index.min() >= 0) and (index.max() < len(self.classes)), (
            "given index have out of range value(s)."
        )

        ids = np.full(index.shape, -1)
        for i, cls in enumerate(self.classes):
            ids[index == i] = cls.id
        assert ids.min() >= 0

        return ids.astype(np.int64)

    def id_to_name(self, cls_id: int) -> str:
        """Returns class name of the given class ID.

        Args:
            cls_id (int): class ID.

        Raises:
            ValueError: ``class_id`` does not exists in the activity set.

        Returns:
            str: class name
        """
        for cls in self.classes:
            if cls.id == cls_id:
                return cls.name
        raise ValueError(f"got unexpected class id. cls_id={cls_id}")

    def name_to_id(self, cls_name: str) -> int:
        """Returns class ID of the given class ID.

        Args:
            cls_name (str): class name.

        Raises:
            ValueError: ``class_name`` does not exists in the activity set.

        Returns:
            int: class id
        """
        for cls in self.classes:
            if cls.name == cls_name:
                return cls.id
        raise ValueError(f"got unexpected class name. cls_name={cls_name}")


""" Activity Set Definitions
"""

OPENPACK_OPERATIONS = ActSet((
    ActClass(100, "Picking"),
    ActClass(200, "MoveItemLabel"),
    ActClass(300, "AssembleBox"),
    ActClass(400, "PackInBox"),
    ActClass(500, "CloseBox"),
    ActClass(600, "ReadLabel"),
    ActClass(700, "AttachLabel"),
    ActClass(800, "PutOnCartRack"),
    ActClass(900, "Pen"),
    ActClass(1000, "Null", is_ignore=True),
))
