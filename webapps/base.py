from fastapi import APIRouter
from webapps.auth import route_login
from webapps.dashboard import route_dashboard
from webapps.users import route_users


api_router = APIRouter()
# api_router.include_router(route_users.router, prefix="", tags=["users-webapps"])
api_router.include_router(route_login.router, prefix="", tags=["auth-webapps"])
api_router.include_router(route_dashboard.router, prefix="", tags=["dashboard-webapps"])
