"""
File with application settings
"""
import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    SERVER_HOST: str = '127.0.0.1'
    SERVER_PORT: int = 8000

    REQUESTS_PERIOD: int = 60 * 60  # Value in seconds

    class Config:
        root_dir: str = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
        env_file = os.path.join(root_dir, '.env')
        env_file_encoding = 'utf-8'


settings = Settings()
