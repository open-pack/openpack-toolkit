import numpy as np
import pytest

from openpack_toolkit.activity import OPENPACK_WORKPROCESS_CLASSES, ActClass, ActSet


@pytest.fixture
def act_set():
    dummy_activity_set = ActSet((
        ActClass(100, "Act100"),
        ActClass(200, "Act200"),
        ActClass(300, "Act300"),
        ActClass(400, "Act400"),
        ActClass(1000, "Null", is_ignore=True),
    ))
    return dummy_activity_set


def test_ActSet__to_tuple__01(act_set):
    expect = (
        (100, "Act100"),
        (200, "Act200"),
        (300, "Act300"),
        (400, "Act400"),
        (1000, "Null"),
    )
    actual = act_set.to_tuple()

    np.testing.assert_array_equal(actual, expect)


def test_ActSet__to_tuple__02(act_set):
    expect = act_set.classes
    actual = act_set.to_tuple(keep_actclass=True)

    np.testing.assert_array_equal(actual, expect)


def test_ActSet__get_ids__01(act_set):
    expect = (100, 200, 300, 400, 1000)
    actual = act_set.get_ids()

    np.testing.assert_array_equal(actual, expect)


def test_ActSet__get_ignore_class_index__01(act_set):
    expect = 4
    actual = act_set.get_ignore_class_index()

    assert actual == expect


def test_ActSet__get_ignore_class_id__01(act_set):
    expect = 1000
    actual = act_set.get_ignore_class_id()

    assert actual == expect


""" Activity Set Definition
"""


def test_OPENPACK_WORKPROCESS_CLASSES__01():
    act_set = OPENPACK_WORKPROCESS_CLASSES

    # check datatype
    assert isinstance(act_set, ActSet)
    for act in act_set.classes:
        assert isinstance(act, ActClass), f"act={act}"

    # the number of activities
    assert len(act_set) == 10
