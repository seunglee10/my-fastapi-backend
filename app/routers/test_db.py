from sqlalchemy import text
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:tmddb24%21%21@db.xacmeurwwbxqopelaify.supabase.co:5432/postgres"

engine = create_engine(DATABASE_URL, future=True)

with engine.connect() as conn:
    result = conn.execute(text("SELECT 1"))
    print(result.all())