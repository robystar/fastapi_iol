from pydantic import BaseModel, HttpUrl

from typing import Sequence


class RecipeBase(BaseModel):
    label: str
    source: str
    url: str


class RecipeCreate(RecipeBase):
    submitter_id: str


class RecipeUpdate(RecipeBase):
    id: int


class RecipeUpdateRestricted(BaseModel):
    id: int
    label: str


# Properties shared by models stored in DB
class RecipeInDBBase(RecipeBase):
    id: int
    submitter_id: str

    class Config:
        orm_mode = True


# Properties to return to client
class Recipe(RecipeInDBBase):
    pass


# Properties properties stored in DB
class RecipeInDB(RecipeInDBBase):
    pass


class RecipeSearchResults(BaseModel):
    results: Sequence[Recipe]
