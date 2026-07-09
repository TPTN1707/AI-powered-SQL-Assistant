# gui.py

import streamlit as st
from core.chains import sql_generation_chain, nl_response_chain
from database.connection import db, schema
from database.tools import db_executor_tool
from security.sql_validator import is_safe_query

st.set_page_config(page_title="AI SQL Assistant", page_icon="🤖")
st.title("🤖 AI-Powered SQL Assistant")

# Input for user question
question = st.text_area("Enter your question about the data:")

if st.button("Generate & Execute SQL"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Processing your question..."):
            try:
                # 1. Generate SQL Query
                sql = sql_generation_chain.invoke({"question": question, "schema": schema})
                
                st.subheader("🛠️ Generated SQL Query:")
                st.code(sql, language="sql")
                
                # 2. Validate SQL Query
                if not is_safe_query(sql):
                    st.error("🚨 WARNING: Generated SQL query is unsafe and was not executed.")
                    return

                # 3. Execute SQL Query
                result = db_executor_tool.invoke(sql)
                
                st.subheader("📊 Raw Query Result:")
                if result:
                    st.write(result)
                else:
                    st.info("No results found or query did not return data.")
                
                # 4. Generate Natural Language Response
                final_answer = nl_response_chain.invoke({
                    "question": question,
                    "query": sql,
                    "result": result
                })
                
                st.subheader("💬 Final Answer:")
                st.markdown(final_answer) # Use markdown to render potential formatting

            except Exception as e:
                st.error(f"An error occurred: {e}")

st.markdown("---")
st.caption("Powered by Google Gemini & LangChain")