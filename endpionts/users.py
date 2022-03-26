from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, Request,  Form
from repositories.users import UserRepository
from models.users import User, UserIn
from .depends import get_user_repository, get_current_user
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter()
templates = Jinja2Templates(directory='templates')

link = "accounts/register.html"


@router.get("/", response_model=List[User], response_class=HTMLResponse)
async def read_users(request: Request,
                     users: UserRepository = Depends(get_user_repository),
                     limit: int = 100,
                     skip: int = 0, ):
    await users.get_all(limit=limit, skip=skip)
    return templates.TemplateResponse(link, context={"request": request})


@router.post("/", response_model=User)
async def create_user(user: UserIn = Depends(UserIn.as_form),
                      users: UserRepository = Depends(get_user_repository)):
    return await users.create(u=user)


@router.patch("/", response_model=User)
async def update_user(
        request: Request,
        id: int,
        user: UserIn,
        users: UserRepository = Depends(get_user_repository),
        current_user: User = Depends(get_current_user)):
    old_user = await users.get_by_id(id=id)
    if old_user is None or old_user.email != current_user.email:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found user")
    await users.update(id=id, u=user)
    return templates.TemplateResponse(link, context={"request": request})
