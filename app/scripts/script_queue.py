import os
import json

# Define the path for the queue logs
logs_path = os.path.join(os.path.dirname(__file__), '..', 'logs', 'queue_logs.json')

# Sample logs to populate the queue
sample_logs = [
    {
        "ip": "192.168.1.15",
        "timestamp": "2024-10-21T10:10:00Z",
        "reason": "blocked IP"
    },
    {
        "ip": "10.0.0.5",
        "timestamp": "2024-10-21T10:15:00Z",
        "reason": "multiple failed attempts"
    },
    {
        "ip": "10.0.0.12",
        "timestamp": "2024-10-21T10:20:00Z",
        "reason": "unrecognized device"
    },
    {
        "ip": "192.168.1.25",
        "timestamp": "2024-10-21T10:25:00Z",
        "reason": "wrong password"
    },
    {
        "ip": "192.168.1.30",
        "timestamp": "2024-10-21T10:30:00Z",
        "reason": "account locked"
    },
    {
        "ip": "192.168.1.35",
        "timestamp": "2024-10-21T10:35:00Z",
        "reason": "blocked IP"
    },
    {
        "ip": "10.0.0.45",
        "timestamp": "2024-10-21T10:40:00Z",
        "reason": "unrecognized device"
    },
    {
        "ip": "10.0.0.50",
        "timestamp": "2024-10-21T10:45:00Z",
        "reason": "multiple failed attempts"
    },
    {
        "ip": "10.182.10.1",
        "timestamp": "2024-10-21T12:31:27.969588",
        "reason": "Pubkey failed"
    },
    {
        "ip": "10.182.220.1",
        "timestamp": "2024-10-23T11:23:27.024761",
        "reason": "Invalid domain"
    },
    {
        "ip": "10.182.12.2",
        "timestamp": "2024-10-23T11:39:50.483206",
        "reason": "DNS Failure"
    },
    {
        "ip": "192.155.18.12",
        "timestamp": "2024-10-23T12:03:26.464184",
        "reason": "DNS Failure"
    },
    {
        "ip": "192.99.99.88",
        "timestamp": "2024-10-24T01:44:32.589635",
        "reason": "Failed Password"
    }
]

# Write the sample logs to the file
with open(logs_path, 'w') as log_file:
    json.dump(sample_logs, log_file, indent=4)

print("Queue logs have been regenerated.")
