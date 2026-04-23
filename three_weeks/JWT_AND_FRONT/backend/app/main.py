from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import api_router
from app import models  # noqa: F401
from app.core.config import settings
from app.db.base import Base
from app.db.session import engine
from app.services.seed_service import seed_admin_user


@asynccontextmanager
async def lifespan(_: FastAPI):
    Base.metadata.create_all(bind=engine)
    seed_admin_user()
    yield


app = FastAPI(
    title="JWT Member Service",
    version="1.0.0",
    description="Member management API with JWT authentication, refresh-token hashing, and access-token blacklist.",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api")


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "JWT Member Service is running"}
