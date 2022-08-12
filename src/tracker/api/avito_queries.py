from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from loguru import logger

from tracker import utils
from tracker.exceptions import DatabaseError
from tracker.schemas import AvitoQueryCreate, AvitoQueryValueBase
from tracker.services.avito_queries import AvitoQueryService, AvitoQueryValueService

router = APIRouter()


@router.post('/add')
def add_avito_query(avito_query_data: AvitoQueryCreate,
                    avito_query_service: AvitoQueryService = Depends()):
    utils.check_avito_query(avito_query_data)
    try:
        avito_query = avito_query_service.create(avito_query_data)
    except DatabaseError as error:
        logger.error(error)
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE)
    return {'id': avito_query.id}


@router.get('/stat', response_model=List[AvitoQueryValueBase])
def get_avito_query_values(avito_query_id: int,
                           start: Optional[str] = None,
                           end: Optional[str] = None,
                           avito_query_value_service: AvitoQueryValueService = Depends()):
    utils.check_start_and_end_datetime(start, end)
    try:
        avito_query_values = avito_query_value_service.get_by_avito_query_id(avito_query_id, start, end)
    except DatabaseError as error:
        logger.error(error)
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE)

    return avito_query_values
