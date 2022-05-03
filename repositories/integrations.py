import datetime
from typing import List, Optional
from db.integrations import account_integrations
from models.integrations import Integration, IntegrationIn
from .base import BaseRepository


class IntegrationsRepository(BaseRepository):

    async def create(self, owner_id: Optional[int], j: IntegrationIn) -> Integration:
        integration = Integration(
            id=0,
            name=j.name_integration,
            owner_id=owner_id,
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.utcnow(),
            is_active=j.is_active,
            code=j.code,
            api_key=j.AccessKeyId,
            api_secret=j.SecretKey,
            badge_key=j.badge_key,
        )
        values = {**integration.dict()}
        values.pop("id", None)
        query = account_integrations.insert().values(**values)
        integration.id = await self.database.execute(query=query)
        return integration

    async def update(self, id: int, badge_key, code, owner_id: Optional[int],
                     j: IntegrationIn) -> Integration:
        integration = Integration(
            id=id,
            owner_id=owner_id,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow(),
            is_active=j.is_active,
            code=code,
            api_key=j.AccessKeyId,
            api_secret=j.SecretKey,
            badge_key=badge_key,
        )
        values = {**integration.dict()}
        values.pop("id", None)
        values.pop("created_at", None)
        query = account_integrations.update().where(account_integrations.c.id == id).values(**values)
        await self.database.execute(query=query)
        return integration

    async def delete(self, id: int):
        query = account_integrations.delete().where(account_integrations.c.id == id)
        return await self.database.execute(query=query)

    async def get_all(self, limit: int = 100, skip: int = 0) -> List[Integration]:
        query = account_integrations.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)

    async def get_by_owner_id(self, id: int) -> Optional[Integration]:
        query = account_integrations.select().where(account_integrations.c.owner_id == id)
        integration = await self.database.fetch_all(query)
        if integration is None:
            return None
        return integration
