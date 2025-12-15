from fastapi import FastAPI
from main import analyze_log
from ai_ops import ask_ai_for_help # <-- Importing our new AI brain!

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "active", "system": "healthy"}

@app.get("/report")
def get_report():
    count = analyze_log('server.log')
    return {"error_count": count, "message": "Analysis Complete"}

# --- NEW AI ENDPOINT ---
@app.get("/ai-analysis")
def ai_analysis():
    # 1. We look at the logs again to find the error
    with open('server.log', 'r') as f:
        log_content = f.read()
    
    # 2. We find the specific line that failed (simulated logic)
    # In a real app, we would loop through all errors. 
    # Here, we grab the first error we see.
    problem_line = "ERROR: Database connection failed" 

    # 3. We ask the AI for help
    ai_response = ask_ai_for_help(problem_line)
    
    return ai_response