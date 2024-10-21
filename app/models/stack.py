import json
import os
from datetime import datetime

class Stack:
    def __init__(self):
        self.stack = []
        self.log_file = os.path.join(os.path.dirname(__file__), '..', 'logs', 'stack_logs.json')
        self.load_stack()

    def load_stack(self):
        # Load stack data from the JSON log file
        if os.path.exists(self.log_file):
            with open(self.log_file, 'r') as file:
                self.stack = json.load(file)

    def push(self, item):
        # Expecting a string in format: "username, status"
        try:
            username, status = item.split(',')
            log_entry = {
                "username": username.strip(),
                "status": status.strip(),
                "timestamp": datetime.now().isoformat()  # Add current timestamp
            }
            self.stack.append(log_entry)
            self.save_stack()
        except ValueError:
            print("Invalid input. Make sure the input is in the format 'username, status'.")

    def pop(self):
        # Remove the most recent login attempt and save the changes
        if not self.is_empty():
            popped_item = self.stack.pop()
            self.save_stack()
            return popped_item
        return None

    def peek(self):
        # View the most recent login attempt
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def get_stack(self):
        # Return the current stack for display
        return self.stack

    def save_stack(self):
        # Save the stack to the log file
        with open(self.log_file, 'w') as file:
            json.dump(self.stack, file, indent=4)