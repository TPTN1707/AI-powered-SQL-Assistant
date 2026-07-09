from langchain_community.tools.sql_database.tool import QuerySQLDatabaseTool
from database.connection import db # Import the database connection

# Initialize database executor tool
db_executor_tool = QuerySQLDatabaseTool(db=db)

__all__ = ["db_executor_tool"]