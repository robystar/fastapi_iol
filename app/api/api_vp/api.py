from fastapi import APIRouter

from app.api.api_vp.endpoints import istanze, login, users, utils, richiedenti, tecnici, recipe

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["Utenti"])
api_router.include_router(recipe.router, prefix="/ricette", tags=["Ricette"])

api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
api_router.include_router(istanze.router, prefix="/sue/istanze", tags=["SUE"])
api_router.include_router(richiedenti.router, prefix="/sue/richiedenti", tags=["Richiedenti"])
api_router.include_router(tecnici.router, prefix="/sue/tecnici", tags=["Tecnici"])
