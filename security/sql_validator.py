def is_safe_query(sql_query: str) -> bool:
    """
    Validates if a SQL query is safe to execute.
    Currently only allows SELECT statements and disallows common DML/DDL keywords.
    """
    clean_query = sql_query.strip().upper()

    # Rule 1: Must start with SELECT
    if not clean_query.startswith("SELECT"):
        return False

    # Rule 2: Disallow common DML/DDL keywords anywhere in the query
    forbidden_keywords = [
        "INSERT", "UPDATE", "DELETE", "DROP", "ALTER", "CREATE",
        "TRUNCATE", "REPLACE", "GRANT", "REVOKE", "COMMIT", "ROLLBACK",
        "MERGE", "CALL", "EXEC", "EXECUTE"
    ]
    for keyword in forbidden_keywords:
        if keyword in clean_query:
            return False
            
    # Rule 3: Basic check for multiple statements (semicolon outside comments/strings)
    # This is a simple check and might not catch all cases, but good for a start.
    if ";" in clean_query.replace("''", "").replace('""', "")[clean_query.find("SELECT")+6:]: # After initial SELECT
        return False

    return True

__all__ = ["is_safe_query"]