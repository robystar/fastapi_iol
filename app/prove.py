from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, Text, Boolean
from sqlalchemy.orm import declarative_base, relationship, Session
from geoalchemy2 import Geometry
from sqlalchemy.dialects.postgresql import JSONB
import enum

import pathlib, sys

from app.models.soggetti import Giuridica
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

#from app.db.base_class import Base  # noqa

# Make the engine
engine = create_engine("postgresql://postgres:postgres@localhost:5444/provaiol", future=True, echo=False)

Base = declarative_base()

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

class Istanza(Base):
    __tablename__ = 'istanze'
    __table_args__ = {'schema': 'sue'}
    
    id_istanza = Column(Integer, primary_key=True, index=True)
    id_pratica = Column(Integer, index=True)
    
    anno = Column(Integer, nullable=False)
    data_creazione = Column(Date, nullable=False)
    data_presentazione = Column(Date, nullable=True)
    
    tipo = Column(String(256), nullable=False)
    sportello = Column(String(256), nullable=False)

    user_id = Column(String(256))
    #delegato_id = Column(Integer, ForeignKey("sue.fisica.id_fisica"))
    items = Column(JSONB)
    
    richiedenti = relationship("Richiedente", back_populates="istanza")
    tecnici = relationship("Tecnico", back_populates="istanza")
    esecutori = relationship("Esecutore", back_populates="istanza")
    delegato = relationship("Delegato", back_populates="istanza")


class Richiedente(Base, Fisica, Indirizzo, Recapito):         
    __tablename__ = 'richiedenti'
    __table_args__ = {'schema': 'sue'}
    
    id = Column(Integer, primary_key=True)
    id_istanza = Column(Integer, ForeignKey("sue.istanze.id_istanza"))   
    id_pratica = Column(Integer, nullable=True)    
    ruolo = Column(String(256), nullable=True)
    giuridica_opt = Column(Integer)
    delegato_opt = Column(Integer)
    domicilio_opt = Column(Integer)
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

    id = Column(Integer, primary_key=True)
    id_istanza = Column(Integer, ForeignKey("sue.istanze.id_istanza"))   
    id_pratica = Column(Integer, nullable=True)
    ruolo = Column(String(256), nullable=True)
    data_incarico = Column(Date, nullable=True) 
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


    
    
    
    
    
    
    
    
    
    
    
    
    

Base.metadata.create_all(engine)
exit() 


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    projects = relationship('Project', secondary='project_users', back_populates='users')


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    users = relationship('User', secondary='project_users', back_populates='projects')


class ProjectUser(Base):
    __tablename__ = "project_users"

    id = Column(Integer, primary_key=True)
    notes = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    project_id = Column(Integer, ForeignKey('projects.id'))


class ItemDetail(Base):
    __tablename__ = 'ItemDetail'
    id = Column(Integer, primary_key=True, index=True)
    itemId = Column(Integer, ForeignKey('Item.id'))
    detailId = Column(Integer, ForeignKey('Detail.id'))
    endDate = Column(Date)

class Item(Base):
    __tablename__ = 'Item'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(Text)
    details = relationship('Detail', secondary='ItemDetail', back_populates='items')

class Detail(Base):
    __tablename__ = 'Detail'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    value = Column(String)
    items = relationship('Item', secondary='ItemDetail', back_populates='details')



#exit() 

# Test it
with Session(bind=engine) as session:

    # add users
    usr1 = User(name="bob")
    session.add(usr1)

    usr2 = User(name="alice")
    session.add(usr2)

    session.commit()

    # add projects
    prj1 = Project(name="Project 1")
    session.add(prj1)

    prj2 = Project(name="Project 2")
    session.add(prj2)

    session.commit()

    # map users to projects
    prj1.users = [usr1, usr2]
    prj2.users = [usr2]

    session.commit()


with Session(bind=engine) as session:

    print(session.query(User).where(User.id == 1).one().projects)
    print(session.query(Project).where(Project.id == 1).one().users)
















