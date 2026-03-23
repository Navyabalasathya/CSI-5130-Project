from langchain_openai import ChatOpenAI

llm = ChatOpenAI(temperature=0)


def explain_results(question, sql, results):
    prompt = f"""
You are a helpful data analyst.

User Question:
{question}

SQL Query:
{sql}

Query Results:
{results}

Explain the results in simple, clear natural language.
Be concise and user-friendly.
"""

    response = llm.invoke(prompt)
    return response.content.strip()