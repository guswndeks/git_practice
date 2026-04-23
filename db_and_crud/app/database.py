import os
# os 모듈은 운영체제의 환경변수(Environment Variable)를 읽을 때 사용합니다.
# 예: DATABASE_URL, POSTGRES_USER 같은 값을 코드 바깥에서 주입할 수 있습니다.

from dotenv import load_dotenv
# load_dotenv()는 .env 파일에 작성한 환경변수를 현재 파이썬 실행 환경에 로드합니다.

from sqlalchemy import create_engine
# create_engine():
# SQLAlchemy가 DB와 통신하기 위한 "엔진" 객체를 생성하는 함수입니다.
# 쉽게 말해, PostgreSQL과 연결하기 위한 핵심 통로를 만듭니다.

from sqlalchemy.orm import sessionmaker, declarative_base
# sessionmaker():
# DB 작업용 Session 객체를 생성하는 "세션 공장(factory)"입니다.
# SessionLocal()을 호출하면 실제 DB 세션 객체가 만들어집니다.
#
# declarative_base():
# ORM 모델 클래스들이 상속받는 기본 부모 클래스를 생성합니다.
# class User(Base): 처럼 사용합니다.


# .env 파일 로드
load_dotenv()


# os.getenv("환경변수명", 기본값)
# - 운영체제/환경에 해당 이름의 환경변수가 있으면 그 값을 사용
# - 없으면 두 번째 인자인 기본값 사용
#
# 즉, 여기서는 DATABASE_URL 환경변수가 존재하면 그 값을 사용하고
# 없으면 기본 PostgreSQL 접속 문자열을 사용합니다.
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:1234@localhost:5432/fastapi_db"
)


# create_engine(...)
# - 실제 DB 연결용 엔진 생성
# - echo=True: SQLAlchemy가 내부적으로 실행하는 SQL문을 콘솔에 출력
#   학습과 디버깅에 매우 유용합니다.
engine = create_engine(DATABASE_URL, echo=True)


# sessionmaker(...)
# - DB 세션 생성 규칙을 정의하는 공장 함수
#
# autocommit=False
# - commit을 자동으로 하지 않음
# - 즉, db.commit()을 직접 호출해야 INSERT/UPDATE/DELETE가 실제 반영됨
#
# autoflush=False
# - 세션 변경사항을 자동 flush 하지 않음
# - 학습 단계에서는 commit/refresh 흐름을 이해하기 좋음
#
# bind=engine
# - 어떤 DB 엔진과 연결되는 세션인지 지정
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# declarative_base()
# - ORM 모델들의 부모 클래스 Base 생성
# - Base를 상속한 클래스들이 SQLAlchemy ORM 모델로 인식됨
Base = declarative_base()