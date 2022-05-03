from .endpoints import users, login, integrations
from fastapi import APIRouter


api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(login.router, prefix="/login", tags=["login"])
api_router.include_router(integrations.router, prefix="/integrations", tags=["integrations"])
