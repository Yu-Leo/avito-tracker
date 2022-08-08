from pydantic import BaseModel


class AvitoRequestBase(BaseModel):
    text: str
    region: str

    class Config:
        orm_mode = True


class AvitoRequestCreate(AvitoRequestBase):
    pass
