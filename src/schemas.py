import datetime

from pydantic import BaseModel


class AvitoRequestBase(BaseModel):
    text: str
    region: str

    class Config:
        orm_mode = True


class AvitoRequestCreate(AvitoRequestBase):
    pass


def convert_datetime_to_iso_8601_without_microseconds(dt: datetime.datetime) -> str:
    return dt.strftime('%Y-%m-%dT%H:%M:%S')


class RequestValuesBase(BaseModel):
    timestamp: datetime.datetime
    value: str

    class Config:
        orm_mode = True

        json_encoders = {
            datetime.datetime: convert_datetime_to_iso_8601_without_microseconds
        }
