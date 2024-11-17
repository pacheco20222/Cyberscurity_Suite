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
        logs = [data for data, _ in self.inorder_traversal_with_position()]
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
            flash(f"Insertion Error: {e}", 'danger')

    def _insert_recursive(self, node, data):
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

    def search(self, data):
        """
        Search for a node in the binary tree with validation.
        Returns the position if found, or -1 if not found.
        """
        if not isinstance(data, str):
            flash("Search Error: Data should be a string", 'danger')
            return -1
        return self._search_with_position(self.root, data, 1)

    def _search_with_position(self, node, data, position):
        if node is None:
            return -1
        if node.data == data:
            return position
        elif data < node.data:
            return self._search_with_position(node.left, data, position * 2)
        else:
            return self._search_with_position(node.right, data, position * 2 + 1)

    def delete(self, data):
        """
        Delete a node from the binary tree.
        """
        if not isinstance(data, str):
            flash("Deletion Error: Data should be a string", 'danger')
            return False
        exists = self.search(data) != -1
        self.root = self._delete_recursive(self.root, data)
        self.save_logs()
        return exists

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
        while current.left:
            current = current.left
        return current

    def inorder_traversal_with_position(self):
        result = []
        self._inorder_recursive_with_position(self.root, result, 1)
        return result

    def _inorder_recursive_with_position(self, node, result, position):
        if node:
            self._inorder_recursive_with_position(node.left, result, position * 2)
            result.append((node.data, position))
            self._inorder_recursive_with_position(node.right, result, position * 2 + 1)

    def preorder_traversal_with_position(self):
        result = []
        self._preorder_recursive_with_position(self.root, result, 1)
        return result

    def _preorder_recursive_with_position(self, node, result, position):
        if node:
            result.append((node.data, position))
            self._preorder_recursive_with_position(node.left, result, position * 2)
            self._preorder_recursive_with_position(node.right, result, position * 2 + 1)

    def postorder_traversal_with_position(self):
        result = []
        self._postorder_recursive_with_position(self.root, result, 1)
        return result

    def _postorder_recursive_with_position(self, node, result, position):
        if node:
            self._postorder_recursive_with_position(node.left, result, position * 2)
            self._postorder_recursive_with_position(node.right, result, position * 2 + 1)
            result.append((node.data, position))
