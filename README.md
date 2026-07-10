# 🤖 AI-Powered SQL Assistant

An AI-powered SQL assistant that converts natural language questions into secure SQLite queries, executes them, and translates the raw results back into human-friendly, natural language answers. 

This project utilizes **Google Gemini (Gemini 2.5 Flash)**, **LangChain (LCEL)**, **Streamlit** for the web interface, and **Pandas** for structured data visualization.

---

## ✨ Features

- 🔹 **Natural Language to SQL (NL2SQL):** Converts conversational questions into valid SQLite queries.
- 🔹 **Multi-turn Conversation (Chat History):** Retains context of the last 5 Q&A turns, enabling follow-up questions (e.g., "Who bought the most?" followed by "What did they buy?").
- 🔹 **Self-Correction Loop:** Automatically detects database execution errors, feeds the error details back to Gemini, and self-corrects the query syntax in real-time (up to 2 attempts).
- 🔹 **Database Schema Explorer:** Features an interactive tree view in the sidebar using SQLAlchemy's inspector to display tables, column names, data types, and primary keys (`🔑`).
- 🔹 **Conversational Answers:** Translates raw database tuples into clear, natural language explanations.
- 🔹 **Interactive Web GUI:** A modern, split-layout web interface built with **Streamlit** to display queries and results side-by-side.
- 🔹 **SQL Security Guardrails:** Includes a built-in validator (`security/sql_validator.py`) using regular expressions to block destructive SQL commands (e.g., `DROP`, `DELETE`, `UPDATE`) and prevent SQL Injection (stacked queries).
- 🔹 **Export Results to CSV:** Provides a quick-download button under query results to instantly export tabular data as `.csv` files.

---

## 🏗️ Project Structure

```text
AI-powered-SQL-Assistant/
│
├── core/                           # Core LangChain components & LLM logic
│   ├── chains.py                   # Defines LangChain chains (SQL generation, NL response)
│   └── prompts.py                  # Stores all ChatPromptTemplate instances
│
├── database/                       # Database connection & utilities
│   └── connection.py               # Handles LLM & SQLDatabase connections
│
├── security/                       # SQL Guardrails and validation logic
│   └── sql_validator.py            # Contains logic to validate generated SQL queries
│
├── gui.py                          # Streamlit Web GUI application (Main Entry Point)
├── create_database.py              # Creates and seeds the sample SQLite database
│
├── data/
│   └── shop.db                     # SQLite database file
│
├── .env                            # Environment variables (Google API Key)
├── pyproject.toml
├── uv.lock
└── README.md
```

---

## ⚙️ Tech Stack

- **Python**
- **Google Gemini API**
- **LangChain**
- **SQLite**
- **SQLAlchemy**
- **python-dotenv**
- **uv**

---

## 🚀 How It Works

```text
User Question + Chat History Context
                        │
                        ▼
             [SQL Generation Chain] ◄─── (If SQL fails, self-corrects with error feedback)
                        │
                        ▼
               Generated SQL Query
                        │
       [SQL Validator] ──(Unsafe Query)──► Stop Execution (Error Alert)
                        │
                  (Safe Query)
                        │
                        ▼
              [SQLite Database]
                        │
                        ▼
              Pandas DataFrame ──► Display Interactive Table & CSV Download Button
                        │
                        ▼
             [NL Response Chain]
                        │
                        ▼
             Natural Language Answer (Saved to Chat History)
```

---

## 📦 Installation

Clone the repository

```bash
git clone https://github.com/TPTN1707/AI-powered-SQL-Assistant.git

cd AI-powered-SQL-Assistant
```

Install dependencies

```bash
uv sync
```

---

## 🔑 Environment Variables

Create a `.env` file.

```env
GOOGLE_API_KEY=your_google_ai_studio_api_key
```

You can obtain your API key from Google AI Studio.

---

## 🛡️ Security Guardrails

To prevent unauthorized database modifications, all generated queries must pass through `security/sql_validator.py` before execution. 

The validator applies the following checks:
1. **Query Type Restriction:** Only queries starting with `SELECT` are permitted.
2. **Keyword Blacklist:** Detects and blocks DML/DDL commands (e.g., `INSERT`, `UPDATE`, `DELETE`, `DROP`, `ALTER`) using whole-word regular expression matching to prevent false positives on columns like `created_at`.
3. **Stacked Query Prevention:** Blocks stacked queries containing semicolons (`;`) to mitigate SQL injection.

---

## 📌 Current Limitations

- **SQLite Database Support Only:** The connection is currently hardcoded to SQLite (requires manual adjustments in `database/connection.py` to support other database engines).
- **Local DB File Only:** Database connection settings are static and loaded locally on-disk.

---

## 🚧 Future Improvements

- 🎛️ **Multi-Database Switcher (SQLite):** Add a dropdown list on the sidebar to scan the `data/` folder and dynamically switch between different `.db` and `.sqlite` files.
- 📊 **Dynamic Data Visualization:** Add features to automatically generate interactive charts (bar, line, pie charts) using libraries like Plotly or Streamlit charts based on the query results.
- ☁️ **Cloud Deployment:** Package and deploy the Streamlit application to Streamlit Cloud or Hugging Face Spaces for easy sharing and accessibility.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Tran Pham Trong Nhan**  
AI Engineer | Machine Learning | Computer Vision | LLM Applications