from datetime import datetime, timezone

from fastapi import HTTPException, status
from sqlalchemy import delete, select
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.security import (
    create_access_token,
    create_refresh_token,
    decode_token,
    hash_password,
    hash_token,
    verify_password,
)
from app.models.blacklist import AccessTokenBlacklist
from app.models.refresh_token import RefreshToken
from app.models.user import User, UserRole
from app.schemas.auth import LoginRequest, SignupRequest, TokenResponse, UserSummary


def signup_user(db: Session, payload: SignupRequest) -> User:
    existing = db.scalar(select(User).where(User.email == payload.email))
    if existing:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already exists")

    user = User(
        email=payload.email,
        name=payload.name,
        password_hash=hash_password(payload.password),
        role=UserRole.USER,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def authenticate_user(db: Session, payload: LoginRequest) -> User:
    user = db.scalar(select(User).where(User.email == payload.email))
    if not user or not verify_password(payload.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")
    return user


def build_token_response(db: Session, user: User) -> TokenResponse:
    access_token, _, access_expires_at = create_access_token(str(user.id), user.role.value)
    refresh_token, refresh_jti, refresh_expires_at = create_refresh_token(str(user.id))

    db.execute(delete(RefreshToken).where(RefreshToken.user_id == user.id))
    db.add(
        RefreshToken(
            user_id=user.id,
            token_hash=hash_token(refresh_token),
            jti=refresh_jti,
            expires_at=refresh_expires_at,
        )
    )
    db.commit()

    return TokenResponse(
        access_token=access_token,
        refresh_token=refresh_token,
        access_token_expires_in=settings.access_token_expire_minutes * 60,
        refresh_token_expires_in=settings.refresh_token_expire_days * 24 * 60 * 60,
        user=UserSummary.model_validate(user),
    )


def refresh_access_token(db: Session, raw_refresh_token: str) -> TokenResponse:
    try:
        payload = decode_token(raw_refresh_token)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(exc)) from exc

    if payload.get("type") != "refresh":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")

    token_hash = hash_token(raw_refresh_token)
    stored_token = db.scalar(select(RefreshToken).where(RefreshToken.token_hash == token_hash))
    if not stored_token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Refresh token not found")

    if stored_token.expires_at <= datetime.now(timezone.utc):
        db.delete(stored_token)
        db.commit()
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Refresh token expired")

    user = db.get(User, stored_token.user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")

    return build_token_response(db, user)


def logout_user(db: Session, user: User, access_token: str, refresh_token: str) -> None:
    try:
        access_payload = decode_token(access_token)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(exc)) from exc
    db.add(
        AccessTokenBlacklist(
            token_hash=hash_token(access_token),
            jti=access_payload.get("jti"),
            expires_at=datetime.fromtimestamp(access_payload["exp"], tz=timezone.utc),
            reason="LOGOUT",
            note=f"User {user.email} logged out",
        )
    )

    db.execute(delete(RefreshToken).where(RefreshToken.token_hash == hash_token(refresh_token)))
    db.commit()
