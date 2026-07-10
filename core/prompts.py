from langchain_core.prompts import ChatPromptTemplate

SQL_GENERATION_TEMPLATE = """
You are an expert SQLite developer.

Your task is to convert a natural language question into a valid SQLite query based on the Database Schema and Chat History.

Database Schema:
{schema}

Chat History:
{chat_history}

{error_feedback}

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

SQL_GENERATION_PROMPT = ChatPromptTemplate.from_template(SQL_GENERATION_TEMPLATE)

NL_RESPONSE_TEMPLATE = """
You are a friendly data analysis assistant.

Based on the user's question, the SQL query that was run, and the database results obtained, provide a natural, concise, and accurate answer.

User's Question: {question}
SQL Query: {query}
Database Result: {result}

Answer:
"""

NL_RESPONSE_PROMPT = ChatPromptTemplate.from_template(NL_RESPONSE_TEMPLATE)