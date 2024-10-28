import os
import json
from datetime import datetime
from flask import flash

class Stack:
    def __init__(self):
        """
        Initialize an empty stack and load logs from the stack logs file.
        """
        self.stack = []
        self.logs = os.path.join(os.path.dirname(__file__), '..', 'logs', 'stack_logs.json')
        self.load_stack()

    def load_stack(self):
        """
        Load logs from the stack logs file.
        """
        if os.path.exists(self.logs):
            with open(self.logs, 'r') as log_file:
                self.stack = json.load(log_file)

    def is_empty(self):
        """
        Check if the stack is empty.
        """
        return len(self.stack) == 0

    def get_stack(self):
        """
        Return the current stack.
        """
        return self.stack

    def save_stack(self):
        """
        Save the current stack to the stack logs file.
        """
        with open(self.logs, 'w') as log_file:
            json.dump(self.stack, log_file, indent=4)

    def push(self, log):
        """
        Push a new log to the stack. Validates input format "username, status".
        """
        try:
            username, status = log.split(',')
            username = username.strip()
            status = status.strip()

            if username == '' or status == '':
                flash("Please enter both a valid username and status.", 'danger')
                return False

            new_log = {
                "username": username,
                "status": status,
                "timestamp": datetime.now().isoformat()
            }
            self.stack.append(new_log)
            self.save_stack()
            flash(f"Log for user '{username}' with status '{status}' has been added.", 'success')
            return True
        except ValueError:
            flash("Invalid log format. Please use the correct format: (username, status)", 'danger')
            return False

    def pop(self):
        """
        Pop the last log from the stack if not empty. 
        Provide feedback if the stack is empty.
        """
        if not self.is_empty():
            pop_item = self.stack.pop()
            self.save_stack()
            flash(f"Popped log: {pop_item['username']} with status '{pop_item['status']}'", 'success')
            return pop_item
        flash("Stack is empty, nothing to pop.", 'warning')
        return None
