from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory='templates')


@router.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("/home/index.html", context={"request": request})
