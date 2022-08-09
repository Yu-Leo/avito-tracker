import datetime

from sqlalchemy.orm import Session
from models import AvitoRequest, RequestValues
from schemas import AvitoRequestCreate
import parser


def create_avito_request(db: Session, item: AvitoRequestCreate) -> AvitoRequest:
    avito_request = AvitoRequest(**item.dict())
    db.add(avito_request)
    db.commit()
    db.refresh(avito_request)
    return avito_request


def create_request_value(db: Session, item: AvitoRequest) -> RequestValues:
    request_value = RequestValues(avito_request_id=item.id,
                                  datetime=datetime.datetime.now(),
                                  value=parser.get_number_of_ads(item.text, item.region))
    db.add(request_value)
    db.commit()
    db.refresh(request_value)
    return request_value


def get_request_values(db: Session, id: int, start: str, end: str) -> list:
    request_values = list(db.query(RequestValues).filter(RequestValues.avito_request_id == id))
    return request_values
