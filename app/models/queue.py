from datetime import datetime
import os
import json
import ipaddress
from flask import flash  # Import flash for feedback messages

class Queue:
    def __init__(self):
        # Initialize an empty queue and set the path for the logs
        self.queue = []
        self.logs = os.path.join(os.path.dirname(__file__), '..', 'logs', 'queue_logs.json')
        self.load_queue()  # Load initial data from the file

    def is_empty(self):
        return len(self.queue) == 0
    
    def get_queue(self):
        return self.queue

    def load_queue(self):
        """Load logs from the JSON file into the queue."""
        if os.path.exists(self.logs):
            with open(self.logs, 'r') as log_file:
                self.queue = json.load(log_file)

    def save_queue(self):
        """Save the current queue state back to the JSON file."""
        with open(self.logs, 'w') as log_file:
            json.dump(self.queue, log_file, indent=4)
    
    def enqueue(self, log):
        """
        Add a new log entry to the queue. Validates format "IP, reason".
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
            self.queue.append(new_log)
            self.save_queue()
            flash(f"Log entry for IP '{ip}' with reason '{log_reason}' has been added.", 'success')
            return True

        except ValueError:
            flash("Invalid log format. Please use the correct format: (IP, reason)", 'danger')
            return False

    def dequeue(self):
        """Remove the first log entry from the queue following FIFO."""
        if not self.is_empty():
            first_entry = self.queue.pop(0)
            self.save_queue()
            flash(f"Dequeued log entry for IP '{first_entry['ip']}' with reason '{first_entry['reason']}'", 'success')
            return first_entry
        flash("The queue is empty. Please enqueue a log to proceed.", 'danger')
        return None