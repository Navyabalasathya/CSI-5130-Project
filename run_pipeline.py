from app.chains.sql_generation_chain import generate_sql
from app.database.query_executor import execute_query


def ask_question(question: str):
    print("\nUser Question:")
    print(question)

    # Step 1: Generate SQL
    sql = generate_sql(question)

    print("\nGenerated SQL:")
    print(sql)

    # Step 2: Execute SQL
    results = execute_query(sql)

    print("\nQuery Results:")
    if results:
        for row in results:
            print(row)
    else:
        print("No results found.")


if __name__ == "__main__":
    question = input("Ask a question about the database: ")
    ask_question(question)