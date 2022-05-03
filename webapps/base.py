from fastapi import APIRouter
from webapps.auth import route_login
from webapps.dashboard import route_dashboard, route_settings, router_integrations
from webapps.users import route_users
from webapps.home import route_home

api_router = APIRouter()
api_router.include_router(route_users.router, prefix="", tags=["users-webapps"])
api_router.include_router(route_login.router, prefix="", tags=["auth-webapps"])
api_router.include_router(route_dashboard.router, prefix="", tags=["dashboard-webapps"])
api_router.include_router(route_home.router, prefix="", tags=["home-webapps"])
api_router.include_router(route_settings.router, prefix="", tags=["settings-webapps"])
api_router.include_router(router_integrations.router, prefix="", tags=["transactions-webapps"])
