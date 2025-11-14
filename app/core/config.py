from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

class Settings(BaseSettings):
    # Supabase PostgreSQL 연결 URL을 환경 변수에서 가져옵니다.
    # 환경 변수 이름은 SUPABASE_URL이어야 합니다.
    SUPABASE_URL: str

    # FastAPI 서버가 실행될 포트를 설정합니다. (옵션)
    SERVER_PORT: int = 8000

    # JWT 시크릿 키 등 중요한 정보는 여기에 추가합니다.
    SECRET_KEY: str = "YOUR_SUPER_SECRET_KEY"

    # BaseSettings의 내부 설정 클래스
    class Config:
        # Pydantic이 환경 변수를 읽는 방법을 설정합니다.
        env_file = ".env"
        env_file_encoding = 'utf-8'

# 애플리케이션 전체에서 사용할 설정 객체 인스턴스
settings = Settings()

# 사용법: settings.SUPABASE_URL