from sqlalchemy import Column, String, Integer

from core.db import Base


class AvitoRequest(Base):
    __tablename__ = 'avito_requests'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    text = Column(String(255))
    region = Column(String(255))
