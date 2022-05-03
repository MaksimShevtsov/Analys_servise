from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory='templates')


@router.get("/")  # new
async def home(request: Request):
    return templates.TemplateResponse("home/index.html", {"request": request})
