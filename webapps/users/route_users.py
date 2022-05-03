from fastapi import APIRouter, Depends, Request, responses, status
from fastapi.templating import Jinja2Templates
from sqlalchemy.exc import IntegrityError
from api.endpoints.depends import get_user_repository
from models.user import UserIn
from repositories.users import UserRepository
from api.endpoints.users import create_user

templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)
temp_link = "accounts/register.html"


@router.get("/register/")
def register(request: Request):
    return templates.TemplateResponse(temp_link, {"request": request})


@router.post("/register/")
async def register(user: UserIn = Depends(UserIn.as_form),
                   db: UserRepository = Depends(get_user_repository)):
    form = user
    if form:
        try:
            user = await create_user(user=form, users=db)
            return responses.RedirectResponse(
                "/login", status_code=status.HTTP_302_FOUND
            )  # default is post request, to use get request added status code 302
        except IntegrityError:
            form.__dict__.get("errors").append("Duplicate username or email")
            return templates.TemplateResponse(temp_link, form.__dict__)
    return templates.TemplateResponse(temp_link, form.__dict__)
