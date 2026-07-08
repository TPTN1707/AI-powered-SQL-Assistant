from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from connect_database import llm

template = """
You are an expert SQLite developer.

Your task is to convert a natural language question into a valid SQLite query.

Database Schema:
{schema}

Question:
{question}

Rules:
- Return ONLY the SQL query.
- Do NOT explain anything.
- Do NOT use markdown.
- Do NOT wrap the SQL in ```sql.
- Do NOT add prefixes such as SQLQuery:.
- Use only SQLite syntax.
"""

prompt = ChatPromptTemplate.from_template(template)

chain = (
    prompt
    | llm
    | StrOutputParser()
)