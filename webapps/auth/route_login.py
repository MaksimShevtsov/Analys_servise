from api.endpoints.login import login_for_access
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from models.accounts_profil import LoginForm
from repositories.users import UserRepository
from api.endpoints.depends import get_user_repository


templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)


@router.get("/login")
def login(request: Request):
    return templates.TemplateResponse("accounts/login.html", {"request": request})


@router.post("/login")
async def login(request: Request, db: UserRepository = Depends(get_user_repository)):
    form = LoginForm(request)
    await form.load_data()
    if await form.is_valid():
        try:
            form.__dict__.update(msg="Login Successful :)")
            response = RedirectResponse("/dashboard")
            await login_for_access(response=response, login=form, users=db)
            return response
        except HTTPException:
            form.__dict__.update(msg="")
            form.__dict__.get("errors").append("Incorrect Email or Password")
            return templates.TemplateResponse("auth/login.html", form.__dict__)
    return templates.TemplateResponse("auth/login.html", form.__dict__)