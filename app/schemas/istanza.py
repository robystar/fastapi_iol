import datetime
from lib2to3.pgen2.token import OP
from pydantic import BaseModel, HttpUrl

from typing import Sequence, Optional, Dict


class IstanzaBase(BaseModel):
    items: Dict

class IstanzaCreate(IstanzaBase):
    id_istanza: int
    user_id: str
    anno: int
    data_creazione: Optional[datetime.datetime]
    sportello: str
    tipo: str
    
class IstanzaUpdate(IstanzaBase):
    id_istanza: int


class IstanzaUpdateRestricted(BaseModel):
    id_istanza: int
    
# Properties shared by models stored in DB
class IstanzaInDBBase(IstanzaBase):
    id_istanza: int
    user_id: str

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
