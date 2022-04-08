from fastapi import APIRouter, HTTPException, status, Depends, Response
from models.token import Token
from repositories.users import UserRepository
from core.security import verify_password, create_access_token
from .depends import get_user_repository
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2PasswordRequestForm
from api.utils import OAuth2PasswordBearerWithCookie

router = APIRouter()

templates = Jinja2Templates(directory='templates')

oauth2_scheme = OAuth2PasswordBearerWithCookie(tokenUrl="/login/token")


@router.post("/token", response_model=Token)
async def login_for_access(response: Response,
                           login: OAuth2PasswordRequestForm = Depends(),
                           users: UserRepository = Depends(get_user_repository),
                           ):
    user = await users.get_by_email(email=login.username)
    if user is None or not verify_password(login.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    token = Token(
        access_token=create_access_token({"sub": user.email}),
        token_type="Bearer"
    )
    response.set_cookie(key="access_token", value=f"Bearer {token.access_token}",
                        httponly=True)  # set HttpOnly cookie in response
    return token
