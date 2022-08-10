from typing import List, Optional

from fastapi import APIRouter, Depends

from tracker.schemas import AvitoQueryCreate, AvitoQueryValueBase
from tracker.services.avito_queries import AvitoQueryService, AvitoQueryValueService

router = APIRouter()


@router.post('/add')
def add_avito_request(item: AvitoQueryCreate, avito_query_service: AvitoQueryService = Depends()):
    avito_query = avito_query_service.create(item)
    return {'id': avito_query.id}


@router.get('/stat', response_model=List[AvitoQueryValueBase])
def get_request_values(avito_query_id: int,
                       start: Optional[str] = None,
                       end: Optional[str] = None,
                       avito_query_value_service: AvitoQueryValueService = Depends()):
    avito_query_values = avito_query_value_service.get_by_avito_query_id(avito_query_id, start, end)
    return avito_query_values
