from app.database.connection import get_engine
from sqlalchemy import text

engine = get_engine()

with engine.connect() as conn:
    result = conn.execute(text("SELECT name FROM sqlite_master WHERE type='table';"))
    
    print("Tables in database:")
    for row in result:
        print(row[0])