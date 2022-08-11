from pydantic import BaseSettings


class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    SERVER_HOST: str = '127.0.0.1'
    SERVER_PORT: int = 8000

    REQUESTS_PERIOD: int = 10  # In seconds

    class Config:
        env_file = '../../.env'
        env_file_encoding = 'utf-8'


settings = Settings()
