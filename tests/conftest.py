import datetime

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from starlette.testclient import TestClient

from tracker import models
from tracker.app import app
from tracker.db import get_session
from tracker.models import Base
from tracker.schemas import AvitoQueryValueCreate, AvitoQueryCreate

SQLALCHEMY_DATABASE_URL = "sqlite:///tests/db.sqlite3"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    session = TestingSessionLocal()

    try:
        yield session
    finally:
        session.close()


@pytest.fixture
def client(session):
    # Dependency override
    def override_get_session():
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_session] = override_get_session
    yield TestClient(app)


@pytest.fixture
def avito_queries_list(session):
    avito_queries_list = []
    for i in range(10):
        avito_query_data = AvitoQueryCreate(query=f'query{i}', region=f'region{i}')
        avito_query_object = models.AvitoQuery(**avito_query_data.dict())
        avito_queries_list.append(avito_query_object)
        session.add(avito_query_object)
    session.commit()
    return avito_queries_list


@pytest.fixture
def add_avito_query_values(session):
    session.add(models.AvitoQueryValue(**AvitoQueryValueCreate(
        avito_query_id=1,
        timestamp=datetime.datetime(2022, 8, 13, 0, 0, 0, 0),
        value=1
    ).dict()))
    session.add(models.AvitoQueryValue(**AvitoQueryValueCreate(
        avito_query_id=2,
        timestamp=datetime.datetime(2022, 8, 13, 0, 0, 0, 0),
        value=1
    ).dict()))
    session.add(models.AvitoQueryValue(**AvitoQueryValueCreate(
        avito_query_id=1,
        timestamp=datetime.datetime(2020, 8, 13, 0, 0, 0, 0),
        value=1
    ).dict()))
    session.add(models.AvitoQueryValue(**AvitoQueryValueCreate(
        avito_query_id=1,
        timestamp=datetime.datetime(2023, 8, 13, 0, 0, 0, 0),
        value=1
    ).dict()))

    session.commit()


@pytest.fixture
def add_real_avito_queries(session):
    avito_query_data = AvitoQueryCreate(query=f'book', region='moskva')
    avito_query_object = models.AvitoQuery(**avito_query_data.dict())
    session.add(avito_query_object)
    session.commit()
