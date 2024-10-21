import os
import json
from models.stack import Stack
from models.queue import Queue
from models.hash_table import HashTable
from models.binary_tree import BinaryTree
from models.circular_double_link_list import CircularDoubleLinkedList
from models.graph import Graph

class LogProcessor:
    def __init__(self, log_folder="./logs/suricata"):
        self.log_folder = log_folder
        self.stack = Stack()
        self.queue = Queue()
        self.hash_table = HashTable()
        self.binary_tree = BinaryTree()
        self.circular_double_linked_list = CircularDoubleLinkedList()
        self.graph = Graph()

    def load_logs(self):
        """Load logs from the Suricata log folder."""
        logs = []
        try:
            for filename in os.listdir(self.log_folder):
                filepath = os.path.join(self.log_folder, filename)
                if filename.endswith(".json"):
                    with open(filepath, 'r') as file:
                        logs.extend(json.load(file))
            return logs
        except Exception as e:
            print(f"Error loading logs: {e}")
            return logs

    def distribute_logs(self, logs):
        """Distribute logs to the data structures."""
        for log in logs:
            self.stack.push(log)  # Add logs to Stack
            self.queue.enqueue(log)  # Add logs to Queue
            # For Hash Table, we can use a unique key (like timestamp or ID)
            if 'timestamp' in log:
                self.hash_table.insert(log['timestamp'], log)
            # Binary Tree can be based on a specific attribute (e.g., severity)
            if 'severity' in log:
                self.binary_tree.insert(log['severity'])
            # Add logs to Circular Double Linked List
            self.circular_double_linked_list.insert(log)
            # Add logs as nodes in the graph (e.g., IP relationships)
            if 'src_ip' in log and 'dest_ip' in log:
                self.graph.add_node(log['src_ip'])
                self.graph.add_node(log['dest_ip'])
                self.graph.add_edge(log['src_ip'], log['dest_ip'])

    def process_logs(self):
        """Load and process logs."""
        logs = self.load_logs()
        self.distribute_logs(logs)