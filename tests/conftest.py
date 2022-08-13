import datetime

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from tracker import models
from tracker.models import Base
from tracker.schemas import AvitoQueryValueCreate, AvitoQueryCreate


@pytest.fixture
def create_database():
    # Set up
    SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )
    TestingSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    Base.metadata.create_all(bind=engine)

    return TestingSession


@pytest.fixture
def database_session(create_database):
    TestingSession = create_database

    session = TestingSession()

    try:
        yield session  # Run test wit session
    finally:  # Tear down
        session.close()


@pytest.fixture
def avito_queries_list(database_session):
    avito_queries_list = []
    for i in range(10):
        avito_query_data = AvitoQueryCreate(query=f'query{i}', region=f'region{i}')
        avito_query_object = models.AvitoQuery(**avito_query_data.dict())
        avito_queries_list.append(avito_query_object)
        database_session.add(avito_query_object)
    database_session.commit()
    return avito_queries_list


@pytest.fixture
def avito_query_values_list(database_session):
    database_session.add(models.AvitoQueryValue(**AvitoQueryValueCreate(
        avito_query_id=1,
        timestamp=datetime.datetime(2022, 8, 13, 0, 0, 0, 0),
        value=1
    ).dict()))
    database_session.add(models.AvitoQueryValue(**AvitoQueryValueCreate(
        avito_query_id=2,
        timestamp=datetime.datetime(2022, 8, 13, 0, 0, 0, 0),
        value=1
    ).dict()))
    database_session.add(models.AvitoQueryValue(**AvitoQueryValueCreate(
        avito_query_id=1,
        timestamp=datetime.datetime(2020, 8, 13, 0, 0, 0, 0),
        value=1
    ).dict()))
    database_session.add(models.AvitoQueryValue(**AvitoQueryValueCreate(
        avito_query_id=1,
        timestamp=datetime.datetime(2023, 8, 13, 0, 0, 0, 0),
        value=1
    ).dict()))

    database_session.commit()
