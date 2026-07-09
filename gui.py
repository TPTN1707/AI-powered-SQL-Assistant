# gui.py

import streamlit as st
import pandas as pd
from sqlalchemy import text
from core.chains import sql_generation_chain, nl_response_chain
from database.connection import db, schema
from security.sql_validator import is_safe_query

st.set_page_config(page_title="AI SQL Assistant", page_icon="🤖", layout="wide")
st.title("🤖 AI-Powered SQL Assistant")

# Input for user question
question = st.text_area("Enter your question about the data:", placeholder="e.g., Show me all products in the database")

if st.button("Generate & Execute SQL", type="primary"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Processing your question..."):
            try:
                # 1. Generate SQL Query
                sql = sql_generation_chain.invoke({"question": question, "schema": schema})
                
                # Split layout into columns for SQL and Final Answer to look cleaner
                col1, col2 = st.columns([1, 1])
                
                with col1:
                    st.subheader("🛠️ Generated SQL Query:")
                    st.code(sql, language="sql")
                
                # 2. Validate SQL Query
                if not is_safe_query(sql):
                    st.error("🚨 WARNING: Generated SQL query is unsafe and was not executed.")
                    st.stop()

                # 3. Execute SQL Query and get structured DataFrame
                # Use SQLAlchemy connection directly with Pandas
                with db._engine.connect() as conn:
                    df = pd.read_sql_query(text(sql), conn)
                
                # Display results as an interactive table
                st.subheader("📊 Query Result:")
                if not df.empty:
                    st.dataframe(df, use_container_width=True, hide_index=True)
                    # Convert dataframe to a clean string format for the LLM to read
                    result_for_llm = df.to_string(index=False)
                else:
                    st.info("Query executed successfully, but returned no rows.")
                    result_for_llm = "No results found."
                
                # 4. Generate and display Natural Language Response
                with col2:
                    final_answer = nl_response_chain.invoke({
                        "question": question,
                        "query": sql,
                        "result": result_for_llm
                    })
                    
                    st.subheader("💬 Final Answer:")
                    st.info(final_answer)

            except Exception as e:
                st.error(f"An error occurred: {e}")

st.markdown("---")
st.caption("Powered by Google Gemini & LangChain")