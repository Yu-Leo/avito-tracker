import pytest
from fastapi import HTTPException, status

from tracker.utils import check_start_and_end_datetime


@pytest.mark.parametrize('start, end', [(None, None),
                                        ('2022-08-13T10:00:00', '2022-08-13T10:00:00'),
                                        ('2022-08-13T10:00', '2022-08-13T10:00'),
                                        ('2022-08-13', '2022-08-13'),
                                        ('2022-08-13T10:00:00', None),
                                        (None, '2022-08-13T10:00'), ])
def test_check_start_and_end_datetime_with_correct_values(start, end):
    check_start_and_end_datetime(start, end)


@pytest.mark.parametrize('start, end', [('123', None),
                                        ('asdfadsfasdf', None),
                                        (None, 'asdfadsfasdf',),
                                        ('1133422', 'asdfadsfasdf',), ])
def test_check_start_and_end_datetime_with_incorrect_values(start, end):
    with pytest.raises(HTTPException) as exception:
        check_start_and_end_datetime(start, end)
    assert exception.value.status_code == status.HTTP_400_BAD_REQUEST
