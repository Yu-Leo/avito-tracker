"""
File with application settings
"""
import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str = 'localhost'
    DB_PORT: int = 5432

    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

    SERVER_HOST: str = 'localhost'
    SERVER_PORT: int = 8000

    REQUESTS_PERIOD: int = 60 * 60  # Value in seconds

    class Config:
        root_dir: str = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
        env_file = os.path.join(root_dir, '.env')
        env_file_encoding = 'utf-8'


settings = Settings()
