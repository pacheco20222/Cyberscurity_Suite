from flask import Blueprint, render_template, request, redirect, url_for
from .models.hash_table import HashTable
from .models.stack import Stack
from .models.queue import Queue
from .models.sorting import Sorting
from .models.array import Array
from .models.binary_tree import BinaryTree
from .models.circular_double_link_list import CircularDoubleLinkedList
from .models.graph import Graph

main = Blueprint('main', __name__)
hash_table_instance = HashTable()
stack_instance = Stack()
queue_instance = Queue()
sorting_instance = Sorting()
array_instance = Array()
binary_tree_instance = BinaryTree()
circular_double_linked_list_instance = CircularDoubleLinkedList()
graph_instance = Graph()

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/array', methods=['GET', 'POST'])
def array():
    current = array_instance.get_array()
    message = "Array is empty for now"
    
    if request.method == 'POST':
        operation = request.form.get('operation')

        if operation == 'insert':
            index = int(request.form.get('index'))
            item = request.form.get('value')
            if array_instance.insert(index, item):
                message = f"Item {item} inserted at index {index}"
            else:
                message = "Invalid index. Please try again."
        
        elif operation == 'delete':
            index = int(request.form.get('index'))
            if array_instance.delete(index):
                message = f"Item deleted from index {index}"
            else:
                message = "Invalid index. Please try again."
        
        elif operation == 'access':
            index = int(request.form.get('index'))
            item = array_instance.access(index)
            if item is not None:
                message = f"Item at index {index} is {item}"
            else:
                message = "Invalid index. Please try again."
        
        elif operation == 'update':
            index = int(request.form.get('index'))
            item = request.form.get('value')
            if array_instance.update(index, item):
                message = f"Item at index {index} updated to {item}"
            else:
                message = "Invalid index. Please try again."
        
        return redirect(url_for('main.array', message=message))
    
    return render_template('array.html', array=current, message=message)

@main.route('/stack', methods=['GET', 'POST'])
def stack():
    if request.method == 'POST':
        push_item = request.form.get('push_item')  # Use the input from the form
        if push_item:
            stack_instance.push(push_item)  # Pass the string directly to the stack instance
        return redirect(url_for('main.stack'))

    return render_template('stack.html', stack=stack_instance.get_stack())


@main.route('/stack/pop', methods=['POST'])
def pop_stack():
    stack_instance.pop()
    return redirect(url_for('main.stack'))


@main.route('/queue', methods=['GET', 'POST'])
def queue():
    if request.method == 'POST':
        item = request.form.get('enqueue_item')
        if item:
            queue_instance.enqueue(item)
        return redirect(url_for('main.queue'))

    return render_template('queue.html', queue=queue_instance.get_queue())

@main.route('/queue/dequeue', methods=['POST'])
def dequeue_queue():
    queue_instance.dequeue()
    return redirect(url_for('main.queue'))

@main.route('/hash_table', methods=['GET', 'POST'])
def hash_table():
    if request.method == 'POST':
        key = request.form.get('key')
        value = request.form.get('value')
        if key and value:
            hash_table_instance.insert(key, value)
        return redirect(url_for('main.hash_table'))
    return render_template('hash_table.html', table=hash_table_instance.get_table(), enumerate=enumerate)

@main.route('/hash_table/delete', methods=['POST'])
def delete_from_hashtable():
    key = request.form.get('key_delete')
    hash_table_instance.delete(key)
    return redirect(url_for('main.hash_table'))

@main.route('/hash_table/search', methods=['POST'])
def search_in_hashtable():
    key = request.form.get('search_key')
    value = hash_table_instance.search(key)
    return render_template('hash_table.html', table=hash_table_instance.get_table(), search_key=key, search_result=value)

@main.route('/binary_tree', methods=['GET', 'POST'])
def binary_tree():
    current_tree = binary_tree_instance.get_inorder()
    message = ""
    
    if request.method == 'POST':
        operation = request.form.get('operation')

        if operation == 'insert':
            value = int(request.form.get('value'))
            binary_tree_instance.insert(value)
            message = f"Inserted {value} into the tree."
        
        elif operation == 'delete':
            value = int(request.form.get('value'))
            binary_tree_instance.delete(value)
            message = f"Deleted {value} from the tree."
        
        elif operation == 'search':
            value = int(request.form.get('value'))
            found = binary_tree_instance.search(value)
            message = f"Value {value} {'found' if found else 'not found'} in the tree."
        
        return redirect(url_for('main.binary_tree', message=message))

    return render_template('binary_tree.html', tree=current_tree, message=message)

@main.route('/sorting', methods=['GET', 'POST'])
def sorting():
    sorted_list = None  # Initialize sorted_list as None for GET request
    if request.method == 'POST':
        raw_input = request.form.get('numbers')
        if raw_input:
            try:
                # Convert the input string to a list of integers
                numbers = list(map(int, raw_input.split(',')))
                sorted_list = sorting_instance.quicksort(numbers)  # Sort the list
            except ValueError:
                sorted_list = ['Invalid input. Please enter numbers separated by commas.']
    
    # Render the template with sorted_list initialized
    return render_template('sorting.html', sorted_list=sorted_list)

@main.route('/graph', methods=['GET', 'POST'])
def graph():
    current_graph = graph_instance.get_graph()
    message = ""
    
    if request.method == 'POST':
        operation = request.form.get('operation')

        if operation == 'add_node':
            node = request.form.get('node')
            graph_instance.add_node(node)
            message = f"Added node {node} to the graph."
        
        elif operation == 'add_edge':
            node1 = request.form.get('node1')
            node2 = request.form.get('node2')
            graph_instance.add_edge(node1, node2)
            message = f"Added edge between {node1} and {node2}."
        
        return redirect(url_for('main.graph', message=message))

    return render_template('graph.html', graph=current_graph, message=message)

@main.route('/circular_double_link_list', methods=['GET', 'POST'])
def circular_double_link_list():
    current_list = circular_double_linked_list_instance.traverse()
    message = ""
    
    if request.method == 'POST':
        operation = request.form.get('operation')

        if operation == 'insert':
            value = int(request.form.get('value'))
            circular_double_linked_list_instance.insert(value)
            message = f"Inserted {value} into the list."
        
        elif operation == 'delete':
            value = int(request.form.get('value'))
            deleted = circular_double_linked_list_instance.delete(value)
            if deleted:
                message = f"Deleted {value} from the list."
            else:
                message = f"Value {value} not found in the list."
        
        return redirect(url_for('main.circular_double_link_list', message=message))

    return render_template('circular_double_link_list.html', list=current_list, message=message)