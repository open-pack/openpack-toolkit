"""Activity set definitions for OpenPack dataset.
"""
from dataclasses import dataclass
from logging import getLogger
from typing import Tuple, Union

import numpy as np

from ..configs import Label

logger = getLogger(__name__)


ActClass = Label

@dataclass
class ActSet():
    """ActSet binds activity classes and proved methods that can be useful when you apply machine
    learning approach. Activity class definition of OpenPack dataset will be provided in this
    format.
    """
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

    def __call__(self, cls_idx: int) -> ActClass:
        """Return ActClass object at index=``cls_idx``.

        Args:
            cls_idx (int): ckass index

        Returns:
            ActClass
        """
        return self.classes[cls_idx]

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
        When there is no ignore classe, return None.

        Returns:
            Union[int, Tuple] or None
        """
        index = tuple([i for i, act in enumerate(
            self.classes) if act.is_ignore])
        if len(index) == 0:
            return None
        if len(index) == 1:
            return index[0]
        return index

    def get_ignore_class_id(self) -> Union[int, Tuple]:
        """Return the ID of ignore classes, i.e., ``is_ignore=True``.
        If there are only one ignore class, return the ID as int.
        When there is no ignore classe, return None.

        Returns:
            Union[int, Tuple] or None
        """
        ids = tuple([act.id for act in self.classes if act.is_ignore])
        if len(ids) == 0:
            return None
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
        assert set(ids.ravel()) <= set(self.get_ids()), (
            f"expected ID set is {set(self.get_ids())}, "
            f"but got ID set={set(ids.ravel())}."
        )

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
            f"given index have out of range value(s)([0, {len(self.classes)}])."
            f" index.min()={index.min()}, index.max={index.max()}"
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
