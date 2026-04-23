from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select

from app.core.security import decode_token, hash_token
from app.models.blacklist import AccessTokenBlacklist
from app.models.user import User
from app.schemas.blacklist import BlacklistCreateRequest, BlacklistResponse, BlacklistUpdateRequest
from app.utils.dependencies import DbSession, require_admin

router = APIRouter()


@router.get("", response_model=list[BlacklistResponse])
def list_blacklist(db: DbSession, _: User = Depends(require_admin)) -> list[AccessTokenBlacklist]:
    return list(db.scalars(select(AccessTokenBlacklist).order_by(AccessTokenBlacklist.id.desc())).all())


@router.post("", response_model=BlacklistResponse, status_code=201)
def create_blacklist(payload: BlacklistCreateRequest, db: DbSession, _: User = Depends(require_admin)) -> AccessTokenBlacklist:
    try:
        token_payload = decode_token(payload.access_token)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc

    if token_payload.get("type") != "access":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Only access tokens can be blacklisted")

    token_hash = hash_token(payload.access_token)
    existing = db.scalar(select(AccessTokenBlacklist).where(AccessTokenBlacklist.token_hash == token_hash))
    if existing:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Token is already blacklisted")

    item = AccessTokenBlacklist(
        token_hash=token_hash,
        jti=token_payload.get("jti"),
        expires_at=datetime.fromtimestamp(token_payload["exp"], tz=timezone.utc),
        reason=payload.reason,
        note=payload.note,
    )
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@router.patch("/{item_id}", response_model=BlacklistResponse)
def update_blacklist(
    item_id: int,
    payload: BlacklistUpdateRequest,
    db: DbSession,
    _: User = Depends(require_admin),
) -> AccessTokenBlacklist:
    item = db.get(AccessTokenBlacklist, item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blacklist item not found")
    if payload.reason is not None:
        item.reason = payload.reason
    if payload.note is not None:
        item.note = payload.note
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@router.delete("/{item_id}", status_code=204)
def delete_blacklist(item_id: int, db: DbSession, _: User = Depends(require_admin)) -> None:
    item = db.get(AccessTokenBlacklist, item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blacklist item not found")
    db.delete(item)
    db.commit()
