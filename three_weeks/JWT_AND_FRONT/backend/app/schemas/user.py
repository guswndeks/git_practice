from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field

from app.models.user import UserRole


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: EmailStr
    name: str
    role: UserRole
    created_at: datetime
    updated_at: datetime


class UpdateMeRequest(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=100)
    password: str | None = Field(default=None, min_length=8, max_length=100)
