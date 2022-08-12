import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from tracker.models import Base


@pytest.fixture()
def database_session():
    # Set up
    SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    Base.metadata.create_all(bind=engine)

    session = TestingSessionLocal()

    yield session  # Testing

    # Tear down
    session.close()
