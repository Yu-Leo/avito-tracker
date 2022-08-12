import datetime
from typing import Optional

from fastapi import HTTPException, status
from loguru import logger

from tracker.exceptions import AvitoQueryError, ParserError
from tracker.schemas import AvitoQueryCreate
from tracker.services.avito_parser import get_number_of_ads


def check_start_and_end_datetime(start: Optional[str] = None, end: Optional[str] = None) -> None:
    datetime_format = 'Datetime must be in ISO 8601 YYYY-MM-DDThh:mm:ss format (for example: 1985-10-26T01:18:00)'
    is_start_datetime_correct = _is_datetime_correct(start)
    is_end_datetime_correct = _is_datetime_correct(end)
    if not (is_start_datetime_correct and is_end_datetime_correct):
        if not is_start_datetime_correct and is_end_datetime_correct:
            detail_phrase = 'Invalid value in \'start\' field. '
        elif is_start_datetime_correct and not is_end_datetime_correct:
            detail_phrase = 'Invalid value in \'end\' field. '
        else:
            detail_phrase = 'Invalid value in \'start\' and \'end\' field. '

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=detail_phrase + datetime_format)


def check_avito_query(avito_query: AvitoQueryCreate):
    try:
        get_number_of_ads(avito_query.query, avito_query.region)
    except AvitoQueryError as error:
        logger.warning(error)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error))
    except ParserError as error:
        logger.error(error)
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=str(error))


def _is_datetime_correct(dt: Optional[str]) -> bool:
    if dt is None:
        return True
    try:
        datetime.datetime.fromisoformat(dt)
    except ValueError:
        return False
    else:
        return True
