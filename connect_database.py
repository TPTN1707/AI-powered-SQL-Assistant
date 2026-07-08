from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.utilities import SQLDatabase
import os

load_dotenv()



llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0,
)

db = SQLDatabase.from_uri("sqlite:///data/shop.db")

print(db.get_usable_table_names())