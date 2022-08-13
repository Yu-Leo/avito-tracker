import datetime

import pytest

from tracker.schemas import convert_datetime_to_iso_8601_without_microseconds


@pytest.mark.parametrize('datetime, formatted_datetime',
                         [(datetime.datetime(2022, 8, 13, 10, 0, 0, 0), '2022-08-13T10:00:00'),
                          (datetime.datetime(2020, 8, 13, 10, 0, 0), '2020-08-13T10:00:00'), ])
def test_convert_datetime_to_iso_8601_without_microseconds(datetime, formatted_datetime):
    assert convert_datetime_to_iso_8601_without_microseconds(datetime) == formatted_datetime
