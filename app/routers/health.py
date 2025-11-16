from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db # database.py에서 정의한 get_db 임포트
# from ..models import Item # SQLAlchemy 모델 임포트

router = APIRouter()

# 3. BE-DB 연결 확인을 위한 테스트 엔드포인트
@router.get("/api/v1/db-test")
def test_db_connection(db: Session = Depends(get_db)):
    try:
        # 실제 테이블에 대한 간단한 쿼리 실행
        # 예: db.query(Item).limit(1).all()
        # 간단히 DB 접속 및 세션 생성이 되는지 확인하려면 아래 쿼리를 사용합니다.
        db.execute("SELECT 1")
        return {"message": "DB connection successful and simple query executed"}
    except Exception as e:
        return {"message": "DB connection FAILED", "error": str(e)}
