"""
File with ORM (SQLAlchemy) models
"""
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class AvitoQuery(Base):
    __tablename__ = 'avito_queries'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    query = Column(String(255))
    region = Column(String(255))


class AvitoQueryValue(Base):
    __tablename__ = 'avito_query_values'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    avito_query_id = Column(Integer, ForeignKey("avito_queries.id"))
    timestamp = Column(DateTime)
    value = Column(Integer)
