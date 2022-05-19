from typing import Optional
import datetime

from pydantic import BaseModel

# Shared properties
class Fisica(BaseModel): 
    app : Optional[str] = None
    nome : str
    cognome : str
    cf : str
    piva : Optional[str] = None
    data_nato: datetime.date = None
    comune_nato : Optional[str] = None
    prov_nato : Optional[str] = None
    codcat_nato : Optional[str] = None
    cittadinanza : Optional[str] = None 
    sesso : Optional[str]

  
class Indirizzo(BaseModel):
    comune : Optional[str] = None
    prov : Optional[str] = None
    loc : Optional[str] = None
    cap : Optional[str] = None
    indirizzo : Optional[str] = None
    civico : Optional[str] = None

      
class Recapito(BaseModel):
    email : Optional[str] = None
    pec : Optional[str] = None
    telefono : Optional[str] = None
    cellulare : Optional[str] = None
    fax : Optional[str] = None    










