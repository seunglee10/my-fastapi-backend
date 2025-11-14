from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User
from app.schemas import UserCreate, UserResponse # Pydantic 스키마 가져오기

# 비밀번호 해싱을 위한 라이브러리 (실제 프로젝트에서는 passlib 등을 사용합니다)
# 여기서는 간단히 문자열을 반환하는 함수로 대체합니다.
def hash_password(password: str) -> str:
    # TODO: 실제로는 bcrypt나 Argon2를 사용하여 안전하게 해싱해야 합니다.
    return f"hashed_{password}_securely"

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

# 1. 사용자 등록 (회원가입) 엔드포인트
@router.post("/signup", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def signup_user(user_data: UserCreate, db: Session = Depends(get_db)):
    # 1. 이메일 중복 확인
    db_user = db.query(User).filter(User.email == user_data.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # 2. 비밀번호 해싱
    hashed_password = hash_password(user_data.password)

    # 3. 새 사용자 모델 인스턴스 생성
    new_user = User(
        email=user_data.email,
        hashed_password=hashed_password,
    )

    # 4. DB에 저장
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # 5. 응답으로 Pydantic 모델 반환 (UserResponse)
    return new_user

# 2. 인증 상태 확인 엔드포인트 (이전에 작성된 것)
@router.get("/status")
def get_auth_status(db: Session = Depends(get_db)):
    try:
        db.execute("SELECT 1")
        return {"status": "Auth Router is active", "db_status": "Connected"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database Connection Error: {e}")