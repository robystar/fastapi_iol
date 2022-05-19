from typing import Union

from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from app.crud.base import CRUDBase
from app.models.soggetto import Richiedente
from app.schemas.richiedente import RichiedenteCreate, RichiedenteUpdate


class CRUDRichiedente(CRUDBase[Richiedente, RichiedenteCreate, RichiedenteUpdate]):

    pass

richiedente = CRUDRichiedente(Richiedente)
