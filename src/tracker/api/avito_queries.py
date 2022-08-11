from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, status

from tracker.schemas import AvitoQueryCreate, AvitoQueryValueBase
from tracker.services.avito_parser import is_avito_query_correct
from tracker.services.avito_queries import AvitoQueryService, AvitoQueryValueService

router = APIRouter()


@router.post('/add')
def add_avito_query(item: AvitoQueryCreate, avito_query_service: AvitoQueryService = Depends()):
    if not is_avito_query_correct(item):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Invalid value in the \'query\' or \'region\' field (for avito.ru)')
    avito_query = avito_query_service.create(item)
    return {'id': avito_query.id}


@router.get('/stat', response_model=List[AvitoQueryValueBase])
def get_avito_query_values(avito_query_id: int,
                           start: Optional[str] = None,
                           end: Optional[str] = None,
                           avito_query_value_service: AvitoQueryValueService = Depends()):
    avito_query_values = avito_query_value_service.get_by_avito_query_id(avito_query_id, start, end)
    return avito_query_values
