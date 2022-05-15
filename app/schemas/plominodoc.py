import json
from typing import Optional, Dict

from pydantic import BaseModel


# Shared properties
class Plominodoc(BaseModel):
    id_plomino: str
    items: Dict
    
    class Config:
        orm_mode = True
