import os
import json
from flask import flash
import pydot


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
        self.logs_path = os.path.join(os.path.dirname(__file__), '..', 'logs', 'binary_tree_logs.json')
        self.image_path = os.path.join(os.path.dirname(__file__), '..', 'static', 'img', 'binary_tree.png')
        self.load_logs()

    def load_logs(self):
        if os.path.exists(self.logs_path):
            with open(self.logs_path, 'r') as logfile:
                logs = json.load(logfile)
                self.build_tree(logs)
        else:
            default_logs = ["Node 1", "Node 2", "Node 3", "Node 4", "Node 5", "Node 6", "Node 7"]
            self.build_tree(default_logs)
            self.save_logs()

    def save_logs(self):
        logs = self.level_order_traversal()
        with open(self.logs_path, 'w') as logfile:
            json.dump(logs, logfile, indent=4)

    def build_tree(self, data_list):
        """Constructs a complete binary tree from a list of data."""
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
        """Returns a level-order traversal of the binary tree as a list."""
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
        """Inserts a new node to maintain a complete binary tree."""
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
        """Deletes a node by replacing it with the deepest and rightmost node."""
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

    def generate_tree_image(self):
        """Generate a graphical representation of the binary tree and save it as an image."""
        if not os.path.exists(os.path.dirname(self.image_path)):
            os.makedirs(os.path.dirname(self.image_path))

        graph = pydot.Dot(graph_type="graph")
        self._add_nodes_to_graph(self.root, graph)
        graph.write_png(self.image_path)

    def _add_nodes_to_graph(self, node, graph, parent_label=None):
        if node:
            current_label = str(node.data)
            graph.add_node(pydot.Node(current_label, style="filled", fillcolor="green"))
            if parent_label:
                graph.add_edge(pydot.Edge(parent_label, current_label))
            self._add_nodes_to_graph(node.left, graph, current_label)
            self._add_nodes_to_graph(node.right, graph, current_label)