from sqlalchemy import text
from database import engine

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print("DB接続成功:", result.scalar())
except Exception as e:
    print("DB接続失敗:", e)
