from sqlalchemy.ext.declarative import as_declarative, declared_attr
from app.core.config import settings

@as_declarative()
class Base:
    __name__: str
    __table_args__ = {'schema': settings.APP_SCHEMA}
    
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
    