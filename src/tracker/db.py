"""
File with database settings
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from tracker.settings import settings

SQLALCHEMY_DATABASE_URL = \
    f'postgresql://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}/{settings.DB_NAME}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session() -> Session:
    session = Session()
    try:
        yield session
    finally:
        session.close()
