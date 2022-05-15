from __future__ import annotations
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB

from app.db.base_class import Base


class Istanza(Base):

    id_istanza = Column(Integer, primary_key=True, index=True)
    id_pratica = Column(Integer, index=True)
    
    anno = Column(Integer, nullable=False)
    data_creazione = Column(Date, nullable=False)
    data_presentazione = Column(Date, nullable=True)
    
    tipo = Column(String(256), nullable=False)
    sportello = Column(String(256), nullable=False)

    owner_id = Column(String(256))
    #delegato_id = Column(Integer, ForeignKey("sue.fisica.id_fisica"))
    
    items = Column(JSONB)

