import pytest

from openpack_toolkit.utils.time import convert_iso_timestamp_to_unixttime


@pytest.mark.parametrize(
    "iso_timestamp,unixtime_expect", (("2021-10-14 11:25:35.437000+09:00", 1634178335437),)
)
def test_convert_iso_timestamp_to_unixttime(iso_timestamp: str, unixtime_expect: int):
    assert convert_iso_timestamp_to_unixttime(iso_timestamp) == unixtime_expect
