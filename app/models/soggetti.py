from sqlalchemy import Boolean, Column, Integer, String, Date, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base
import enum

class SessoType(enum.Enum):
    # tolto per ora che rompe....
    M = "M"
    F = "F"

class Soggetto:    
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
    comune = Column(String(256), nullable=True)
    prov = Column(String(2), nullable=True)
    loc = Column(String(256), nullable=True)
    cap = Column(String(5), nullable=True)
    indirizzo = Column(String(256), nullable=True)
    civico = Column(String(50), nullable=True)  
    

class Recapito:
    email = Column(String(256), nullable=True)
    pec = Column(String(256), nullable=True)
    telefono = Column(String(256), nullable=True)
    cellulare = Column(String(256), nullable=True)
    fax = Column(String(256), nullable=True)


class Fisica(Soggetto, Recapito, Base):
    id_fisica = Column(Integer, primary_key=True, index=True)


class Giuridica(Recapito,Base):    
    
    id_giuridica = Column(Integer, primary_key=True, index=True)
    denominazione = Column(String(256), nullable=True)
    cf = Column(String(16), nullable=True)
    piva = Column(String(11), nullable=True)    
    comune = Column(String(256), nullable=True)
    prov = Column(String(2), nullable=True)
    loc = Column(String(256), nullable=True)
    cap = Column(String(5), nullable=True)
    indirizzo = Column(String(256), nullable=True)
    civico = Column(String(50), nullable=True)


class Tecnico(Soggetto, Recapito, Base):
    id_tecnico = Column(Integer, primary_key=True, index=True)
    denominazione = Column(String(256), nullable=True)
    sede_comune = Column(String(256), nullable=True)
    sede_prov = Column(String(2), nullable=True)
    sede_cap = Column(String(5), nullable=True)
    sede_indirizzo = Column(String(256), nullable=True)
    sede_civico = Column(String(50), nullable=True)
    albo = Column(String(256), nullable=True)
    albo_numero = Column(String(256), nullable=True)
    albo_prov = Column(String(256), nullable=True)

class Esecutore(Soggetto, Recapito, Base):
    id_esecutore = Column(Integer, primary_key=True, index=True)
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
    

class Condominio(Base):
    id_condominio = Column(Integer, primary_key=True, index=True)
    denominazione = Column(String(256), nullable=True)
    indirizzo = Column(String(256), nullable=True)
    cf = Column(String(16), nullable=True)
    piva = Column(String(11), nullable=True)
    

class Richiedenti(Base):
    id = Column(Integer, primary_key=True, index=True)
    id_istanza = Column(Integer, ForeignKey("sue.istanza.id_istanza"))    
    id_fisica = Column(Integer, ForeignKey("sue.fisica.id_fisica"))
    id_giuridica = Column(Integer, ForeignKey("sue.giuridica.id_giuridica"))    
    id_condominio = Column(Integer, ForeignKey("sue.condominio.id_condominio"))
    fisica_ruolo = Column(String(256), nullable=True)
    giuridica_ruolo = Column(String(256), nullable=True)
    id_pratica = Column(Integer, nullable=True)
    sostituito = Column(Boolean, nullable=True)

class Tecnici(Base):
    id = Column(Integer, primary_key=True, index=True)
    id_istanza= Column(Integer, ForeignKey("sue.istanza.id_istanza"))
    id_tecnico = Column(Integer, ForeignKey("sue.tecnico.id_tecnico"))
    tecnico_ruolo = Column(String(256), nullable=True)
    data_incarico = Column(Date, nullable=True) 
    id_pratica = Column(Integer, nullable=True)
    sostituito = Column(Boolean, nullable=True)

class Esecutori(Base):
    id = Column(Integer, primary_key=True, index=True)
    id_istanza = Column(Integer, ForeignKey("sue.istanza.id_istanza"))
    id_esecutore = Column(Integer, ForeignKey("sue.esecutore.id_esecutore"))
    id_pratica = Column(Integer, nullable=True)
    sostituito = Column(Boolean, nullable=True)
    
