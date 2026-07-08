from chain import chain
from connect_database import db

from langchain_community.tools.sql_database.tool import QuerySQLDatabaseTool

executor = QuerySQLDatabaseTool(db=db)

question = input("Ask a question: ")

sql = chain.invoke(
    {
        "question": question
    }
)

print("\nGenerated SQL:")
print(sql)

print("\nExecuting...\n")

result = executor.invoke(sql)

print(result)