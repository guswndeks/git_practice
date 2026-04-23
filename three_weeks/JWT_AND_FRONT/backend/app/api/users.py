from fastapi import APIRouter, Depends
from sqlalchemy import select

from app.core.security import hash_password
from app.models.user import User, UserRole
from app.schemas.auth import UserSummary
from app.schemas.user import UpdateMeRequest, UserResponse
from app.utils.dependencies import DbSession, get_current_user, require_admin

router = APIRouter()


@router.get("", response_model=list[UserSummary])
def list_users(db: DbSession, _: User = Depends(require_admin)) -> list[User]:
    return list(db.scalars(select(User).order_by(User.id)).all())


@router.get("/me", response_model=UserResponse)
def get_me(current_user: User = Depends(get_current_user)) -> User:
    return current_user


@router.patch("/me", response_model=UserResponse)
def update_me(payload: UpdateMeRequest, db: DbSession, current_user: User = Depends(get_current_user)) -> User:
    if payload.name is not None:
        current_user.name = payload.name
    if payload.password is not None:
        current_user.password_hash = hash_password(payload.password)
    db.add(current_user)
    db.commit()
    db.refresh(current_user)
    return current_user


@router.get("/{user_id}", response_model=UserResponse)
def get_user_detail(user_id: int, db: DbSession, current_user: User = Depends(get_current_user)) -> User:
    target_user = db.get(User, user_id)
    if not target_user:
        from fastapi import HTTPException, status

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    if current_user.role != UserRole.ADMIN and current_user.id != user_id:
        from fastapi import HTTPException, status

        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Access denied")
    return target_user
