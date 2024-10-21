import os
import json
from datetime import datetime

class Queue:
    def __init__(self):
        self.queue = []
        self.log_file = os.path.join(os.path.dirname(__file__), '..', 'logs', 'queue_logs.json')
        self.load_queue()

    def enqueue(self, item):
        # Expecting a string in format: "IP, reason"
        try:
            ip, reason = item.split(',')
            log_entry = {
                "ip": ip.strip(),
                "timestamp": datetime.now().isoformat(),  # Add current timestamp
                "reason": reason.strip()
            }
            self.queue.append(log_entry)
            self.save_queue()  # Save the queue after adding an item
        except ValueError:
            print("Invalid input. Make sure the input is in the format 'IP, reason'.")

    def dequeue(self):
        if not self.is_empty():
            dequeued_item = self.queue.pop(0)  # Remove the first item
            self.save_queue()  # Save the queue after removing an item
            return dequeued_item
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def get_queue(self):
        return self.queue

    def load_queue(self):
        # Load the queue from the log file if it exists
        if os.path.exists(self.log_file):
            with open(self.log_file, 'r') as f:
                self.queue = json.load(f)

    def save_queue(self):
        # Save the queue to the log file
        with open(self.log_file, 'w') as f:
            json.dump(self.queue, f, indent=4)