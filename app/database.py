# app/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv() # 환경 변수 로드 (로컬 개발 시)

# Render 환경 변수에서 DB 연결 문자열을 불러옵니다.
DATABASE_URL = os.getenv("DATABASE_URL")
# 예: "postgresql://[USER]:[PASSWORD]@[HOST]:[PORT]/[DATABASE_NAME]"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency (의존성) 함수
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()