from typing import List, Optional

from fastapi import Request


class IntegrationIn:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.AccessKeyId: Optional[str] = None
        self.SecretKey: Optional[str] = None
        self.name_integration: Optional[str] = None
        self.is_active: Optional[str] = True
        self.code: Optional[str] = 'test'
        self.badge_key: Optional[str] = 'None'

    async def load_data(self):
        form = await self.request.form()
        self.AccessKeyId = form.get("api_key")
        self.SecretKey = form.get("api_secret")
        self.name_integration = form.get("name")

    def is_valid(self):
        if not self.AccessKeyId:
            self.errors.append("A valid AccessKeyId is required")
        if not self.SecretKey:
            self.errors.append("A valid SecretKey is required")
        if not self.name_integration:
            self.errors.append("Description too short")
        if not self.errors:
            return True
        return False
