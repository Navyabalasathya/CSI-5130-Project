from sqlalchemy import inspect
from app.database.connection import get_engine


def extract_schema():
    engine = get_engine()
    inspector = inspect(engine)

    tables = inspector.get_table_names()
    

    schema_description = []

    for table in tables:
        columns = inspector.get_columns(table)        
        column_names = [column["name"] for column in columns]

        schema_description.append(
            f"{table}({', '.join(column_names)})"
        )

    return "\n".join(schema_description)


if __name__ == "__main__":
    schema = extract_schema()

    print("\nDatabase Schema:\n")
    print(schema)