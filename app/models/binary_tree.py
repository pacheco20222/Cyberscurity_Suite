import os
import json
from flask import flash

class TreeNode:
    """
    Node structure for the Binary Tree.
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
        self.logs_path = os.path.join(os.path.dirname(__file__), '..', 'logs', 'binary_tree_logs.json')
        self.default_logs = [
            "Critical memory leak detected on WebApp1 (Error: Memory usage exceeded 90%)",
            "Data corruption found on Backup Server (Error: Checksum mismatch)",
            "Unresponsive service detected on API Gateway (Error: Service timeout)",
            "Disk failure imminent on File Server (Error: SMART check failure)",
            "Unexpected shutdown on PostgreSQL Server (Error: Kernel panic)",
            "SSL certificate expired on WebApp1 (Error: Certificate validation failed)",
            "Database replication issue on MySQL (Error: Replication lag over threshold)",
            "High CPU usage on WebApp2 (Warning: CPU usage at 95%)",
            "Unauthorized root access attempt on Admin Server (Error: Permission denied)",
            "System overload on Load Balancer (Error: Load average exceeded threshold)"
        ]
        self.load_logs()

    def load_logs(self):
        """
        Load logs from JSON file and populate the binary tree. Initialize with default logs if empty.
        """
        if os.path.exists(self.logs_path):
            with open(self.logs_path, 'r') as logfile:
                logs = json.load(logfile)
                if logs:
                    for log in logs:
                        self.insert(log)
                else:
                    for log in self.default_logs:
                        self.insert(log)
        else:
            for log in self.default_logs:
                self.insert(log)
            self.save_logs()

    def save_logs(self):
        logs = self.inorder_traversal()
        with open(self.logs_path, 'w') as logfile:
            json.dump(logs, logfile, indent=4)

    def insert(self, data):
        """
        Insert data into the binary tree with validation.
        """
        try:
            if not isinstance(data, str):
                raise ValueError("Data should be a string.")
            if self.root is None:
                self.root = TreeNode(data)
            else:
                self._insert_recursive(self.root, data)
            self.save_logs()
        except ValueError as e:
            print(f"Insertion Error: {e}")
            flash(f"Insertion Error: {e}", 'danger')

    def _insert_recursive(self, node, data):
        try:
            if data < node.data:
                if node.left is None:
                    node.left = TreeNode(data)
                else:
                    self._insert_recursive(node.left, data)
            else:
                if node.right is None:
                    node.right = TreeNode(data)
                else:
                    self._insert_recursive(node.right, data)
        except TypeError as e:
            print(f"Comparison Error: {e}")
            flash(f"Comparison Error: {e}", 'danger')

    def search(self, data):
        """
        Search for a node in the binary tree with validation.
        Returns the position if found, or -1 if not found.
        """
        try:
            if not isinstance(data, str):
                raise ValueError("Data should be a string.")
            result = self._search_with_position(self.root, data, 1)  # Start at position 1
            return result
        except ValueError as e:
            print(f"Search Error: {e}")
            flash(f"Search Error: {e}", 'danger')
            return -1

    def _search_with_position(self, node, data, position):
        """
        Helper method to search for the data and return the position.
        """
        if node is None:
            return -1
        if node.data == data:
            return position
        elif data < node.data:
            return self._search_with_position(node.left, data, position * 2)  # Left child
        else:
            return self._search_with_position(node.right, data, position * 2 + 1)  # Right child


    def delete(self, data):
        """
        Delete a node from the binary tree with validation.
        """
        try:
            if not isinstance(data, str):
                raise ValueError("Data should be a string.")
            node_exists = self.search(data) != -1
            self.root = self._delete_recursive(self.root, data)
            self.save_logs()
            return node_exists
        except ValueError as e:
            print(f"Deletion Error: {e}")
            flash(f"Deletion Error: {e}", 'danger')
            return False


    def _delete_recursive(self, node, data):
        if node is None:
            return node
        if data < node.data:
            node.left = self._delete_recursive(node.left, data)
        elif data > node.data:
            node.right = self._delete_recursive(node.right, data)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp_val = self._find_min(node.right)
            node.data = temp_val.data
            node.right = self._delete_recursive(node.right, temp_val.data)
        return node

    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def preorder_traversal(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def postorder_traversal(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append(node.data)
            self._inorder_recursive(node.right, result)

    def _preorder_recursive(self, node, result):
        if node is not None:
            result.append(node.data)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def _postorder_recursive(self, node, result):
        if node is not None:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.data)
