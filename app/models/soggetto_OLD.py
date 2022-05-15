from sqlalchemy import Boolean, Column, Integer, String, Date, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base
import enum

class SessoEnum(enum.Enum):
    M = "M"
    F = "F"

class Fisica(Base):
    __table_args__ = {'schema': 'sue'}
    
    fisica_id = Column(Integer, primary_key=True, index=True)
    fisica_nome = Column(String(256), nullable=True)
    fisica_cognome = Column(String(256), nullable=True)
    fisica_comune_nato = Column(String(256), nullable=True)
    fisica_prov_nato = Column(String(2), nullable=True)
    fisica_loc_nato = Column(String(256), nullable=True)
    fisica_codcat_nato = Column(String(4), nullable=True)
    fisica_data_nato = Column(Date, nullable=True)
    fisica_cf = Column(String(16), nullable=True)
    fisica_sesso = Column(Enum(SessoEnum), nullable=True)
    fisica_comune = Column(String(256), nullable=True)
    fisica_prov = Column(String(2), nullable=True)
    fisica_loc = Column(String(256), nullable=True)
    fisica_cap = Column(String(5), nullable=True)
    fisica_via = Column(String(256), nullable=True)
    fisica_civico = Column(String(50), nullable=True)  
    fisica_giuridica = relationship("Giuridica", secondary="fisica_giuridica",back_populates="giuridica_fisica")
    #indirizzo = relationship("Indirizzo")
    #domicilio = relationship("Indirizzo")
    #recapito = relationship("Recapito")
    
class Giuridica(Base):    
    __table_args__ = {'schema': 'sue'}
    
    giuridica_id = Column(Integer, primary_key=True, index=True)
    giuridica_denominazione = Column(String(256), nullable=True)
    giuridica_cf = Column(String(16), nullable=True)
    giuridica_piva = Column(String(11), nullable=True)    
    giuridica_comune = Column(String(256), nullable=True)
    giuridica_prov = Column(String(2), nullable=True)
    giuridica_loc = Column(String(256), nullable=True)
    giuridica_cap = Column(String(5), nullable=True)
    giuridica_via = Column(String(256), nullable=True)
    giuridica_civico = Column(String(50), nullable=True)
    giuridica_fisica = relationship("fisica", secondary="fisica_giuridica",back_populates="fisica_giuridica")

class Fisica_Giuridica(Base):
    __table_args__ = {'schema': 'sue'}
    
    fisica_id = Column(Integer, ForeignKey("sue.fisica.fisica_id"), primary_key=True)
    giuridica_id = Column(Integer, ForeignKey("sue.giuridica.giuridica_id"), primary_key=True)
    fisica_ruolo = Column(String(256), nullable=True)
    
class Recapito(Base):
    __table_args__ = {'schema': 'sue'}
    recapito_id = Column(Integer, primary_key=True, index=True)
    recapito_email = Column(String(256), nullable=True)
    recapito_pec = Column(String(256), nullable=True)
    recapito_telefono = Column(String(256), nullable=True)
    recapito_cellulare = Column(String(256), nullable=True)
    recapito_fax = Column(String(256), nullable=True)

class Indirizzo(Base):
    __table_args__ = {'schema': 'sue'}
    
    indirizzo_id = Column(Integer, primary_key=True, index=True)
    indirizzo_comune = Column(String(256), nullable=True)
    indirizzo_prov = Column(String(2), nullable=True)
    indirizzo_loc = Column(String(256), nullable=True)
    indirizzo_cap = Column(String(5), nullable=True)
    indirizzo_via = Column(String(256), nullable=True)
    indirizzo_civico = Column(String(50), nullable=True)
    fisica_id = Column(Integer, ForeignKey("sue.fisica.fisica_id"))
    giuridica_id = Column(Integer, ForeignKey("sue.giuridica.giuridica_id"))
    
