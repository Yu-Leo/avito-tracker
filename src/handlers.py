from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import crud
from core.utils import get_db
from schemas import AvitoRequestCreate

router = APIRouter()


@router.post('/add')
def add_avito_request(item: AvitoRequestCreate, db: Session = Depends(get_db)):
    avito_request = crud.create_avito_request(db, item)
    return {"id": avito_request.id}
