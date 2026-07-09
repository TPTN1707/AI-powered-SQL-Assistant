# 🤖 AI-Powered SQL Assistant

An AI-powered SQL assistant that converts natural language questions into secure SQLite queries, executes them, and translates the raw results back into human-friendly, natural language answers. 

This project utilizes **Google Gemini (Gemini 2.5 Flash)**, **LangChain (LCEL)**, **Streamlit** for the web interface, and **Pandas** for structured data visualization.

---

## ✨ Features

- 🔹 **Natural Language to SQL (NL2SQL):** Converts conversational questions into valid SQLite queries.
- 🔹 **Conversational Answers:** Translates raw database tuples into clear, natural language explanations.
- 🔹 **Interactive Web GUI:** A modern, split-layout web interface built with **Streamlit** to display queries and results side-by-side.
- 🔹 **Command-Line Interface (CLI):** Lightweight terminal-based interface (`cli.py`) for quick testing and development.
- 🔹 **SQL Security Guardrails:** Includes a built-in validator (`security/sql_validator.py`) using regular expressions to block destructive SQL commands (e.g., `DROP`, `DELETE`, `UPDATE`) and prevent SQL Injection (stacked queries).
- 🔹 **Interactive Data Tables:** Renders query results as sortable, searchable tables using **Pandas** and Streamlit's native dataframes.

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
│   ├── connection.py               # Handles LLM & SQLDatabase connections
│   └── tools.py                    # Defines database execution tools
│
├── security/                       # SQL Guardrails and validation logic
│   └── sql_validator.py            # Contains logic to validate generated SQL queries
│
├── cli.py                          # Command-Line Interface application
├── gui.py                          # Streamlit Web GUI application
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
User Question
             │
             ▼
    [SQL Generation Chain]
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
     Pandas DataFrame  ──► Display Interactive Table in GUI
             │
             ▼
    [NL Response Chain]
             │
             ▼
  Natural Language Answer
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

## 📌 Current Limitations

- **Single-turn Conversation Only:** Currently, the system does not retain chat history; each query is treated as an independent conversation without contextual memory.
- **SQLite Database Support Only:** The connection is hardcoded to SQLite (requires manual adjustments in `database/connection.py` to support other database engines).
- **Static Configuration:** Database connection strings are loaded from local files instead of allowing dynamic configuration via the user interface.
- **No Automatic Self-Correction:** If a generated SQL query contains syntax errors, the system displays the database error instead of automatically asking the LLM to rewrite and heal the query.

---

## 🚧 Future Improvements

- 🔄 **Multi-turn Chat & Memory:** Integrate conversational history (e.g., using LangGraph or LangChain's message history) to allow contextual follow-up questions (e.g., "Who bought the most?" followed by "What did they buy?").
- 📊 **Dynamic Data Visualization:** Add features to automatically generate interactive charts (bar, line, pie charts) based on the tabular query results.
- 🎛️ **Dynamic DB Configuration:** Allow users to dynamically configure their database connections (PostgreSQL, MySQL, SQLite) directly from the Web UI.
- 🧠 **Self-Correction Loop:** Implement an agentic loop where the LLM automatically reads database execution errors, self-corrects the SQL query, and retries the execution.
- ☁️ **Cloud Deployment:** Package and deploy the Streamlit application to Streamlit Cloud or Hugging Face Spaces for easy sharing and accessibility.

---

## 🛡️ Security Guardrails

To prevent unauthorized database modifications, all generated queries must pass through `security/sql_validator.py` before execution. 

The validator applies the following checks:
1. **Query Type Restriction:** Only queries starting with `SELECT` are permitted.
2. **Keyword Blacklist:** Detects and blocks DML/DDL commands (e.g., `INSERT`, `UPDATE`, `DELETE`, `DROP`, `ALTER`) using whole-word regular expression matching to prevent false positives on columns like `created_at`.
3. **Stacked Query Prevention:** Blocks stacked queries containing semicolons (`;`) to mitigate SQL injection.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Tran Pham Trong Nhan**  
AI Engineer | Machine Learning | Computer Vision | LLM Applications