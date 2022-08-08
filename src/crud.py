from sqlalchemy.orm import Session
from models import AvitoRequest
from schemas import AvitoRequestCreate


def create_avito_request(db: Session, item: AvitoRequestCreate):
    avito_request = AvitoRequest(**item.dict())
    db.add(avito_request)
    db.commit()
    db.refresh(avito_request)
    return avito_request
