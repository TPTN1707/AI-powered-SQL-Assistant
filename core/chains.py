from langchain_core.output_parsers import StrOutputParser
from core.prompts import SQL_GENERATION_PROMPT, NL_RESPONSE_PROMPT
from database.connection import llm # Import LLM

# Chain for SQL Generation
sql_generation_chain = (
    SQL_GENERATION_PROMPT
    | llm
    | StrOutputParser()
)

# Chain for Natural Language Response (new)
nl_response_chain = (
    NL_RESPONSE_PROMPT
    | llm
    | StrOutputParser()
)

__all__ = ["sql_generation_chain", "nl_response_chain"]