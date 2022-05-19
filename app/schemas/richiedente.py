from typing import Optional, List
import datetime
from pydantic import BaseModel

from .soggetto import Fisica, Indirizzo, Recapito

class Giuridica(BaseModel):
    denominazione: str
    cf: Optional[str]
    piva: Optional[str]
    
    
    class Config:
        orm_mode = True


# Shared properties
class RichiedenteBase(Fisica, Indirizzo, Recapito):
    ruolo:  Optional[str]

    giuridica_opt: Optional[int]
    delegato_opt:  Optional[int]
    domicilio_opt:  Optional[int]
    
    id_istanza: int   
    id_pratica: Optional[int]    
    sostituito: Optional[bool]
    principale: Optional[bool]
    
    giuridica: Optional[Giuridica]


# Properties to receive on Richiedente creation
class RichiedenteCreate(RichiedenteBase):
    
    
    
    pass

# Properties to receive on Richiedente update
class RichiedenteUpdate(RichiedenteBase):
    pass


# Properties shared by models stored in DB
class RichiedenteInDBBase(RichiedenteBase):
    id: int
    data_nato: Optional[datetime.date]

    class Config:
        orm_mode = True


# Properties to return to client
class Richiedente(RichiedenteInDBBase):
    pass


# Properties properties stored in DB
class RichiedenteInDB(RichiedenteInDBBase):
    pass
