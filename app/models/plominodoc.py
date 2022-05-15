from __future__ import annotations
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB

from app.db.base_class import Base


class Plominodoc(Base):

    id_istanza = Column(Integer, primary_key=True, index=True)
    id_plomino = Column(String(80), index=True)
    items = Column(JSONB)
    
    #owner = relationship("User", back_populates="istanza")

