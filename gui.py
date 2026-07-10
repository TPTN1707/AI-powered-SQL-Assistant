import streamlit as st
import pandas as pd
from sqlalchemy import text
from core.chains import sql_generation_chain, nl_response_chain
from database.connection import db, schema
from security.sql_validator import is_safe_query

st.set_page_config(page_title="AI SQL Assistant", page_icon="🤖", layout="wide")
st.title("🤖 AI-Powered SQL Assistant")

# Initialize Chat History in Session State if not present
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  # List of dicts: {"question": ..., "answer": ...}

# Sidebar to clear history
st.sidebar.header("⚙️ Chat Settings")
if st.sidebar.button("Clear Chat History"):
    st.session_state.chat_history = []
    st.sidebar.success("Chat history cleared!")

# Helper function to format recent chat history for the prompt context
def format_chat_history():
    formatted_history = ""
    # We only pass the last 5 turns to maintain contextual focus and save token limits
    for turn in st.session_state.chat_history[-5:]:
        formatted_history += f"User: {turn['question']}\nAI Response: {turn['answer']}\n\n"
    return formatted_history if formatted_history else "No previous history."

# Input for user question
question = st.text_input("Ask a question about your database:", placeholder="e.g., Who is our top customer?")

if st.button("Submit", type="primary"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Processing..."):
            try:
                chat_history_str = format_chat_history()
                error_feedback = ""
                sql = ""
                df = pd.DataFrame()
                max_attempts = 2  # 1 initial attempt + 1 self-correction attempt
                
                for attempt in range(max_attempts):
                    try:
                        # 1. Generate SQL Query (includes chat history and potential error feedback)
                        sql = sql_generation_chain.invoke({
                            "question": question,
                            "schema": schema,
                            "chat_history": chat_history_str,
                            "error_feedback": error_feedback
                        })
                        
                        # 2. Validate SQL Query
                        if not is_safe_query(sql):
                            st.error("🚨 WARNING: Generated SQL query was flagged as unsafe and was blocked.")
                            st.stop()

                        # 3. Execute SQL Query against SQLite
                        with db._engine.connect() as conn:
                            df = pd.read_sql_query(text(sql), conn)
                        
                        # If successful, exit the self-correction retry loop
                        break
                        
                    except Exception as execution_error:
                        # If the first attempt failed, prepare error feedback and retry
                        if attempt == 0:
                            error_feedback = (
                                f"--- PREVIOUS ATTEMPT FAILED ---\n"
                                f"You generated this query: {sql}\n"
                                f"It failed with the following database error: {str(execution_error)}\n"
                                f"Please analyze the error, rewrite the SQL query, and ensure it uses correct SQLite syntax."
                            )
                            continue
                        else:
                            # If the self-corrected query fails as well, bubble up the error
                            raise execution_error

                # 4. Display Results (Columns layout)
                col1, col2 = st.columns([1, 1])
                
                with col1:
                    st.subheader("🛠️ Executed SQL Query:")
                    st.code(sql, language="sql")
                    
                    st.subheader("📊 Query Result:")
                    if not df.empty:
                        st.dataframe(df, width="stretch", hide_index=True)
                        
                        # Convert dataframe to CSV format for download
                        csv_data = df.to_csv(index=False).encode('utf-8')
                        st.download_button(
                            label="📥 Download Results as CSV",
                            data=csv_data,
                            file_name="query_results.csv",
                            mime="text/csv"
                        )

                        result = df.to_string(index=False)
                    else:
                        st.info("Query returned no rows.")
                        result_for_llm = "No results found."

                # 5. Generate Natural Language Response
                with col2:
                    final_answer = nl_response_chain.invoke({
                        "question": question,
                        "query": sql,
                        "result": result_for_llm
                    })
                    st.subheader("💬 Answer:")
                    st.info(final_answer)
                    
                    # Store current Q&A turn into the chat history state
                    st.session_state.chat_history.append({
                        "question": question,
                        "answer": final_answer
                    })

            except Exception as e:
                st.error(f"An error occurred while executing the query: {e}")

# Render Chat Log at the bottom of the page
if st.session_state.chat_history:
    st.markdown("---")
    st.subheader("📜 Recent Conversation History")
    # Display newest conversations on top
    for turn in reversed(st.session_state.chat_history):
        with st.chat_message("user"):
            st.write(turn["question"])
        with st.chat_message("assistant"):
            st.write(turn["answer"])