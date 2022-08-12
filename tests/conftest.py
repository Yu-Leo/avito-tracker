import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from tracker.models import Base


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
