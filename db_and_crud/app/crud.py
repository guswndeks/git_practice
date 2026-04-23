from sqlalchemy.orm import Session
# Session:
# SQLAlchemy에서 DB 작업을 수행하는 세션 객체 타입입니다.

from . import models, schemas
# models: ORM 모델
# schemas: Pydantic 스키마


def create_user(db: Session, user: schemas.UserCreate):
    # 사용자 생성 함수
    # - db: DB 세션
    # - user: 사용자 생성 요청 데이터

    db_user = models.User(
        name=user.name,
        email=user.email,
        age=user.age
    )
    # Pydantic 스키마 값을 이용하여
    # 실제 DB에 저장할 ORM 객체 생성

    db.add(db_user)
    # db.add(...)
    # - 이 객체를 DB 저장 대상으로 세션에 등록합니다.
    # - 아직 실제 DB에 INSERT가 확정된 것은 아닙니다.
    # - Session이 이 객체를 추적하도록 등록하는 단계입니다.

    db.commit()
    # db.commit()
    # - 현재 세션의 변경사항을 실제 DB에 반영합니다.
    # - create에서는 INSERT SQL이 실행됩니다.
    # - commit 전까지는 트랜잭션 내부 변경 상태입니다.

    db.refresh(db_user)
    # db.refresh(...)
    # - DB에 저장된 최신 상태를 다시 ORM 객체에 반영합니다.
    # - 자동 생성된 id 값 등을 객체에 채워 넣습니다.

    return db_user


def get_users(db: Session):
    # 전체 사용자 목록 조회
    return db.query(models.User).all()


def get_user(db: Session, user_id: int):
    # 특정 사용자 1명 조회
    # 없으면 None 반환
    return db.query(models.User).filter(models.User.id == user_id).first()


def update_user(db: Session, user_id: int, user_data: schemas.UserUpdate):
    # 사용자 수정 함수
    # - 대상 사용자를 찾고
    # - 전달된 값만 수정한 뒤
    # - commit/refresh 수행

    db_user = db.query(models.User).filter(models.User.id == user_id).first()

    if not db_user:
        return None

    if user_data.name is not None:
        db_user.name = user_data.name
        # name 값이 전달된 경우에만 수정

    if user_data.email is not None:
        db_user.email = user_data.email
        # email 값이 전달된 경우에만 수정

    if user_data.age is not None:
        db_user.age = user_data.age
        # age 값이 전달된 경우에만 수정

    db.commit()
    # commit을 호출해야 UPDATE 내용이 실제 DB에 반영됩니다.

    db.refresh(db_user)
    # DB에 반영된 최신 상태를 다시 ORM 객체에 동기화합니다.

    return db_user


def delete_user(db: Session, user_id: int):
    # 사용자 삭제 함수
    # - 대상 사용자를 찾고
    # - 존재하면 삭제 후 commit
    # - 없으면 None 반환

    db_user = db.query(models.User).filter(models.User.id == user_id).first()

    if not db_user:
        return None

    db.delete(db_user)
    # db.delete(...)
    # - ORM 객체를 삭제 대상으로 표시합니다.
    # - 아직 바로 DB에서 지워지는 것은 아니고
    #   commit 시점에 DELETE SQL이 실행됩니다.

    db.commit()
    # 삭제 내용을 실제 DB에 반영합니다.

    return db_user