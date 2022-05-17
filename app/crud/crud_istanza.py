from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.istanza import Istanza
from app.schemas.istanza import IstanzaCreate, IstanzaUpdate, IstanzaBase


class CRUDIstanza(CRUDBase[Istanza, IstanzaCreate, IstanzaUpdate]):

    def get(self, db: Session, id: int) -> IstanzaCreate:
            return db.query(self.model).filter(self.model.id_istanza == id).first()
        
        
    def getItems(self, db: Session, id: int) -> IstanzaBase:
            return db.query(self.model).filter(self.model.id_istanza == id).first()["items"]
    
    def create_with_owner(
        self, db: Session, *, obj_in: IstanzaCreate, user_id: str
    ) -> Istanza:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, user_id=user_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_owner(
        self, db: Session, *, user_id: str, skip: int = 0, limit: int = 100
    ) -> List[Istanza]:
        return (
            db.query(self.model)
            .filter(Istanza.user_id == user_id)
            .offset(skip)
            .limit(limit)
            .all()
        )


istanza = CRUDIstanza(Istanza)
