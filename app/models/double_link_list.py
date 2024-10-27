import os
import json

class Node:
    """
    A Node in a doubly linked list.
    """
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.logs_path = os.path.join(os.path.dirname(__file__), '..', 'logs', 'app_logs.json')
        self.load_logs()

    def load_logs(self):
        """
        Load logs from the JSON file and populate the doubly linked list.
        """
        if os.path.exists(self.logs_path):
            with open(self.logs_path, 'r') as logfile:
                logs = json.load(logfile)
                for log in logs:
                    self.append(log)

    def save_logs(self):
        """
        Save the current state of the doubly linked list to the JSON file.
        """
        logs = self.to_list()
        with open(self.logs_path, 'w') as logfile:
            json.dump(logs, logfile, indent=4)

    def append(self, data):
        """
        Add a new node with the given data to the end of the list.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
        self.save_logs()

    def insert_at(self, index, data):
        """
        Insert a new node at a specific index.
        """
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                if current is None:
                    return False
                current = current.next
            if current is None:
                return False
            new_node.next = current.next
            if current.next:
                current.next.prev = new_node
            current.next = new_node
            new_node.prev = current
        self.save_logs()
        return True

    def delete_at(self, index):
        """
        Delete a node at a specific index.
        """
        if self.head is None:
            return False
        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
        else:
            current = self.head
            for _ in range(index):
                if current is None:
                    return False
                current = current.next
            if current is None or current.prev is None:
                return False
            if current.next:
                current.next.prev = current.prev
            current.prev.next = current.next
        self.save_logs()
        return True

    def update_at(self, index, data):
        """
        Update the data at a specific index.
        """
        current = self.head
        for _ in range(index):
            if current is None:
                return False
            current = current.next
        if current is None:
            return False
        current.data = data
        self.save_logs()
        return True

    def get_at(self, index):
        """
        Access the data at a specific index.
        """
        current = self.head
        for _ in range(index):
            if current is None:
                return None
            current = current.next
        return current.data if current else None

    def clear(self):
        """
        Clear all the nodes in the list.
        """
        self.head = None
        self.save_logs()

    def to_list(self):
        """
        Convert the doubly linked list to a regular Python list.
        """
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
