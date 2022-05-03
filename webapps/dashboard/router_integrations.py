from api.endpoints.integrations import create_integrations
from fastapi import APIRouter, HTTPException, status, Depends, Request, responses
from repositories.integrations import IntegrationsRepository
from api.endpoints.depends import get_user_repository, get_current_user, get_integration_repository
from fastapi.templating import Jinja2Templates
from models.user import User
from models.integrations import Integration
from models.integrations_form import IntegrationIn
from fastapi.security.utils import get_authorization_scheme_param
from repositories.users import UserRepository

router = APIRouter()
templates = Jinja2Templates(directory='templates')
temp_link = "home/integrations.html"


@router.get("/integrations")  # new
async def integrations(request: Request,
                       integration: IntegrationsRepository = Depends(get_integration_repository),
                       current_user: User = Depends(get_current_user)):
    list_of_integrations = await integration.get_by_owner_id(id=int(current_user.id))
    return templates.TemplateResponse(temp_link, {"request": request,
                                                  "current_user": current_user.username,
                                                  "integrations": list_of_integrations})


@router.post("/integrations")
async def integrations_post(request: Request, db: UserRepository = Depends(get_user_repository),
                            integrations: IntegrationsRepository = Depends(get_integration_repository)):
    form = IntegrationIn(request)
    await form.load_data()
    if form.is_valid():
        try:
            token = request.cookies.get("access_token")
            scheme, param = get_authorization_scheme_param(
                token
            )  # scheme will hold "Bearer" and param will hold actual token value
            current_user: User = await get_current_user(token=param, users=db)
            integration: Integration = await create_integrations(i=form, current_user=current_user,
                                                                 integrations=integrations)
            return responses.RedirectResponse("/integrations", status_code=status.HTTP_302_FOUND)
        except HTTPException:
            form.__dict__.update(msg="")
            form.__dict__.get("errors").append("Incorrect Email or Password")
            return templates.TemplateResponse(temp_link, form.__dict__)
    return templates.TemplateResponse(temp_link, form.__dict__)
