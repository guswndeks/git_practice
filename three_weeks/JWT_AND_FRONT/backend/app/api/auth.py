from typing import Annotated

from fastapi import APIRouter, Depends, Header

from app.schemas.auth import LoginRequest, LogoutRequest, MessageResponse, RefreshRequest, SignupRequest, TokenResponse
from app.services.auth_service import authenticate_user, build_token_response, logout_user, refresh_access_token, signup_user
from app.utils.dependencies import DbSession, get_current_user

router = APIRouter()


@router.post("/signup", response_model=TokenResponse, status_code=201)
def signup(payload: SignupRequest, db: DbSession) -> TokenResponse:
    user = signup_user(db, payload)
    return build_token_response(db, user)


@router.post("/login", response_model=TokenResponse)
def login(payload: LoginRequest, db: DbSession) -> TokenResponse:
    user = authenticate_user(db, payload)
    return build_token_response(db, user)


@router.post("/refresh", response_model=TokenResponse)
def refresh(payload: RefreshRequest, db: DbSession) -> TokenResponse:
    return refresh_access_token(db, payload.refresh_token)


@router.post("/logout", response_model=MessageResponse)
def logout(
    payload: LogoutRequest,
    db: DbSession,
    current_user=Depends(get_current_user),
    authorization: Annotated[str | None, Header()] = None,
) -> MessageResponse:
    access_token = authorization.removeprefix("Bearer ").strip() if authorization else ""
    logout_user(db, current_user, access_token, payload.refresh_token)
    return MessageResponse(message="Logged out successfully")
