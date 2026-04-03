print("🚀 sql_generation_chain started")
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

from app.database.schema_extractor import extract_schema

load_dotenv()

def clean_sql_output(sql_text: str) -> str:
    """
    Removes Markdown formatting like ```sql ... ```
    """

    sql_text = sql_text.strip()

    if sql_text.startswith("```"):
        # Remove opening ```sql or ```
        sql_text = sql_text.split("\n", 1)[1]

    if sql_text.endswith("```"):
        sql_text = sql_text.rsplit("\n", 1)[0]

    return sql_text.strip()


def generate_sql(question: str) -> str:
    """
    Convert natural language question into SQL query.
    """

    # Get database schema
    schema = extract_schema()

    # Create prompt template
    prompt_template = PromptTemplate(
        input_variables=["schema", "question"],
        template="""
You are an expert SQL generator.

Database Schema:
{schema}

Return ONLY a valid SQL SELECT query.
Do NOT return explanations.
Do NOT return comments.
If the requested table does not exist, use the most relevant existing table.

Question:
{question}
""",
    )

    prompt = prompt_template.format(
        schema=schema,
        question=question
    )

    # Initialize LLM
    llm = ChatOpenAI(
        model="gpt-4.1-mini",
        temperature=0
    )

    # Generate SQL
    response = llm.invoke(prompt)
    #response = llm.invoke(prompt)

    raw_sql = response.content
    print(raw_sql)
    clean_sql = clean_sql_output(raw_sql)

    return clean_sql

if __name__ == "__main__":
    question = "List customer names who live in detroit"
    sql = generate_sql(question)

    print("\nGenerated SQL:\n")
    print(sql)