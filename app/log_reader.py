import os

# Example function to read Suricata logs
def read_suricata_logs():
    log_file = './logs/suricata/eve.json'  # Suricata outputs JSON logs by default
    logs = []
    if os.path.exists(log_file):
        with open(log_file, 'r') as file:
            logs = file.readlines()
            # Process logs if needed (parsing, etc.)
    return logs

# Example function to read Nginx logs
def read_nginx_logs():
    log_file = './logs/nginx/access.log'
    logs = []
    if os.path.exists(log_file):
        with open(log_file, 'r') as file:
            logs = file.readlines()
            # Process logs if needed
    return logs