from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Istanza])
def read_all(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve istanze.
    """
    if crud.user.is_superuser(current_user):
        istanze = crud.istanza.get_multi(db, skip=skip, limit=limit)
    else:
        istanze = crud.istanza.get_multi_by_owner(
            db=db, user_id=current_user.id, skip=skip, limit=limit
        )
    return istanze


@router.post("/", response_model=schemas.Istanza)
def create(
    *,
    db: Session = Depends(deps.get_db),
    istanza_in: schemas.IstanzaCreate,
) -> Any:
    istanza = crud.istanza.create(db=db, obj_in=istanza_in)
    return istanza


@router.put("/{id}", response_model=schemas.Istanza)
def update(
    *,
    db: Session = Depends(deps.get_db),
    id_istanza: int,
    istanza_in: schemas.IstanzaUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update an istanza.
    """
    istanza = crud.istanza.get(db=db, id=id)
    if not istanza:
        raise HTTPException(status_code=404, detail="Istanza not found")
    if not crud.user.is_superuser(current_user) and (istanza.user_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    istanza = crud.istanza.update(db=db, db_obj=istanza, obj_in=istanza_in)
    return istanza


@router.get("/{id}", response_model=schemas.Istanza)
def read_one(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get istanza by ID.
    """
    istanza = crud.istanza.get(db=db, id=id)
    if not istanza:
        raise HTTPException(status_code=404, detail="Istanza not found")
    if not crud.user.is_superuser(current_user) and (istanza.user_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return istanza


@router.delete("/{id}", response_model=schemas.Istanza)
def delete(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an istanza.
    """
    istanza = crud.istanza.get(db=db, id=id)
    if not istanza:
        raise HTTPException(status_code=404, detail="Istanza not found")
    if not crud.user.is_superuser(current_user) and (istanza.user_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    istanza = crud.istanza.remove(db=db, id=id)
    return istanza
