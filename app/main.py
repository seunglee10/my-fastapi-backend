from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from app.routers import auth # auth 라우터 모듈 가져오기
from app.core.config import settings # 설정 가져오기
from app.database import engine, Base
from app import models # models.py에서 정의된 모든 모델을 가져옴 (테이블 생성용)

# FastAPI 애플리케이션 인스턴스 생성
app = FastAPI(
    title="FastAPI Supabase Backend",
    description="Python/FastAPI with SQLAlchemy 2.0+ and Supabase/Render",
    version="1.0.0"
)

# 1. CORS 설정 (Vercel과의 통신을 위해 필수)
# TODO: 배포 후에는 실제 Vercel 도메인으로 변경해야 합니다.
origins = [
    "http://localhost:3000", # 로컬 FE 개발용
    "https://your-vercel-frontend-domain.vercel.app", # Vercel 배포 도메인
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. 데이터베이스 테이블 생성
# Base에 정의된 모든 모델을 사용하여 DB에 테이블이 없으면 생성합니다.
# NOTE: 실제 운영에서는 Alembic 같은 마이그레이션 툴을 사용해야 합니다.
Base.metadata.create_all(bind=engine)

# 3. 라우터 포함 (경로 등록)
app.include_router(auth.router)

# 루트 경로
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Backend"}


# 개발용 서버 실행 명령 (Render 배포 시에는 사용하지 않음)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=settings.SERVER_PORT)