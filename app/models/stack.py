import os
import json
from datetime import datetime

class Stack:
    def __init__(self):
        """
        Just like queue, I will start with a empty stack, which will be populated by the file logs
        """
        self.stack = []
        self.logs = os.path.join(os.path.dirname(__file__), '..', 'logs', 'stack_logs.json')
        self.load_stack() # Calling the function to load the stack with the logs
        
    def load_stack(self):
        """
        This method is to get the logs from the /app/logs/stack_logs.json file
        """
        # Check the path that I have already defined
        if os.path.exists(self.logs):
            """
            I will open the file and read the logs from the file"""
            with open(self.logs, 'r') as log_file:
                self.stack = json.load(log_file)
                
    def is_empty(self):
        return len(self.stack) == 0 # Check if the stack is empty
    
    def get_stack(self):
        # This is to display the stack
        return self.stack
    
    def save_stack(self):
        """
        This method is to save the logs to the /app/logs/stack_logs.json file
        """
        # Check the path that I have already defined
        with open(self.logs, 'w') as log_file:
            json.dump(self.stack, log_file, indent=4)
    
    def push(self, log):
        # In this case we will validate the user uses correct format for this logs "username, status"
        try:
            username, status = log.split(',') # Split the log into username and status seperated by a comma
            username = username.strip() # Remove any white spaces from the username
            status = status.strip() # Remove any white spaces from the status
            
            """
            if their is blank username or status, I will return False and print an error
            """
            if username == '' or status == '':
                print("Please enter a valid username and status")
                return False
            
            """
            I will append the log to the stack
            """
            new_log = {
                "username": username,
                "status": status,
                "timestamp" : datetime.now().isoformat()
            }
            self.stack.append(new_log)
            self.save_stack() # Save the stack to the file
            return True # Return True if the log is successfully added to the stack
        except ValueError:
            print("Invalid log format. Please use the correct format: (username, status)")
            return False # Return False if the log is not successfully added to the stack
        
    def pop(self):
        # I will check if the stack is empty
        if not self.is_empty():
            pop_item = self.stack.pop() # Pop the last item from the stack
            self.save_stack()
            return pop_item
        return None