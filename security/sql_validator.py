import re

def is_safe_query(sql_query: str) -> bool:
    """
    Validates if a SQL query is safe to execute.
    Allows only SELECT statements and prevents DML/DDL operations.
    """
    clean_query = sql_query.strip()
    
    # Remove trailing semicolon if it exists at the absolute end of the query
    if clean_query.endswith(";"):
        clean_query = clean_query[:-1].strip()
        
    clean_query_upper = clean_query.upper()

    # Rule 1: Must start with SELECT
    if not clean_query_upper.startswith("SELECT"):
        return False

    # Rule 2: Disallow common DML/DDL keywords as WHOLE words only
    forbidden_keywords = {
        "INSERT", "UPDATE", "DELETE", "DROP", "ALTER", "CREATE",
        "TRUNCATE", "REPLACE", "GRANT", "REVOKE", "COMMIT", "ROLLBACK",
        "MERGE", "CALL", "EXEC", "EXECUTE"
    }
    
    # Extract all uppercase words to avoid partial matching (e.g., 'created_at' containing 'CREATE')
    words = set(re.findall(r'\b[A-Z]+\b', clean_query_upper))
    if not words.isdisjoint(forbidden_keywords):
        return False

    # Rule 3: Block stacked queries (multiple SQL statements separated by remaining semicolons)
    if ";" in clean_query:
        return False

    return True

__all__ = ["is_safe_query"]