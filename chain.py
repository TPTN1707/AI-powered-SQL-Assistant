from langchain.chains import create_sql_query_chain

from connect_database import llm, db

chain = create_sql_query_chain(
    llm,
    db
)