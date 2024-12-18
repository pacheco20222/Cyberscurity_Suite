"""
Importing the os and json modules, just like the other structures
we use these libraries to read from files, and put them in a json format.
Just like queue we import datetime to get the current time, and flash so we validate
the user correctly inputs the data.
"""
import os
import json
from datetime import datetime
from flask import flash

class Stack:
    def __init__(self):
        """ 
        Initialize the empty stack, which will be populated
        by reading the stack_logs.json file.
        """
        self.stack = []
        self.logs = os.path.join(os.path.dirname(__file__), '..', 'logs', 'stack_logs.json')
        self.load_stack()
        
    def load_stack(self):
        """ 
        This will get the logs from the stack_logs.json file.
        """
        if os.path.exists(self.logs):  # Check if the path file exists
            with open(self.logs, 'r') as logfile:
                self.stack = json.load(logfile)
    
    def is_empty(self):
        """
        Simply checks if the stack is empty.
        
        Returns:
        bool: True if the stack is empty, False otherwise.
        """
        return len(self.stack) == 0 # If the length of the stack is 0, it is empty return True
    
    def get_stack(self):
        """
        Returns the stack.
        
        Returns:
        list: The current stack.
        """
        return self.stack
    
    def save_stack(self):
        """
        The changes that have been made to the stack will be saved
        to the stack_logs.json file.
        """
        with open(self.logs, 'w') as logfile:
            json.dump(self.stack, logfile, indent=4)
    
    def push(self, log):
        """
        Push the log that the user inputs into the stack.
        
        Parameters:
        log (str): The log entry to be added in the format "username, status".
        
        Returns:
        bool: True if the log entry is successfully added, False otherwise.
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
            return True
        except ValueError:
            flash("Please enter both a valid username and status.", 'danger')
            return False
        
    def pop(self):
        """
        Pop the last element of the stack.
        
        Returns:
        dict: The popped log entry if the stack is not empty, None otherwise.
        """
        if not self.is_empty():
            pop_log = self.stack.pop()
            self.save_stack()
            return pop_log
        flash("The stack is empty.", 'danger')
        return None