from app.chains.sql_generation_chain import generate_sql
from app.database.query_executor import execute_query
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from app.chains.result_explainer import explain_results


llm = ChatOpenAI(temperature=0)


def fix_sql_query(bad_sql, error_message, question, schema):
    repair_prompt = f"""
You are an expert SQL assistant.

The following SQL query failed.

User Question:
{question}

Failed SQL:
{bad_sql}

Database Error:
{error_message}

Available Database Schema:
{schema}

Fix the SQL query so it works correctly.
Return ONLY the corrected SQL SELECT query.
Do not include explanations or comments.
If the requested table does not exist, use the most relevant existing table.
"""

    response = llm.invoke(repair_prompt)
    return response.content.strip()


def ask_with_self_correction(question: str):
    print("\nUser Question:")
    print(question)

    # Step 1: Generate SQL
    sql = generate_sql(question)

    # Step 2: Try execution
    try:
        results = execute_query(sql)        
        explanation = explain_results(question, sql, results)
        return results, explanation
        
    except Exception as e:

        #print("\n⚠️ Execution failed. Attempting to fix...\n")
        #print("Error:", e)

        # Step 3: Ask LLM to fix SQL
        schema = get_schema()
        fixed_sql = fix_sql_query(sql, str(e), question)

        #print("\nFixed SQL:")
        #print(fixed_sql)

        # Step 4: Retry execution
        try:
            results = execute_query(fixed_sql)
            return results, explanation

            #print("\nQuery Results After Fix:")
            #for row in results:
                #print(row)

        except Exception as e2:
            #print("\n❌ Still failed after correction.")
            #print("Error:", e2)
            return results, explanation

if __name__ == "__main__":
    question = input("Ask a question about the database: ")
    ask_with_self_correction(question)