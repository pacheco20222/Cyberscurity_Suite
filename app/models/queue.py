# I am usign datetime to get the current time since the logs will be queued in the current time
from datetime import datetime
import os
import json
import ipaddress

class Queue:
    def __init__(self):
        # I will start with a empty queue, since I will read the logs and put them in the queue
        self.queue = []
        """
        I use os.path.join to join the path of the current file and the path of the logs folder
        Since is this specific project I have the root folder and insie
        I have the app folder and this file is inside the models folder, I need to go back one folder
        to the logs folder
        """
        self.logs = os.path.join(os.path.dirname(__file__), '..', 'logs', 'queue_logs.json')
        
        self.load_queue() # Calling the function to load the queue with the logs
        
    def is_empty(self):
        return len(self.queue) == 0
    
    def get_queue(self):
        return self.queue
    
    def load_queue(self):
        """
        This method is to get the logs from the /app/logs/queue_logs.json file
        """
        # Check the path that I have already defined
        if os.path.exists(self.logs):
            """
            I will open the file and read the logs from the file"""
            with open(self.logs, 'r') as log_file:
                self.queue = json.load(log_file)
    
    def save_queue(self):
        """
        This method is to save the logs to the /app/logs/queue_logs.json file
        """
        # Check the path that I have already defined
        with open(self.logs, 'w') as log_file:
            json.dump(self.queue, log_file, indent=4) # The indent is to make the file more readable
    
    def enqueue(self, log):
        # I will validate the user uses correct format for the log "IP, reason"
        try:
            ip, log_reason = log.split(',') # Split the log into IP and reason seperated by a comma
            ip = ip.strip() # Remove any white spaces from the IP
            log_reason = log_reason.strip() # Remove any white spaces from the reason
            
            """
            Now I am going to use the ipaddress module to validate the IP address format: 0.0.0.0
            """
            try:
                ipaddress.ip_address(ip) # In the case of a wrong ip I will raise a ValueError
            except ValueError:
                print("Invalid IP address format. Please use the correct format: (0.0.0.0)")
                return False
            
            """
            Now I will use if to check for blank IP and reason
            """
            if ip == '' or log_reason == '':
                print("Please enter a valid IP and reason")
                return False
            
            """
            Now I will append the log to the queue
            """
            
            new_log = {
                "ip": ip,
                "timestamp" : datetime.now().isoformat(),
                "reason": log_reason
            }
            
            self.queue.append(new_log) # Append the new log to the queue
            self.save_queue() # Save the queue to the file
            return True # Return True if the log was successfully added to the queue
        except ValueError:
            print("Invalid log format. Please use the correct format: (IP, reason)")
            return False
        """
        Now I will use and exception to catch any errors that might occur
        """
    
    def dequeue(self):
        # I will use the is_empty function I created to check is the queue is empty
        if not self.is_empty():
            take_out_first = self.queue.pop(0) # pop the first one to have enter FIFO logic from queues
            self.save_queue()
            return take_out_first
        return None