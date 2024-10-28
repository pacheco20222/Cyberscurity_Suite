import json
import os

# Define the default stack logs
default_logs = [
    {
        "username": "user1",
        "timestamp": "2024-10-21T10:00:00Z",
        "status": "success"
    },
    {
        "username": "user2",
        "timestamp": "2024-10-21T10:05:00Z",
        "status": "failure"
    },
    {
        "username": "user3",
        "timestamp": "2024-10-21T10:10:00Z",
        "status": "failure"
    },
    {
        "username": "user4",
        "timestamp": "2024-10-21T10:15:00Z",
        "status": "success"
    },
    {
        "username": "user5",
        "status": "failure",
        "timestamp": "2024-10-23T11:45:16.718807"
    },
    {
        "username": "user6",
        "status": "success",
        "timestamp": "2024-10-23T12:02:49.003673"
    }
]

# Path to the stack logs file
logs_path = os.path.join(os.path.dirname(__file__), '..', 'logs', 'stack_logs.json')

# Write the default logs to the file
with open(logs_path, 'w') as log_file:
    json.dump(default_logs, log_file, indent=4)
