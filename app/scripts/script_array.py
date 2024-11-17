import json
import os

def regenerate_array_logs():
    logs_path = os.path.join(os.path.dirname(__file__), '..', 'logs', 'array_logs.json')
    default_logs = [
        "Log Entry 1 (MySQL Server)",
        "Log Entry 2 (Apache Server)",
        "Log Entry 3 (SSH Server)",
        "Log Entry 5 (Nginx Server)",
        "Log Entry 6 (DNS Server)",
        "Log Entry 7 (MySQL Server)",
        "Log Entry 8 (SSH Server)",
        "Log Entry 9 (Redis Server)",
        "Log Entry 10 (PostgreSQL Server)",
        "Log Entry 11 (Apache Server)",
        "Log Entry 12 (SSH Server)",
        "Log Entry 13 (FTP Server)",
        "Log Entry 14 (MySQL Server)",
        "Log Entry 15 (Redis Server)",
        "Log Entry 16 (Nginx Server)",
        "Log Entry 17 (PostgreSQL Server)",
        "Log Entry 18 (Apache Server)",
        "Log Entry 19 (SSH Server)",
        "Log Entry 20 (MySQL Server)",
        "Log Entry 21 (Surfshark Server)"
    ]
    
    with open(logs_path, 'w') as logfile:
        json.dump(default_logs, logfile, indent=4)
    print("Array logs have been reset to default.")

# Run the function if this script is executed directly
if __name__ == "__main__":
    regenerate_array_logs()
