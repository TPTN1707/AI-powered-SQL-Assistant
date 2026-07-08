# 🤖 AI-Powered SQL Assistant

An AI-powered SQL assistant that converts natural language questions into SQL queries using **Google Gemini** and **LangChain**, then executes them on a **SQLite** database.

This project demonstrates how Large Language Models (LLMs) can bridge the gap between human language and relational databases through **Natural Language to SQL (NL2SQL)**.

---

## ✨ Features

- 🔹 Convert natural language into SQL queries using Google Gemini.
- 🔹 Execute generated SQL against a SQLite database.
- 🔹 Prompt-based SQL generation using LangChain Expression Language (LCEL).
- 🔹 Database schema-aware prompting.
- 🔹 Command-line interface (CLI).
- 🔹 Easy to customize for other databases.

---

## 🏗️ Project Structure

```text
AI-powered-SQL-Assistant/
│
├── app.py                  # Main CLI application
├── chain.py                # LangChain prompt pipeline
├── connect_database.py     # Database & Gemini configuration
├── create_database.py      # Create and seed SQLite database
│
├── data/
│   └── sample.db             # Sample SQLite database
│
├── .env                    # Google AI Studio API Key
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
ChatPromptTemplate
      │
      ▼
Google Gemini
      │
Generate SQL Query
      │
      ▼
SQLite Database
      │
Execute Query
      │
      ▼
Query Result
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

## 🗄️ Sample Database

A sample SQLite database is included for demonstration purposes.

If needed, you can generate the sample database by running:

```bash
uv run create_database.py
```

You can also replace it with your own SQLite database by updating the database connection in `connect_database.py`.

---

## ▶️ Usage

Run the application

```bash
uv run app.py
```

### Example

```text
Ask a question:

List all records from the sample database.
```

Generated SQL

```sql
SELECT *
FROM your_table;
```

Result

```text
[(...)]
```

---

## 📌 Current Limitations

- Supports SQLite only.
- CLI interface only.
- No SQL safety validation.
- No natural language explanation of query results.
- Uses a small sample database.

---

## 🚧 Future Improvements

- Streamlit web interface.
- SQL validation & guardrails.
- Natural language explanation of query results.
- Support PostgreSQL / MySQL.
- Chat history.
- Multi-turn conversation.
- Database connection from user configuration.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Tran Pham Trong Nhan**

AI Engineer | Machine Learning | Computer Vision | LLM Applications