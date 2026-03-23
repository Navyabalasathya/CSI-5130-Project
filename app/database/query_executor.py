from sqlalchemy import text
from app.database.connection import get_engine


def execute_query(sql_query: str):
    """
    Executes SQL query and returns results as list of dictionaries.
    """

    engine = get_engine()

    with engine.connect() as conn:
        result = conn.execute(text(sql_query))
        if result.returns_rows:
            rows = result.fetchall()
        else:
            return []        
        columns = result.keys()

        data = [
            dict(zip(columns, row))
            for row in rows
        ]

    return data


if __name__ == "__main__":
    test_sql = "SELECT * FROM customers"
    results = execute_query(test_sql)

    print("\nQuery Results:\n")
    for row in results:
        print(row)