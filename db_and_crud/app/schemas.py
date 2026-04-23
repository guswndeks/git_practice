from pydantic import BaseModel, EmailStr
# BaseModel:
# FastAPI에서 요청/응답 데이터 검증에 사용하는 기본 클래스입니다.
#
# EmailStr:
# 이메일 형식인지 자동 검증해주는 타입입니다.

from typing import Optional
# Optional[T]:
# 값이 T이거나 None일 수 있음을 의미합니다.


class UserCreate(BaseModel):
    # 사용자 생성 요청용 스키마
    # POST /users 요청 본문(JSON)의 구조를 정의합니다.

    name: str
    # 사용자 이름
    # 필수 입력값이며 문자열이어야 합니다.

    email: EmailStr
    # 사용자 이메일
    # 필수 입력값이며 이메일 형식이어야 합니다.

    age: Optional[int] = None
    # 사용자 나이
    # 선택 입력값이며 입력하지 않으면 None 입니다.


class UserUpdate(BaseModel):
    # 사용자 수정 요청용 스키마
    # PUT /users/{user_id} 요청에서 사용합니다.
    # 부분 수정이 가능해야 하므로 모든 필드를 Optional 처리합니다.

    name: Optional[str] = None
    # 이름 수정값
    # 보내지 않으면 기존 값 유지

    email: Optional[EmailStr] = None
    # 이메일 수정값
    # 보내지 않으면 기존 값 유지
    # 보낸 경우 이메일 형식 검증 수행

    age: Optional[int] = None
    # 나이 수정값
    # 보내지 않으면 기존 값 유지


class UserResponse(BaseModel):
    # 응답용 스키마
    # DB에서 가져온 User ORM 객체를 어떤 형식으로 응답할지 정의합니다.

    id: int
    # 사용자 ID

    name: str
    # 사용자 이름

    email: EmailStr
    # 사용자 이메일

    age: Optional[int] = None
    # 사용자 나이 (없을 수 있음)

    class Config:
        from_attributes = True
        # SQLAlchemy ORM 객체를 Pydantic 응답 모델로 변환할 수 있게 해줍니다.
        # 즉, dict가 아니라 ORM 객체(User)를 그대로 반환해도
        # FastAPI가 자동으로 UserResponse 형태로 변환합니다.