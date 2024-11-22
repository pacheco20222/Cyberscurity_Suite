""" 
We import os as always to be able to read files, and get the file path, and json to use the json format and organize the logs in the json format.
For the queue we also import ipaddress to simply validate the correct format of the IP the user inputs.
We also import datetime so when the log is generated it uses the current datetime.
We also import flash from flask, since it can be very common for the user to incorrectly input the wrong IP address format.
"""
import os
import json
import ipaddress
from datetime import datetime
from flask import flash

class Queue:
    """
    A class representing a queue data structure.

    Attributes:
        queue (list): The list to store queue elements.
        logs (str): The file path to store the queue logs.
    """
    def __init__(self):
        """Initializes an empty queue and sets up the path for logs."""
        self.queue = []
        self.logs = os.path.join(os.path.dirname(__file__), '..', 'logs', 'queue_logs.json')
        self.load_queue()
    
    def is_empty(self):
        """
        Check if the queue is empty.
        
        Returns:
        bool: True if the queue is empty, False otherwise.
        """
        return len(self.queue) == 0
    
    def get_queue(self):
        """
        Get the current state of the queue.
        
        Returns:
        list: The current queue.
        """
        return self.queue
    
    def load_queue(self):
        """Read the json file and populate the queue with the logs."""
        if os.path.exists(self.logs):
            with open(self.logs, 'r') as logfile:
                self.queue = json.load(logfile)
                
    def save_queue(self):
        """Save the current queue to the logfile in case the user has made changes to the queue."""
        with open(self.logs, 'w') as log_file:
            json.dump(self.queue, log_file, indent=4)
            
    def enqueue(self, log):
        """
        Add a new log entry to the queue. Before adding it, we check the input format, we use split
        to make sure the user separates them with a comma, also we validate the correct format
        of the IP address, 0.0.0.0.
        
        Parameters:
        log (str): The log entry to be added in the format "IP, reason".
        
        Returns:
        bool: True if the log entry is successfully added, False otherwise.
        """
        try:
            ip, log_reason = log.split(',')
            ip = ip.strip()
            log_reason = log_reason.strip()

            # Validate IP format
            try:
                ipaddress.ip_address(ip)
            except ValueError:
                flash("Invalid IP address format. Please use the correct format: (0.0.0.0)", 'danger')
                return False

            # Check for blank IP and reason
            if not ip or not log_reason:
                flash("Please enter both a valid IP and reason.", 'danger')
                return False

            # Create the new log entry and add to queue
            new_log = {
                "ip": ip,
                "timestamp": datetime.now().isoformat(),
                "reason": log_reason
            }
            self.queue.append(new_log)  # Add element to the end of the queue following FIFO
            self.save_queue()
            flash(f"Log entry for IP '{ip}' with reason '{log_reason}' has been added.", 'success')
            return True

        except ValueError:
            flash("Invalid log format. Please use the correct format: (IP, reason)", 'danger')
            return False

    def dequeue(self):
        """
        Remove the first log entry from the queue following FIFO.
        
        Returns:
        dict: The dequeued log entry if the queue is not empty, None otherwise.
        """
        if not self.is_empty():
            first_entry = self.queue.pop(0)
            self.save_queue()
            flash(f"Dequeued log entry for IP '{first_entry['ip']}' with reason '{first_entry['reason']}'", 'success')
            return first_entry
        flash("The queue is empty. Please enqueue a log to proceed.", 'danger')
        return None