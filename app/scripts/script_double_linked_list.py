import json
import os

def regenerate_array_logs():
    logs_path = os.path.join(os.path.dirname(__file__), '..', 'logs', 'double_linked_list_logs.json')
    default_logs = [
        "User login attempt on WebApp1 (Success)",
        "Database connection error on MySQL server (Error: Connection timeout)",
        "File upload on WebApp1 (Success)",
        "User logout on WebApp1 (Success)",
        "Failed API request on WebApp2 (Error: Unauthorized)",
        "Service restart on Apache Server (Info: Restart completed)",
        "Failed login attempt on Admin Portal (Error: Incorrect password)",
        "User password change on WebApp1 (Success)",
        "Data backup completed on Backup Server (Info: Backup successful)",
        "Disk usage warning on File Server (Warning: Disk space low)"
    ]
    
    with open(logs_path, 'w') as logfile:
        json.dump(default_logs, logfile, indent=4)
    print("Linked List logs have been reset to default.")

# Run the function if this script is executed directly
if __name__ == "__main__":
    regenerate_array_logs()