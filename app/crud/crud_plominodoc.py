from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.plominodoc import Plominodoc
from app.schemas.plominodoc import Plominodoc as PlominodocSchema


class CRUDPlominodoc(CRUDBase[Plominodoc, PlominodocSchema, PlominodocSchema]):
    def create(
        self, db: Session, *, obj_in: PlominodocSchema
    ) -> Plominodoc:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


plominodoc = CRUDPlominodoc(Plominodoc)
