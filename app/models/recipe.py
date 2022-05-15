from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.models.user import User


class Recipe(Base):
    __table_args__ = {'schema': 'ricette'}
    id = Column(Integer, primary_key=True, index=True)
    label = Column(String(256), nullable=False)
    url = Column(String(256), index=True, nullable=True)
    source = Column(String(256), nullable=True)
    owner_id = Column(Integer, ForeignKey("utenti.user.id"))


