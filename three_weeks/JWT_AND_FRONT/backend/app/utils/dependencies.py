from typing import Annotated

from fastapi import Depends, Header, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.security import decode_token, hash_token
from app.db.session import get_db
from app.models.blacklist import AccessTokenBlacklist
from app.models.user import User, UserRole

DbSession = Annotated[Session, Depends(get_db)]


def _extract_bearer_token(authorization: str | None) -> str:
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing bearer token")
    return authorization.removeprefix("Bearer ").strip()


def get_current_user(
    db: DbSession,
    authorization: Annotated[str | None, Header()] = None,
) -> User:
    token = _extract_bearer_token(authorization)
    token_hash = hash_token(token)
    blocked = db.scalar(select(AccessTokenBlacklist).where(AccessTokenBlacklist.token_hash == token_hash))
    if blocked:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Access token is blacklisted")

    try:
        payload = decode_token(token)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(exc)) from exc

    if payload.get("type") != "access":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid access token")

    user_id = payload.get("sub")
    user = db.get(User, int(user_id))
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    return user


def require_admin(current_user: Annotated[User, Depends(get_current_user)]) -> User:
    if current_user.role != UserRole.ADMIN:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin access required")
    return current_user
