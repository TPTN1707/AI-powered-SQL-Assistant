from core.chains import sql_generation_chain, nl_response_chain
from database.connection import db, schema
from database.tools import db_executor_tool
from security.sql_validator import is_safe_query

def main():
    print("🤖 AI-Powered SQL Assistant (CLI)")
    question = input("Ask a question: ")

    if not question.strip():
        print("Question cannot be empty.")
        return

    try:
        # 1. Generate SQL Query
        print("\nGenerating SQL...")
        sql = sql_generation_chain.invoke(
            {
                "question": question,
                "schema": schema,
            }
        )
        
        print("\nGenerated SQL:")
        print(sql)

        # 2. Validate SQL Query
        if not is_safe_query(sql):
            print("\n🚨 WARNING: Generated SQL query is unsafe and will not be executed.")
            return

        # 3. Execute SQL Query
        print("\nExecuting SQL...\n")
        result = db_executor_tool.invoke(sql)
        
        print("\nRaw Query Result:")
        print(result)

        # 4. Generate Natural Language Response
        print("\nGenerating Natural Language Response...")
        final_answer = nl_response_chain.invoke({
            "question": question,
            "query": sql,
            "result": result
        })

        print("\nFinal Answer:")
        print(final_answer)

    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()