"""
Import os library to read files and get the logs, and get the json library to get the list to json format
"""
import os
import json

class Node:
    """
    A class representing a node in a doubly linked list.

    Attributes:
        data: The data stored in the node.
        next: A reference to the next node in the list.
        before: A reference to the previous node in the list.
    """
    def __init__(self, data):
        """
        Initializes a Node with the given data.
        
        Parameters:
        data (any): The data to be stored in the node.
        """
        self.data = data
        self.next = None
        self.before = None

class DoublyLinkedList:
    """
    A class representing a doubly linked list.

    Attributes:
        head: The head node of the doubly linked list.
        tail: The tail node of the doubly linked list.
        logs_path: The file path to store the doubly linked list logs.
    """
    def __init__(self):
        """
        Initializes a DoublyLinkedList with no head and tail, and sets up the path for logs.
        """
        self.head = None
        self.tail = None  # Track the tail of the list for efficient appending
        self.logs_path = os.path.join(os.path.dirname(__file__), '..', 'logs', 'double_linked_list_logs.json')
        self.load_doubly_linked_list()
        
    def load_doubly_linked_list(self):
        """
        Load logs from the json file, and get the content of the file to populate the list.
        """
        if os.path.exists(self.logs_path):
            with open(self.logs_path, 'r') as logfile:
                logs = json.load(logfile)
                for log in logs:
                    self.append(log)
                
    def save_logs(self):
        """
        Save the current state of the list to the file.
        """
        logs = self.to_list()
        with open(self.logs_path, 'w') as logfile:
            json.dump(logs, logfile, indent=4)
            
    def append(self, data):
        """
        Add a new node with the given data to the end of the list.
        
        Parameters:
        data (any): The data to be appended to the list.
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
        
        Parameters:
        index (int): The position at which to insert the new node.
        data (any): The data to be inserted into the new node.
        
        Returns:
        bool: True if insertion is successful, False otherwise.
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
        
        Parameters:
        index (int): The position of the node to be deleted.
        
        Returns:
        bool: True if deletion is successful, False otherwise.
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
        
        Parameters:
        index (int): The position of the node to be updated.
        data (any): The new data to be stored in the node.
        
        Returns:
        bool: True if update is successful, False otherwise.
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
        
        Parameters:
        index (int): The position of the node to be accessed.
        
        Returns:
        any: The data at the specified index if successful, None otherwise.
        """
        current = self.head
        for _ in range(index):
            if current is None:
                return None
            current = current.next
        return current.data if current else None
    
    def to_list(self):
        """
        Convert the doubly linked list into a Python list.

        Returns:
            list: A list containing the data of all nodes in the doubly linked list.
        """
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
    
    def to_list_with_pointers(self):
        """
        Convert the list into a Python list, including pointers to head and tail.
        
        Returns:
        list: A list of dictionaries representing the nodes with pointers to head and tail.
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