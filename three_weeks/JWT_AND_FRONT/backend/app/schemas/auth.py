from pydantic import BaseModel, ConfigDict, EmailStr, Field

from app.models.user import UserRole


class SignupRequest(BaseModel):
    email: EmailStr
    name: str = Field(min_length=2, max_length=100)
    password: str = Field(min_length=8, max_length=100)


class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=100)


class RefreshRequest(BaseModel):
    refresh_token: str


class UserSummary(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: EmailStr
    name: str
    role: UserRole


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    access_token_expires_in: int
    refresh_token_expires_in: int
    user: UserSummary


class LogoutRequest(BaseModel):
    refresh_token: str


class MessageResponse(BaseModel):
    message: str
