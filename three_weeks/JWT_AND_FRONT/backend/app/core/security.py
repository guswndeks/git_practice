from datetime import datetime, timedelta, timezone
from hashlib import sha256
from uuid import uuid4

from jose import JWTError, jwt
from passlib.context import CryptContext

from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def hash_token(token: str) -> str:
    return sha256(token.encode("utf-8")).hexdigest()


def create_access_token(subject: str, role: str) -> tuple[str, str, datetime]:
    expires_at = datetime.now(timezone.utc) + timedelta(minutes=settings.access_token_expire_minutes)
    jti = str(uuid4())
    payload = {
        "sub": subject,
        "role": role,
        "type": "access",
        "jti": jti,
        "exp": expires_at,
    }
    token = jwt.encode(payload, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)
    return token, jti, expires_at


def create_refresh_token(subject: str) -> tuple[str, str, datetime]:
    expires_at = datetime.now(timezone.utc) + timedelta(days=settings.refresh_token_expire_days)
    jti = str(uuid4())
    payload = {
        "sub": subject,
        "type": "refresh",
        "jti": jti,
        "exp": expires_at,
    }
    token = jwt.encode(payload, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)
    return token, jti, expires_at


def decode_token(token: str) -> dict:
    try:
        return jwt.decode(token, settings.jwt_secret_key, algorithms=[settings.jwt_algorithm])
    except JWTError as exc:
        raise ValueError("Invalid or expired token") from exc
