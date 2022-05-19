from __future__ import annotations
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB, ARRAY

from app.db.base_class import Base


class Istanza(Base):
    __tablename__ = 'istanze'
    __table_args__ = {'schema': 'sue'}
    
    id_istanza = Column(Integer, primary_key=True, index=True)
    id_pratica = Column(Integer, nullable=True, index=True)
    
    anno = Column(Integer, nullable=False)
    data_creazione = Column(Date, nullable=False)
    data_presentazione = Column(Date, nullable=True)
    
    numero_protocollo = Column(Integer, nullable=True)
    data_protocollo = Column(Date, nullable=True)
    numero_pratica = Column(String(256), nullable=True)

    tipo = Column(String(256), nullable=False)
    sportello = Column(String(256), nullable=False)

    user_id = Column(String(256))
    owners = Column(ARRAY(String))
    items = Column(JSONB)
    
    richiedenti = relationship("Richiedente", back_populates="istanza")
    tecnici = relationship("Tecnico", back_populates="istanza")
    esecutori = relationship("Esecutore", back_populates="istanza")
    delegato = relationship("Delegato", back_populates="istanza")
    
    civici = relationship("Civico", back_populates="istanza")
    mappali = relationship("Mappale", back_populates="istanza")
    uiu = relationship("Uiu", back_populates="istanza")
   
    
    