from typing import List
from models.integrations import Integration, IntegrationIn
from models.user import User
from repositories.integrations import IntegrationsRepository
from fastapi import APIRouter, Depends, status, HTTPException
from .depends import get_integration_repository, get_current_user

router = APIRouter()


@router.get("/", response_model=List[Integration])
async def read_integrations(
        limit: int = 100,
        skip: int = 0,
        integration: IntegrationsRepository = Depends(get_integration_repository)):
    return await integration.get_all(limit=limit, skip=skip)


@router.post("/", response_model=Integration)
async def create_integrations(i: IntegrationIn,
                              integrations: IntegrationsRepository = Depends(get_integration_repository),
                              current_user: User = Depends(get_current_user)):
    return await integrations.create(owner_id=current_user.id, j=i)


@router.patch("/", response_model=Integration)
async def update_integrations(
        id: int,
        integrations: IntegrationsRepository = Depends(get_integration_repository),
        current_user: User = Depends(get_current_user)):
    integration = await integrations.get_by_id(id=id)
    if integration is None or integration.id != current_user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job not found")
    return await integrations.update(id=id, owner_id=current_user.id, j=i, badge_key=None, code=None)


@router.delete("/")
async def delete_integrations(id: int,
                              integrations: IntegrationsRepository = Depends(get_integration_repository),
                              current_user: User = Depends(get_current_user)):
    integration = await integrations.get_by_id(id=id)
    not_found_exception = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job not found")
    if integration is None or integration.id != current_user.id:
        raise not_found_exception
    result = await integrations.delete(id=id)
    return {"status": True}
