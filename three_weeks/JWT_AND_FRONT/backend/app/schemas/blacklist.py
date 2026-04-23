from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class BlacklistCreateRequest(BaseModel):
    access_token: str
    reason: str = Field(default="MANUAL_BLOCK", min_length=2, max_length=255)
    note: str | None = Field(default=None, max_length=1000)


class BlacklistUpdateRequest(BaseModel):
    reason: str | None = Field(default=None, min_length=2, max_length=255)
    note: str | None = Field(default=None, max_length=1000)


class BlacklistResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    token_hash: str
    jti: str | None
    expires_at: datetime
    reason: str
    note: str | None
    created_at: datetime
