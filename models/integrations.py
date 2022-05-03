import datetime
from pydantic import BaseModel, validator
from fastapi import Form
from typing import Optional
from datetime import date


class BaseIntegration(BaseModel):
    name: Optional[str]
    is_active: bool = True
    created_at: Optional[date] = datetime.datetime
    updated_at: Optional[date] = datetime.datetime

    class Config:
        orm_mode = True


class Integration(BaseIntegration):
    id: Optional[int]
    owner_id: Optional[int]
    code: str = 'test'
    api_key: Optional[str]
    api_secret: Optional[str]
    badge_key: str = 'test'


class IntegrationIn(BaseModel):
    name_integration: str
    AccessKeyId: str
    SecretKey: str
    is_active: bool
    code: str
    badge_key: str

    @classmethod
    def as_form(
            cls,
            name: str = Form(...),
            AccessKeyId: str = Form(...),
            SecretKey: str = Form(...)
    ):
        return cls(name_integration=name, AccessKeyId=AccessKeyId, SecretKey=SecretKey)
