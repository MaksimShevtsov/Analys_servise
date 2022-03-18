from fastapi import APIRouter, Depends
from repositories.users import UserRepository
from .depends import get_user_repository


router = APIRouter()


@router.get("/")
async def read_users(
        users: UserRepository = Depends(get_user_repository),
        limit: int = 100,
        skip: int = 100):
    return {}
