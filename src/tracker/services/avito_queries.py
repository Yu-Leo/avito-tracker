import datetime
from typing import List, Optional

from fastapi import Depends
from sqlalchemy.orm import Session

from tracker import models
from tracker.db import get_session
from tracker.schemas import AvitoQueryCreate, AvitoQueryValueCreate


class AvitoQueryService():
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def create(self, avito_query_data: AvitoQueryCreate) -> models.AvitoQuery:
        avito_query = models.AvitoQuery(**avito_query_data.dict())
        self.session.add(avito_query)
        self.session.commit()
        return avito_query

    def get_list(self) -> List[models.AvitoQuery]:
        return self.session.query(models.AvitoQuery).all()


class AvitoQueryValueService():
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def create(self, avito_query_value_data: AvitoQueryValueCreate) -> models.AvitoQueryValue:
        avito_query_value = models.AvitoQueryValue(**avito_query_value_data.dict())
        self.session.add(avito_query_value)
        self.session.commit()
        return avito_query_value

    def get_by_avito_query_id(self, avito_query_id: int,
                              start: Optional[str] = None,
                              end: Optional[str] = None) -> List[models.AvitoQueryValue]:

        avito_query_values = (
            self.session.query(models.AvitoQueryValue)
            .filter(models.AvitoQueryValue.avito_query_id == avito_query_id))
        if start:
            start_datetime = datetime.datetime.fromisoformat(start)
            avito_query_values = avito_query_values.filter(models.AvitoQueryValue.timestamp >= start_datetime)
        if end:
            end_datetime = datetime.datetime.fromisoformat(end)
            avito_query_values = avito_query_values.filter(models.AvitoQueryValue.timestamp <= end_datetime)
        return avito_query_values.all()
