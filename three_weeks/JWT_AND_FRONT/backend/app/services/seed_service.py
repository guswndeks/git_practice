from sqlalchemy import select

from app.core.config import settings
from app.core.security import hash_password
from app.db.session import SessionLocal
from app.models.user import User, UserRole


def seed_admin_user() -> None:
    db = SessionLocal()
    try:
        admin = db.scalar(select(User).where(User.email == settings.admin_email))
        if not admin:
            db.add(
                User(
                    email=settings.admin_email,
                    name=settings.admin_name,
                    password_hash=hash_password(settings.admin_password),
                    role=UserRole.ADMIN,
                )
            )
            db.commit()
    finally:
        db.close()
