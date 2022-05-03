from fastapi import APIRouter, HTTPException, status, Depends, Request
from repositories.users import UserRepository
from api.endpoints.depends import get_user_repository, get_current_user
from fastapi.templating import Jinja2Templates
from models.user import User

router = APIRouter()
templates = Jinja2Templates(directory='templates')


@router.get("/settings")  # new
async def settings(request: Request,
                   users: UserRepository = Depends(get_user_repository),
                   current_user: User = Depends(get_current_user)):
    return templates.TemplateResponse("home/settings.html", {"request": request,
                                                             "current_user": current_user.username})
