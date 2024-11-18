import json
import os

def regenerate_array_logs():
    logs_path = os.path.join(os.path.dirname(__file__), '..', 'logs', 'binary_tree_logs.json')
    default_logs = [
    "Node 1",
    "Node 2",
    "Node 3",
    "Node 4",
    "Node 5",
    "Node 6",
    "Node 7"
]
    
    with open(logs_path, 'w') as logfile:
        json.dump(default_logs, logfile, indent=4)
    print("Binary tree logs have been reset to default.")

# Run the function if this script is executed directly
if __name__ == "__main__":
    regenerate_array_logs()
