from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from app.core.config import settings # Config 모듈에서 설정 가져오기
from typing import Generator

# Supabase URL을 설정에서 가져옵니다.
SQLALCHEMY_DATABASE_URL = settings.SUPABASE_URL

# Engine 생성
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

# 세션 생성기
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 모든 모델의 기반 클래스 (SQLAlchemy 2.0+ 스타일)
class Base(DeclarativeBase):
    pass

# 의존성 주입(Dependency Injection)을 위한 함수
# API 요청마다 독립적인 DB 세션을 제공합니다.
def get_db() -> Generator[SessionLocal, None, None]:
    db = SessionLocal()
    try:
        # yield를 사용하여 세션을 반환하고, 요청 처리 후 finally 블록이 실행됩니다.
        yield db
    finally:
        # 세션 닫기
        db.close()