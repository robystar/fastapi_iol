from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, Text, Boolean
from sqlalchemy.orm import declarative_base, relationship, Session
from geoalchemy2 import Geometry
from sqlalchemy.dialects.postgresql import JSONB
import enum

import pathlib, sys

sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

#from app.db.base_class import Base  # noqa

# Make the engine
engine = create_engine("postgresql://postgres:postgres@localhost:5444/provaiol", future=True, echo=False)

from app.db.base_class import Base

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
















