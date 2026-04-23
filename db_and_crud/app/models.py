from sqlalchemy import Integer, String
# Integer, String 은 DB 컬럼 타입입니다.

from sqlalchemy.orm import Mapped, mapped_column
# Mapped[T]:
# SQLAlchemy 2.0 스타일에서 ORM 필드를 타입 힌트와 함께 선언할 때 사용합니다.
#
# mapped_column(...):
# 기존 Column(...) 대신 사용하는 2.0 스타일 컬럼 선언 함수입니다.

from .database import Base
# Base는 ORM 모델들의 공통 부모 클래스입니다.


class User(Base):
    # User 클래스는 users 테이블과 연결되는 ORM 모델입니다.

    __tablename__ = "users"
    # 실제 DB에 생성될 테이블 이름

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )
    # id 컬럼
    # - Integer: 정수형
    # - primary_key=True: 기본키
    # - index=True: 인덱스 생성

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )
    # name 컬럼
    # - String(100): 최대 100자
    # - nullable=False: 필수값

    email: Mapped[str] = mapped_column(
        String(200),
        unique=True,
        index=True,
        nullable=False
    )
    # email 컬럼
    # - String(200): 최대 200자
    # - unique=True: 중복 불가
    # - index=True: 검색 성능 향상
    # - nullable=False: 필수값

    age: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )
    # age 컬럼
    # - Integer: 정수형
    # - nullable=True: 선택값
    # - int | None: Python 타입 힌트상 None 허용