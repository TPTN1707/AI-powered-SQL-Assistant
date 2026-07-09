from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.utilities import SQLDatabase
import os

load_dotenv()

# Initialize LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0,
)

# Initialize SQLDatabase
db = SQLDatabase.from_uri("sqlite:///data/shop.db")
schema = db.get_table_info()

# Export for easy import
__all__ = ["llm", "db", "schema"]