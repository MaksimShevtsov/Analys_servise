import datetime
from fastapi import Form
from pydantic import BaseModel, EmailStr, validator, constr
from typing import Optional


class User(BaseModel):
    id: Optional[str] = None
    email: EmailStr
    username: str
    created_at: datetime.datetime
    update_at: datetime.datetime

    class Config:
        orm_mode = True


class UserCreate(User):
    hashed_password: str


class UserIn(BaseModel):
    name: str
    email: EmailStr
    password: constr(min_length=8)
    password2: str

    @classmethod
    def as_form(
            cls,
            name: str = Form(...),
            email: str = Form(...),
            password: constr(min_length=8) = Form(...),
            password2: str = Form(...)
    ):
        return cls(name=name, email=email, password=password, password2=password2)

    @validator('password2')
    def passwords_match(cls, v, values, **kwargs):
        if 'password' in values and v != values['password']:
            raise ValueError('passwords do not match')
        return v


