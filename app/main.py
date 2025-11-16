from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from .routers import health_router # health 라우터가 있다면 임포트

app = FastAPI()

# 1. FE-BE 연결 확인을 위한 CORS 설정
origins = [
    "http://localhost:3000",
    "https://vercel-render-supabase-login-3mx1egdk6-seunglee10s-projects.vercel.app/" # Vercel 배포 주소
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. 상태 확인 엔드포인트 (선택 사항)
@app.get("/api/v1/health")
def read_health():
    return {"status": "Backend is running"}