import datetime
import time

from sqlalchemy.orm import Session

import parser
from core.db import SessionLocal
from models import AvitoRequest, RequestValues
from schemas import AvitoRequestCreate


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


def regular_parse(t: int):
    while True:
        db = SessionLocal()
        start_time = time.time()
        items = get_avito_requests(db)
        for item in items:
            create_request_value(db, item)
        db.close()
        finish_time = time.time()
        time_delta = finish_time - start_time
        time.sleep(t - time_delta)


def get_avito_requests(db: Session) -> list:
    request_values = list(db.query(AvitoRequest).all())
    return request_values


def get_request_values(db: Session, id: int, start: str | None, end: str | None) -> list:
    request_values = db.query(RequestValues).filter(RequestValues.avito_request_id == id)
    if start is not None:
        start_datetime = datetime.datetime.fromisoformat(start)
        request_values = request_values.filter(RequestValues.datetime >= start_datetime)
    if end is not None:
        end_datetime = datetime.datetime.fromisoformat(end)
        request_values = request_values.filter(RequestValues.datetime <= end_datetime)
    return request_values.all()
