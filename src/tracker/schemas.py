import datetime

from pydantic import BaseModel


class AvitoQueryBase(BaseModel):
    query: str
    region: str

    class Config:
        orm_mode = True


class AvitoQueryCreate(AvitoQueryBase):
    pass


def convert_datetime_to_iso_8601_without_microseconds(dt: datetime.datetime) -> str:
    return dt.strftime('%Y-%m-%dT%H:%M:%S')


class AvitoQueryValueBase(BaseModel):
    timestamp: datetime.datetime
    value: str

    class Config:
        orm_mode = True

        json_encoders = {
            datetime.datetime: convert_datetime_to_iso_8601_without_microseconds
        }


class AvitoQueryValueCreate(AvitoQueryValueBase):
    avito_query_id: int
