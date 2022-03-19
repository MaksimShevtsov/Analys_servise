from pydantic import BaseModel, EmailStr


class Token(BaseModel):
    access_token: str
    token_type: str


class LoginIn(BaseModel):
    email: EmailStr
    password: str
