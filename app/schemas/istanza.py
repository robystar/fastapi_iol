from pydantic import BaseModel, HttpUrl

from typing import Sequence


class IstanzaBase(BaseModel):
    label: str
    source: str
    url: HttpUrl


class IstanzaCreate(IstanzaBase):
    label: str
    source: str
    url: HttpUrl
    owner_id: int


class IstanzaUpdate(IstanzaBase):
    id: int


class IstanzaUpdateRestricted(BaseModel):
    id: int
    label: str


# Properties shared by models stored in DB
class IstanzaInDBBase(IstanzaBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Istanza(IstanzaInDBBase):
    pass


# Properties properties stored in DB
class IstanzaInDB(IstanzaInDBBase):
    pass


class IstanzaSearchResults(BaseModel):
    results: Sequence[Istanza]
