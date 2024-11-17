import json
import os

def regenerate_array_logs():
    logs_path = os.path.join(os.path.dirname(__file__), '..', 'logs', 'binary_tree_logs.json')
    default_logs = [
    "Critical memory leak detected on WebApp1 (Error: Memory usage exceeded 90%)",
    "Data corruption found on Backup Server (Error: Checksum mismatch)",
    "Database replication issue on MySQL (Error: Replication lag over threshold)",
    "Disk failure imminent on File Server (Error: SMART check failure)",
    "High CPU usage on WebApp2 (Warning: CPU usage at 95%)",
    "SSL certificate expired on WebApp1 (Error: Certificate validation failed)",
    "System overload on Load Balancer (Error: Load average exceeded threshold)",
    "Unauthorized root access attempt on Admin Server (Error: Permission denied)",
    "Unexpected shutdown on PostgreSQL Server (Error: Kernel panic)",
    "Unresponsive service detected on API Gateway (Error: Service timeout)"
    ]
    
    with open(logs_path, 'w') as logfile:
        json.dump(default_logs, logfile, indent=4)
    print("Binary tree logs have been reset to default.")

# Run the function if this script is executed directly
if __name__ == "__main__":
    regenerate_array_logs()
