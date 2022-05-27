import numpy as np
import pytest

from openpack_toolkit.activity import OPENPACK_OPERATIONS, ActClass, ActSet


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


def test_ActSet__iterator__01(act_set):
    cnt = 0
    for cls in act_set:
        print(cnt, cls)
        assert isinstance(cls, ActClass)
        cnt += 1

    assert cnt == 5
    assert cnt == len(act_set)


def test_ActSet__iterator__02(act_set):
    act_iter = iter(act_set)
    act_iter.__next__()  # 1
    act_iter.__next__()  # 2
    act_iter.__next__()  # 3
    act_iter.__next__()  # 4
    act_iter.__next__()  # 5

    with pytest.raises(StopIteration):
        act_iter.__next__()  # 6


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


def test_ActSet__convert_id_to_index__01(act_set):
    ids = np.array([100, 200, 300, 400, 1000, 100, 100])
    expect = np.array([0, 1, 2, 3, 4, 0, 0])

    actual = act_set.convert_id_to_index(ids)
    np.testing.assert_array_equal(actual, expect)


def test_ActSet__convert_id_to_index__02(act_set):
    ids = np.array([
        [100, 200, 300, 400, 1000, 100, 100],
        [200, 300, 400, 1000, 100, 100, 100],
    ])
    expect = np.array([
        [0, 1, 2, 3, 4, 0, 0],
        [1, 2, 3, 4, 0, 0, 0],
    ])

    actual = act_set.convert_id_to_index(ids)
    np.testing.assert_array_equal(actual, expect)


def test_ActSet__convert_index_to_id__01(act_set):
    index = np.array([0, 1, 2, 3, 4, 0, 0])
    expect = np.array([100, 200, 300, 400, 1000, 100, 100])

    actual = act_set.convert_index_to_id(index)
    np.testing.assert_array_equal(actual, expect)


def test_ActSet__convert_index_to_id__02(act_set):
    index = np.array([
        [0, 1, 2, 3, 4, 0, 0],
        [1, 2, 3, 4, 0, 0, 0],
    ])
    expect = np.array([
        [100, 200, 300, 400, 1000, 100, 100],
        [200, 300, 400, 1000, 100, 100, 100],
    ])

    actual = act_set.convert_index_to_id(index)
    np.testing.assert_array_equal(actual, expect)


def test_ActSet__convert__01(act_set):
    n = 1000
    index = np.random.choice([0, 1, 2, 3, 4], size=n)

    # Index to ID
    ids = act_set.convert_index_to_id(index)
    # ID to Index
    index_out = act_set.convert_id_to_index(ids)

    np.testing.assert_array_equal(index_out, index)


def test_ActSet__id_to_name__01(act_set):
    id_and_expect = (
        (100, "Act100"),
        (200, "Act200"),
        (300, "Act300"),
        (400, "Act400"),
        (1000, "Null"),
    )

    for cls_id, expect in id_and_expect:
        actual = act_set.id_to_name(cls_id)
        assert actual == expect


def test_ActSet__name_to_id__01(act_set):
    id_and_expect = (
        ("Act100", 100),
        ("Act200", 200),
        ("Act300", 300),
        ("Act400", 400),
        ("Null", 1000),
    )

    for cls_name, expect in id_and_expect:
        actual = act_set.name_to_id(cls_name)
        assert actual == expect


""" Activity Set Definition
"""


def test_OPENPACK_OPERATIONS__01():
    act_set = OPENPACK_OPERATIONS

    # check datatype
    assert isinstance(act_set, ActSet)
    for act in act_set.classes:
        assert isinstance(act, ActClass), f"act={act}"

    # the number of activities
    assert len(act_set) == 10
