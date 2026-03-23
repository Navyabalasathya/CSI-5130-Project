from sqlalchemy import text
from app.database.connection import get_engine


def test_connection():
    engine = get_engine()

    # open connection and run a simple SQL command
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))

    print("Database connection successful.")


if __name__ == "__main__":
    test_connection()