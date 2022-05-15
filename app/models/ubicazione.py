from sqlalchemy import Boolean, Column, Integer, String, Date, Enum, ForeignKey, Float
from sqlalchemy.orm import relationship
from geoalchemy2 import Geometry
from app.db.base_class import Base

 
class Civici(Base):    
    id = Column(Integer, primary_key=True, index=True)
    id_istanza = Column(Integer, ForeignKey("sue.istanza.id_istanza"))    
    id_via = Column(Integer, nullable=True)
    via = Column(String(256), nullable=True)
    civico = Column(String(50), nullable=True)
    note = Column(String(256), nullable=True)
    geom = Column(Geometry(geometry_type='POINT', srid=4326, spatial_index=True))
    
class Nct(Base):    
    id = Column(Integer, primary_key=True, index=True)
    id_istanza = Column(Integer, ForeignKey("sue.istanza.id_istanza"))    
    sezione = Column(String(30), nullable=True)
    foglio = Column(String(8), nullable=True)
    mappale = Column(String(8), nullable=True)
    note = Column(String(256), nullable=True)
    geom = Column(Geometry(geometry_type='POLYGON', srid=4326, spatial_index=True))
    
class Uiu(Base):    
    id = Column(Integer, primary_key=True, index=True)
    id_istanza = Column(Integer, ForeignKey("sue.istanza.id_istanza"))    
    id_civico = Column(Integer,nullable=True)    
    sezione = Column(String(30), nullable=True)
    foglio = Column(String(80), nullable=True)
    mappale = Column(String(80), nullable=True)
    sub = Column(String(80), nullable=True)
    interno = Column(String(80), nullable=True)
    scala = Column(String(80), nullable=True)
    piano = Column(String(80), nullable=True)
    vani = Column(String(80), nullable=True)
    supeficie = Column(Float, nullable=True)
    destuso = Column(String(80), nullable=True)
    note = Column(String(256), nullable=True)
    