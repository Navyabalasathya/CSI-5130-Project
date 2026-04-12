print("sql_generation_chain started")
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


def generate_sql(question: str, context) -> str:
    """
    Convert natural language question into SQL query.
    """

    # Create prompt template
    prompt_template = PromptTemplate(
        input_variables=["context", "question"],
        template="""
You are an expert SQL generator.

Database context:
{context}

Think step-by-step about:
- relevant tables
- joins needed
- aggregations

Then generate the SQL.

IMPORTANT RULES:
- Use ONLY tables and columns from the context
- Always use proper JOIN conditions when multiple tables are needed
- Prefer explicit JOINs over subqueries
- Use table aliases for readability
- If aggregation is needed, use GROUP BY correctly

Return ONLY SQL.
Do NOT return explanations or comments.

GUIDELINES:
- Interpret the user's question carefully before generating SQL
- If the question asks for "highest value order", compute order value as SUM(price + freight_value) per order
- Use appropriate tables based on the question
- Do not assume unnecessary tables
- Do not add extra joins unless required

Question:
{question}
""",
    )

    prompt = prompt_template.format(
        context=context,
        question=question
    )

    # Initialize LLM
    llm = ChatOpenAI(
        model="gpt-4.1-mini",
        temperature=0
    )

    # Generate SQL
    response = llm.invoke(prompt)
    
    raw_sql = response.content
    clean_sql = clean_sql_output(raw_sql)

    return clean_sql

if __name__ == "__main__":
    question = "List customer names who live in detroit"
    sql = generate_sql(question)

    print("\nGenerated SQL:\n")
    print(sql)