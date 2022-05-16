from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from geoalchemy2 import Geometry

from app.db.base_class import Base


class Recipe(Base):
    __tablename__ = 'ricette'
    id = Column(Integer, primary_key=True, index=True)
    label = Column(String(256), nullable=False)
    url = Column(String(256), index=True, nullable=True)
    source = Column(String(256), nullable=True)
    submitter_id = Column(String(80), ForeignKey("users.user_id"), nullable=True)  # 3
    submitter = relationship("User", back_populates="recipes")  # 4

class Civico(Base):    
    __tablename__ = 'civici'
    __table_args__ = {'schema': 'sue'}
    
    id = Column(Integer, primary_key=True, index=True)
    id_istanza = Column(Integer, ForeignKey("sue.istanze.id_istanza"))    
    id_via = Column(Integer, nullable=True)
    via = Column(String(256), nullable=True)
    civico = Column(String(50), nullable=True)
    note = Column(String(256), nullable=True)
    geom = Column(Geometry(geometry_type='POINT', srid=4326, spatial_index=True))
    istanza = relationship("Istanza", back_populates="civici")   
    
    
class Mappale(Base):    
    __tablename__ = 'mappali'
    __table_args__ = {'schema': 'sue'}
    
    id = Column(Integer, primary_key=True, index=True)
    id_istanza = Column(Integer, ForeignKey("sue.istanze.id_istanza"))    
    sezione = Column(String(30), nullable=True)
    foglio = Column(String(8), nullable=True)
    mappale = Column(String(8), nullable=True)
    note = Column(String(256), nullable=True)
    geom = Column(Geometry(geometry_type='POLYGON', srid=4326, spatial_index=True))
    istanza = relationship("Istanza", back_populates="mappali")

class Uiu(Base):    
    __tablename__ = 'uiu'
    __table_args__ = {'schema': 'sue'}
    
    id = Column(Integer, primary_key=True, index=True)
    id_istanza = Column(Integer, ForeignKey("sue.istanze.id_istanza"))    
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
    istanza = relationship("Istanza", back_populates="uiu")   