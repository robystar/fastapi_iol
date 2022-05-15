from sqlalchemy import Boolean, Column, Integer, String, Date, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base

import enum

class SessoType(enum.Enum):
    # tolto per ora che rompe....
    M = "M"
    F = "F"

class Fisica:    
    app = Column(String(256), nullable=True)
    nome = Column(String(256), nullable=True)
    cognome = Column(String(256), nullable=True)
    cf = Column(String(16), nullable=True)
    piva = Column(String(11), nullable=True)  
    data_nato = Column(Date, nullable=True) 
    comune_nato = Column(String(256), nullable=True)
    prov_nato = Column(String(2), nullable=True)
    loc_nato = Column(String(256), nullable=True)
    codcat_nato = Column(String(4), nullable=True)
    cittadinanza = Column(String(256), nullable=True) # cittadinanza serve? in automatico?
    sesso = Column(String(1), nullable=True)
    
class Indirizzo:
    comune = Column(String(256), nullable=True)
    prov = Column(String(2), nullable=True)
    loc = Column(String(256), nullable=True)
    cap = Column(String(5), nullable=True)
    indirizzo = Column(String(256), nullable=True)
    civico = Column(String(50), nullable=True)  
    
class Giuridica: 
    denominazione = Column(String(256), nullable=True)
    cf = Column(String(16), nullable=True)
    piva = Column(String(11), nullable=True)  
      
class Recapito:
    email = Column(String(256), nullable=True)
    pec = Column(String(256), nullable=True)
    telefono = Column(String(256), nullable=True)
    cellulare = Column(String(256), nullable=True)
    fax = Column(String(256), nullable=True)


class Richiedente(Base, Fisica, Indirizzo, Recapito):         
    __tablename__ = 'richiedenti'
    __table_args__ = {'schema': 'sue'}
    
    giuridica_opt = Column(Integer)
    delegato_opt = Column(Integer)
    domicilio_opt = Column(Integer)
    
    ruolo = Column(String(256), nullable=True)
    id = Column(Integer, primary_key=True)
    id_istanza = Column(Integer, ForeignKey("sue.istanze.id_istanza"))   
    id_pratica = Column(Integer, nullable=True)    
    sostituito = Column(Boolean, nullable=True)

    istanza = relationship("Istanza", back_populates="richiedenti")
    domicilio = relationship("RichiedenteDomicilio", back_populates="richiedente")
    condominio = relationship("RichiedenteCondominio", back_populates="richiedente")


class RichiedenteGiuridica(Base,Giuridica,Indirizzo,Recapito):    
    __tablename__ = 'richiedenti_giuridica'
    __table_args__ = {'schema': 'sue'}
    
    id = Column(Integer, primary_key=True)
    id_richiedente = Column(Integer, ForeignKey("sue.richiedenti.id"))    
    richiedente = relationship("Richiedente", back_populates="giuridica")
    
class RichiedenteDomicilio(Base,Indirizzo):    
    __tablename__ = 'richiedenti_domicilio'
    __table_args__ = {'schema': 'sue'}
    
    id = Column(Integer, primary_key=True)
    id_richiedente = Column(Integer, ForeignKey("sue.richiedenti.id"))    
    richiedente = relationship("Richiedente", back_populates="domicilio")    
    
class RichiedenteCondominio(Base):    
    __tablename__ = 'richiedenti_condominio'
    __table_args__ = {'schema': 'sue'}
    
    id = Column(Integer, primary_key=True)
    id_richiedente = Column(Integer, ForeignKey("sue.richiedenti.id"))    
    denominazione = Column(String(256), nullable=True)
    cf = Column(String(16), nullable=True)
    piva = Column(String(11), nullable=True)    
    indirizzo = Column(String(256), nullable=True)
    richiedente = relationship("Richiedente", back_populates="condominio")
    
class Delegato(Base, Fisica, Indirizzo, Recapito):         
    __tablename__ = 'delegati'
    __table_args__ = {'schema': 'sue'}
    id = Column(Integer, primary_key=True)   
    id_istanza = Column(Integer, ForeignKey("sue.istanze.id_istanza"))   
    istanza = relationship("Istanza", back_populates="delegato")

class Tecnico(Base, Fisica, Indirizzo, Recapito):         
    __tablename__ = 'tecnici'
    __table_args__ = {'schema': 'sue'}
    
    denominazione = Column(String(256), nullable=True)
    sede_comune = Column(String(256), nullable=True)
    sede_prov = Column(String(2), nullable=True)
    sede_cap = Column(String(5), nullable=True)
    sede_indirizzo = Column(String(256), nullable=True)
    sede_civico = Column(String(50), nullable=True)
    albo = Column(String(256), nullable=True)
    albo_numero = Column(String(256), nullable=True)
    albo_prov = Column(String(256), nullable=True)

    ruolo = Column(String(256), nullable=True)
    data_incarico = Column(Date, nullable=True) 
    
    id = Column(Integer, primary_key=True)
    id_istanza = Column(Integer, ForeignKey("sue.istanze.id_istanza"))   
    id_pratica = Column(Integer, nullable=True)    
    sostituito = Column(Boolean, nullable=True)
    istanza = relationship("Istanza", back_populates="tecnici")


class Esecutore(Base, Fisica, Indirizzo, Recapito):         
    __tablename__ = 'esecutori'
    __table_args__ = {'schema': 'sue'}
    
    denominazione = Column(String(256), nullable=True)
    sede_comune = Column(String(256), nullable=True)
    sede_prov = Column(String(2), nullable=True)
    sede_cap = Column(String(5), nullable=True)
    sede_indirizzo = Column(String(256), nullable=True)
    sede_civico = Column(String(50), nullable=True)
    cciaa = Column(String(256), nullable=True)
    cciaa_numero = Column(String(256), nullable=True)
    inps = Column(String(256), nullable=True)
    inail = Column(String(256), nullable=True)
    cedile = Column(String(256), nullable=True)
    cedile_prov = Column(String(256), nullable=True)    

    id = Column(Integer, primary_key=True)
    id_istanza = Column(Integer, ForeignKey("sue.istanze.id_istanza"))   
    id_pratica = Column(Integer, nullable=True)
    sostituito = Column(Boolean, nullable=True)
    istanza = relationship("Istanza", back_populates="esecutori")