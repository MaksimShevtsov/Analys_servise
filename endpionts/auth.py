from fastapi import APIRouter, HTTPException, status, Depends, Request
from models.token import Token, LoginIn
from repositories.users import UserRepository
from core.security import verify_password, create_access_token
from .depends import get_user_repository
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory='templates')
link = "accounts/login.html"


@router.get("/", response_class=HTMLResponse)
async def login_get(request: Request,
                    users: UserRepository = Depends(get_user_repository)):
    return templates.TemplateResponse(link, context={"request": request})


@router.post("/", response_model=Token)
async def login(login: LoginIn, users: UserRepository = Depends(get_user_repository)):
    user = await users.get_by_email(login.email)
    if user is None or not verify_password(login.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or paswword")
    return Token(
        access_token=create_access_token({"sub": user.email}),
        token_type="Bearer"
    )
