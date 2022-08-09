from typing import List, Dict

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import crud
from core.utils import get_db
from schemas import AvitoRequestCreate, RequestValuesBase

router = APIRouter()


@router.post('/add')
def add_avito_request(item: AvitoRequestCreate, db: Session = Depends(get_db)):
    avito_request = crud.create_avito_request(db, item)
    crud.create_request_value(db, avito_request)
    return {'id': avito_request.id}


@router.get('/stat', response_model=Dict[str, List[RequestValuesBase]])
def get_request_values(id: int, start: str = None, end: str = None, db: Session = Depends(get_db)):
    request_values = crud.get_request_values(db, id, start, end)
    return {'values': request_values}
