""" 
Importing os to work with reading files, and to work with json files we use the json module.
Importing the pydot since, this will be used to generate the graphical representation of the binary tree.
Using the flash module from flask to display messages to the user.
In this case, this is not a live object of the binary tree, this generates jpg image of the binary tree each time
there is an operation or a change in the binary the image it is reset again.
"""

import os
import json
from flask import flash
import pydot

class TreeNode:
    """
    A class representing a node in a binary tree.

    Attributes:
        data: The data stored in the node.
        left: A reference to the left child node.
        right: A reference to the right child node.
    """
    def __init__(self, data):
        """
        Initializes a TreeNode with the given data.
        
        Parameters:
        data (any): The data to be stored in the node.
        """
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    """
    A class representing a complete binary tree.

    Attributes:
        root: The root node of the binary tree.
        logs_path: The file path to store the binary tree logs.
        image_path: The file path to store the binary tree image.
    """
    def __init__(self):
        """
        Initializes a BinaryTree with no root and sets up paths for logs and images.
        """
        self.root = None
        self.logs_path = os.path.join(os.path.dirname(__file__), '..', 'logs', 'binary_tree_logs.json')
        self.image_path = os.path.join(os.path.dirname(__file__), '..', 'static', 'img', 'binary_tree.png')
        self.load_logs()

    def load_logs(self):
        """
        Loads the binary tree logs from a file and builds the tree.
        If the logs file does not exist, it creates a default tree and saves the logs.
        """
        if os.path.exists(self.logs_path):
            with open(self.logs_path, 'r') as logfile:
                logs = json.load(logfile)
                self.build_tree(logs)
        else:
            default_logs = ["Node 1", "Node 2", "Node 3", "Node 4", "Node 5", "Node 6", "Node 7"]
            self.build_tree(default_logs)
            self.save_logs()

    def save_logs(self):
        """
        Saves the current state of the binary tree to a logs file.
        """
        logs = self.level_order_traversal()
        with open(self.logs_path, 'w') as logfile:
            json.dump(logs, logfile, indent=4)

    def build_tree(self, data_list):
        """
        Constructs a complete binary tree from a list of data.
        
        Parameters:
        data_list (list): The list of data to build the binary tree.
        """
        if not data_list:
            return

        self.root = TreeNode(data_list[0])
        queue = [self.root]
        index = 1

        while index < len(data_list):
            current = queue.pop(0)

            if index < len(data_list):
                current.left = TreeNode(data_list[index])
                queue.append(current.left)
                index += 1

            if index < len(data_list):
                current.right = TreeNode(data_list[index])
                queue.append(current.right)
                index += 1

        self.generate_tree_image()

    def level_order_traversal(self):
        """
        Returns a level-order traversal of the binary tree as a list.

        Returns:
            A list representing the level-order traversal of the binary tree.
        """
        if not self.root:
            return []

        result = []
        queue = [self.root]

        while queue:
            current = queue.pop(0)
            result.append(current.data)

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return result

    def insert(self, data):
        """
        Inserts a new node to maintain a complete binary tree.
        
        Parameters:
        data (any): The data to be inserted into the binary tree.
        """
        if not self.root:
            self.root = TreeNode(data)
        else:
            queue = [self.root]
            while queue:
                current = queue.pop(0)

                if not current.left:
                    current.left = TreeNode(data)
                    break
                else:
                    queue.append(current.left)

                if not current.right:
                    current.right = TreeNode(data)
                    break
                else:
                    queue.append(current.right)

        self.generate_tree_image()
        self.save_logs()

    def delete(self, data):
        """
        Deletes a node by replacing it with the deepest and rightmost node.
        
        Parameters:
        data (any): The data of the node to be deleted.
        
        Returns:
        bool: True if deletion is successful, False otherwise.
        """
        if not self.root:
            flash("Tree is empty. Cannot delete.", "danger")
            return False

        queue = [self.root]
        node_to_delete = None
        last_node = None
        parent_of_last = None

        while queue:
            current = queue.pop(0)
            if current.data == data:
                node_to_delete = current

            if current.left:
                parent_of_last = current
                queue.append(current.left)

            if current.right:
                parent_of_last = current
                queue.append(current.right)

            last_node = current

        if node_to_delete:
            node_to_delete.data = last_node.data
            if parent_of_last and parent_of_last.right == last_node:
                parent_of_last.right = None
            elif parent_of_last and parent_of_last.left == last_node:
                parent_of_last.left = None
            else:
                self.root = None

            self.generate_tree_image()
            self.save_logs()
            return True
        else:
            flash(f"Log '{data}' not found in the tree for deletion.", "danger")
            return False
        
    def inorder(self):
        """
        Returns an inorder traversal of the binary tree as a list.
        
        Returns:
        list: The list of node values in inorder sequence.
        """
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        """ 
        Perform an in-order traversal of the binary tree recursively.
        
        Args:
            node (TreeNode): The current node in the binary tree.
            result (list): The list that accumulates the node values in in-order sequence.
        
        Returns:
            None: This method updates the result list in place.
        """
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.data)
            self._inorder_recursive(node.right, result)
            
    def preorder(self):
        """
        Returns a preorder traversal of the binary tree as a list.
        
        Returns:
        list: The list of node values in preorder sequence.
        """
        result = []
        self._preorder_recursive(self.root, result)
        return result
    
    def _preorder_recursive(self, node, result):
        """ 
        Perform a pre-order traversal of the binary tree recursively.
        
        Args:
            node (TreeNode): The current node in the binary tree.
            result (list): The list that accumulates the node values in pre-order sequence.
        
        Returns:
            None: This method updates the result list in place.
        """
        if node:
            result.append(node.data)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)
            
    def postorder(self):
        """
        Returns a postorder traversal of the binary tree as a list.
        
        Returns:
        list: The list of node values in postorder sequence.
        """
        result = []
        self._postorder_recursive(self.root, result)
        return result
    
    def _postorder_recursive(self, node, result):
        """ 
        Perform a post-order traversal of the binary tree recursively.
        
        Args:
            node (TreeNode): The current node in the binary tree.
            result (list): The list that accumulates the node values in post-order sequence.
        
        Returns:
            None: This method updates the result list in place.
        """
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.data)

    def generate_tree_image(self):
        """
        Generates a graphical representation of the binary tree and saves it as an image.
        """
        if not os.path.exists(os.path.dirname(self.image_path)):
            os.makedirs(os.path.dirname(self.image_path))

        graph = pydot.Dot(graph_type="graph")
        self._add_nodes_to_graph(self.root, graph)
        graph.write_png(self.image_path)

    def _add_nodes_to_graph(self, node, graph, parent_label=None):
        """
        Recursively adds nodes to the graph for visualization.
        
        Parameters:
        node (TreeNode): The current node in the binary tree.
        graph (pydot.Dot): The graph object to which nodes are added.
        parent_label (str): The label of the parent node.
        """
        if node:
            current_label = str(node.data)
            graph.add_node(pydot.Node(current_label, style="filled", fillcolor="green"))
            if parent_label:
                graph.add_edge(pydot.Edge(parent_label, current_label))
            self._add_nodes_to_graph(node.left, graph, current_label)
            self._add_nodes_to_graph(node.right, graph, current_label)