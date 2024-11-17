"""
Import os library to read files and get the logs, and get the json library to get the list to json format
"""
import os
import json

class Node:
    """Define the head, tail of the doubly linked list"""
    def __init__(self, data):
        self.data = data
        self.tail = None
        self.head = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  # Track the tail of the list for efficient appending
        self.logs_path = os.path.join(os.path.dirname(__file__), '..', 'logs', 'double_linked_list_logs.json')
        self.load_logs()
        
    def load_doubly_linked_list(self):
        """
        Load logs from the json file, and get the content of the file to populate the list 
        """
        if os.path.exists(self.logs_path):
            with open(self.logs_path, 'r') as logfile:
                logs = json.load(logfile)
                
    def save_logs(self):
        """
        Save the current state of the list to the file.
        """
        logs = self.to_list()
        with open(self.logs_path, 'w') as logfile:
            json.dump(logs, logfile, indent=4)
            
    def append(self, data):
        """
        Add a new node with the given data to the end of the list, we do the usual validation for a linked list
        validating the head.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.before = self.tail
            self.tail = new_node
        self.save_logs()
        
    def insert_at_index(self, index, data):
        """
        Insert a new node at a specific index.
        """
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            if self.head:
                self.head.before = new_node
            self.head = new_node
            if self.tail is None:  # If the list was empty
                self.tail = new_node
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
                current.next.before = new_node
            current.next = new_node
            new_node.before = current
            if new_node.next is None:  # If inserted at the end
                self.tail = new_node
        self.save_logs()
        return True
    
    def delete_at_index(self, index):
        """
        Delete a node at a specific index.
        """
        if self.head is None:
            return False
        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.before = None
            else:
                self.tail = None  # List is now empty
        else:
            current = self.head
            for _ in range(index):
                if current is None:
                    return False
                current = current.next
            if current is None:
                return False
            if current.before:
                current.before.next = current.next
            if current.next:
                current.next.before = current.before
            if current == self.tail:  # If deleting the last element
                self.tail = current.before
        self.save_logs()
        return True

    def update_at_index(self, index, data):
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
    
    def get_log(self, index):
        """
        Access the data at a specific index.
        """
        current = self.head
        for _ in range(index):
            if current is None:
                return None
            current = current.next
        return current.data if current else None
    
    def to_list_with_pointers(self):
        """
        Convert the list into a Python list, this is just to give the visual to the user of the head and the tail in the list.
        """
        result = []
        current = self.head
        while current:
            node_info = {
                "data": current.data,
                "is_head": current == self.head,
                "is_tail": current == self.tail
            }
            result.append(node_info)
            current = current.next
        return result