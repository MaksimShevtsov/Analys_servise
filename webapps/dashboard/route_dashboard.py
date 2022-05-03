from fastapi import APIRouter, Depends, Request
from api.endpoints.depends import get_current_user, get_integration_repository
from fastapi.templating import Jinja2Templates
from models.user import User
from repositories.integrations import IntegrationsRepository


router = APIRouter()
templates = Jinja2Templates(directory='templates')


@router.get("/dashboard")  # new
async def dashboard(request: Request,
                    integration: IntegrationsRepository = Depends(get_integration_repository),
                    current_user: User = Depends(get_current_user)):
    list_of_integrations = await integration.get_by_owner_id(id=int(current_user.id))
    return templates.TemplateResponse("home/dashboard.html", {"request": request,
                                                              "current_user": current_user.username,
                                                              "integration": list_of_integrations})
