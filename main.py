def analyze_log(filename):
    """
    This function reads a log file and counts how many times "ERROR" appears.
    """
    error_count = 0
    
    with open(filename, 'r') as file:
        for line in file:
            if "ERROR" in line:
                error_count = error_count + 1
                
    return error_count

# --- The Safety Block ---
if __name__ == "__main__":
    # This code only runs if you type 'python main.py'
    count = analyze_log('server.log')
    print(f"Scan complete. Total errors found: {count}")