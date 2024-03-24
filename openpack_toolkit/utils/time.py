import datetime


def convert_iso_timestamp_to_unixttime(timestamp_iso: str) -> int:
    """Convert a timestamp (ISO format; string) into a unix time with millisecond precision.
    For example, `2021-10-14 11:25:35.437000+09:00` will be `1634178335437`.
    """
    return int(datetime.datetime.fromisoformat(timestamp_iso).timestamp() * 1e3)
