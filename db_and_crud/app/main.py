from fastapi import FastAPI, Depends, HTTPException
# FastAPI:
# API 애플리케이션 객체 생성용 클래스
#
# Depends:
# 의존성 주입(Dependency Injection) 기능
# 여기서는 DB 세션을 각 API 함수에 자동 주입할 때 사용
#
# HTTPException:
# 에러 상황에서 HTTP 상태코드와 메시지를 반환할 때 사용

from sqlalchemy.orm import Session
# Session 타입 힌트용 import

from sqlalchemy.exc import IntegrityError
# IntegrityError:
# DB 제약조건 위반 시 발생하는 예외
# 예: unique=True인 email 중복 입력

from .database import SessionLocal, engine, Base
# SessionLocal: DB 세션 생성용
# engine: DB 연결 엔진
# Base: ORM 모델들의 부모 클래스

from . import schemas, crud
# schemas: 요청/응답 검증용 Pydantic 스키마
# crud: 실제 DB 처리 함수들


# Base.metadata.create_all(bind=engine)
# - Base를 상속한 모든 ORM 모델을 기준으로
#   DB에 테이블이 없으면 생성합니다.
# - 즉, 앱 시작 시 users 테이블이 자동 생성됩니다.
Base.metadata.create_all(bind=engine)


# FastAPI 앱 생성
app = FastAPI(
    title="FastAPI + PostgreSQL CRUD Example",
    description="Docker Compose로 PostgreSQL을 실행하고, FastAPI + SQLAlchemy로 User CRUD를 수행하는 예제",
    version="1.0.0"
)
# title, description, version 값은 Swagger / ReDoc / OpenAPI 문서에 반영됩니다.


def get_db():
    # DB 세션 생성 및 종료를 담당하는 함수
    # Depends(get_db) 로 각 API에 주입됩니다.

    db = SessionLocal()
    # 실제 DB 세션 객체 생성

    try:
        yield db
        # API 함수에 db 세션 전달
    finally:
        db.close()
        # 요청 처리가 끝나면 세션 종료
        # 연결 자원 누수를 막기 위해 중요


@app.get("/", tags=["Root"])
def root():
    # 기본 접속 확인용 API
    return {"message": "FastAPI + PostgreSQL + SQLAlchemy CRUD"}


@app.post("/users", response_model=schemas.UserResponse, tags=["Users"])
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # 사용자 생성 API
    #
    # - user: 요청 본문(JSON)을 UserCreate 스키마로 검증한 값
    # - db: Depends(get_db)를 통해 주입받은 DB 세션
    #
    # response_model=UserResponse:
    # 반환값을 UserResponse 형식으로 변환해서 응답

    try:
        return crud.create_user(db, user)
    except IntegrityError:
        db.rollback()
        # rollback():
        # commit 실패 시 현재 트랜잭션 상태를 되돌립니다.
        # 중복 email 등 제약조건 위반 시 세션을 정상 상태로 복구하는 데 필요합니다.

        raise HTTPException(status_code=400, detail="이미 존재하는 이메일입니다.")


@app.get("/users", response_model=list[schemas.UserResponse], tags=["Users"])
def read_users(db: Session = Depends(get_db)):
    # 전체 사용자 목록 조회 API
    return crud.get_users(db)


@app.get("/users/{user_id}", response_model=schemas.UserResponse, tags=["Users"])
def read_user(user_id: int, db: Session = Depends(get_db)):
    # 특정 사용자 조회 API
    # user_id는 URL 경로 변수(Path Parameter)입니다.

    db_user = crud.get_user(db, user_id)

    if not db_user:
        raise HTTPException(status_code=404, detail="사용자를 찾을 수 없습니다.")

    return db_user


@app.put("/users/{user_id}", response_model=schemas.UserResponse, tags=["Users"])
def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    # 사용자 수정 API

    try:
        db_user = crud.update_user(db, user_id, user)

        if not db_user:
            raise HTTPException(status_code=404, detail="사용자를 찾을 수 없습니다.")

        return db_user

    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="이미 존재하는 이메일입니다.")


@app.delete("/users/{user_id}", tags=["Users"])
def delete_user(user_id: int, db: Session = Depends(get_db)):
    # 사용자 삭제 API

    db_user = crud.delete_user(db, user_id)

    if not db_user:
        raise HTTPException(status_code=404, detail="사용자를 찾을 수 없습니다.")

    return {"message": "사용자가 삭제되었습니다."}