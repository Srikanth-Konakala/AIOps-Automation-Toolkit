# This file mimics an AI agent (like LangChain)

def ask_ai_for_help(log_line):
    """
    This function pretends to be an AI. 
    It looks at the error and gives a 'smart' suggestion.
    """
    
    # 1. If the log is about the Database
    if "Database" in log_line:
        return {
            "issue": "The database is not responding.",
            "suggested_fix": "Check if the Postgres container is running. Try restarting the DB service."
        }
    
    # 2. If the log is about a Timeout
    elif "Timeout" in log_line:
        return {
            "issue": " The server took too long to reply.",
            "suggested_fix": "Check your internet connection or increase the timeout limit in settings."
        }
    
    # 3. If we don't know what it is
    else:
        return {
            "issue": "Unknown Error",
            "suggested_fix": "Check the system logs manually."
        }