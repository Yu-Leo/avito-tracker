from sqlalchemy import Column, String, Integer, ForeignKey, DateTime

from core.db import Base


class AvitoRequest(Base):
    __tablename__ = 'avito_requests'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    text = Column(String(255))
    region = Column(String(255))


class RequestValues(Base):
    __tablename__ = 'request_values'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    avito_request_id = Column(Integer, ForeignKey("avito_requests.id"))
    timestamp = Column(DateTime)
    value = Column(Integer)
