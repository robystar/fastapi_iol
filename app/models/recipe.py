from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Recipe(Base):
    __tablename__ = 'ricette'
    id = Column(Integer, primary_key=True, index=True)
    label = Column(String(256), nullable=False)
    url = Column(String(256), index=True, nullable=True)
    source = Column(String(256), nullable=True)
    submitter_id = Column(String(80), ForeignKey("users.user_id"), nullable=True)  # 3
    submitter = relationship("User", back_populates="recipes")  # 4

