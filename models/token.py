from pydantic import BaseModel, EmailStr, constr
from fastapi import Form


class Token(BaseModel):
    access_token: str
    token_type: str


class LoginIn(BaseModel):
    email: EmailStr
    password: str

    @classmethod
    def as_form(
            cls,
            email: str = Form(...),
            password: constr(min_length=8) = Form(...),
    ):
        return cls(email=email, password=password)
