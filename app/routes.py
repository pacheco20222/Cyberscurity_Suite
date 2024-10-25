from flask import Blueprint, render_template, request, redirect, url_for
from flask import flash
from .models.stack import Stack
from .models.queue import Queue
from .models.array import Array
from .models.binary_tree import BinaryTree
from .models.graph import Graph
from .models.hash_table import HashTable
from .models.sorting import Sorting
from .models.circular_double_link_list import CircularDoubleLinkedList
from .models.list import LogList

main = Blueprint('main', __name__)
stack_object = Stack()
queue_object = Queue()
array_object = Array()
binary_tree_instance = BinaryTree()
graph_instance = Graph()
hash_table_instance = HashTable()
sorting_instance = Sorting()
circular_double_linked_list_instance = CircularDoubleLinkedList()

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/stack', methods=['GET', 'POST'])
def stack():
    if request.method == 'POST':
        push_log = request.form.get('push_log')
        if push_log:
            if stack_object.push(push_log):
                flash('Login attempt has successfuly been pushed to the stack', 'success')
            else:
                flash('There was a problem pushing the login attempt to the stack, check format (username, status)', 'danger')
        return redirect(url_for('main.stack'))
    return render_template('stack.html', stack=stack_object.get_stack())

@main.route('/stack/pop', methods=['POST'])
def pop_stack():
    if stack_object.pop():
        flash('Login attempt has been popped from the stack', 'success')
    else:
        flash('The stack is already empty, push a login attempt to try and pop', 'danger')
    return redirect(url_for('main.stack'))

@main.route('/queue', methods=['GET', 'POST'])
def queue():
    if request.method == 'POST':
        log = request.form.get('enqueue_log')
        if log:
            if queue_object.enqueue(log):
                flash('Login attempt has successfuly been enqueued', 'success')
            else:
                flash('There was a problem enqueuing the login attempt, check format (username, status)', 'danger')
        return redirect(url_for('main.queue'))
    return render_template('queue.html', queue=queue_object.get_queue())

@main.route('/queue/dequeue', methods=['POST'])
def dequeue_queue():
    if queue_object.dequeue():
        flash('Login attempt has been dequeued', 'success')
    else:
        flash('The queue is already empty, enqueue a login attempt to try and dequeue', 'danger')
    return redirect(url_for('main.queue'))


@main.route('/array', methods=['GET', 'POST'])
def array():
    live_array = array_object.return_array()
    if request.method == 'POST':
        index = request.form.get('index')
        operation = request.form.get('operation')
        
        if operation == 'insert':
            element = request.form.get('element')
            if element and array_object.insert_element(element, index):
                flash(f"Element {element} has been inserted at index {index}", 'success')
            else:
                flash('Invalid index', 'danger')
        
        elif operation == 'delete':
            if array_object.delete_element(index):
                flash(f"Element at index {index} has been deleted", 'success')
            else:
                flash('Invalid index', 'danger')
        
        elif operation == 'update':
            element = request.form.get('element')
            if element and array_object.update_element(element, index):
                flash(f"Element at index {index} has been updated to {element}", 'success')
            else:
                flash('Invalid index', 'danger')
        
        elif operation == 'access':
            element = array_object.access_element(index)
            if element:
                flash(f"Element at index {index} is {element}", 'success')
            else:
                flash('Invalid index', 'danger')
        return redirect(url_for('main.array'))
    return render_template('array.html', array=live_array)

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