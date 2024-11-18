from flask import Blueprint, render_template, request, redirect, url_for
from flask import flash
import subprocess
from app.models.array import Array
from app.models.double_link_list import DoublyLinkedList
from app.models.queue import Queue
from app.models.quicksort_binary_search import Sorting
from app.models.stack import Stack
from app.models.binary_tree import BinaryTree
from app.models.graph import Graph
import sys

main = Blueprint('main', __name__)
array_object = Array() # The array 
doubly_object = DoublyLinkedList() # The doubly linked list
queue_object = Queue() # This is the queue
sorting_instance = Sorting() # Sorting object
stack_object = Stack() # The stack
binary_tree_instance = BinaryTree() # The binary tree
graph_instance = Graph() # The graph

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/array', methods=['GET', 'POST'])
def array():
    current_array = array_object.current_array()
    if request.method == 'POST':
        index = request.form.get('index') # Get the index the user inputs in the index text box
        operation = request.form.get('operation') # Get the operation the user select from the dropdown menu
        
        if operation == 'insert':
            log = request.form.get('element')
            if log and array_object.insert_log(log, index): #check that the function has what it neeeds
                flash(f"Element: {log} has been added to the array at index: {index}", "success") # Flash the message in the screen use the "success" so it appears green
            else:
                flash(f'Check you index: {index} (Maybe not in the array?)', 'danger')
                
        elif operation == 'delete':
            # We don use request.form.get since we already got the index before, and to delete we just need the index
            if array_object.delete_log(index): #check the function has what it needs
                flash(f'The log in the {index} index has been deleted successfully' 'success')
            else:
                flash(f'Error, {index} index has not been indetify check the you have the correct or a valid index' 'danger')
        
        elif operation == 'update':
            log = request.form.get('element')
            if log and array_object.update_log(log, index):
                flash(f'The element in the {index} index has been updated to: {log}', 'success')
        
        elif operation == 'access':
            log = array_object.get_log(index)
            if log:
                flash(f'The element at index: {index} is: {log}', 'success')
            else:
                flash('Invalid index, or element is not in the array', 'danger')
        return redirect(url_for('main.array'))
    return render_template('array.html', array=current_array)

@main.route('/array/regenerate', methods=['POST'])
def regenerate_array():
    try:
        """
        To regenerate the logs in any case the user wants to, we will execute a script
        which will regenerate the logs in the array_logs.json file.
        """
        subprocess.run([sys.executable, 'app/scripts/script_array.py'], check=True)
        array_object.load_array()
        flash('Array logs have been reset to default.', 'success')
    except subprocess.CalledProcessError:
        flash('Error regenerating array logs.', 'danger')
    return redirect(url_for('main.array'))

@main.route('/double_linked_list', methods=['GET', 'POST'])
def double_linked_list():
    current_doubly_linked_list = doubly_object.to_list_with_pointers()  # This is the method I created to mark the head and the tail of the doubly linked list
    
    if request.method == 'POST':
        index = request.form.get('index')
        operation = request.form.get('operation')
        
        """Check the operations"""
        if operation == 'insert':
            log = request.form.get('log')
            if doubly_object.insert_at(int(index), log):
                flash(f"The {log}, was added successfully in the {index} index", 'success')
            else:
                flash('Error, check the index, index may not be in the list, or check the log format', 'danger')

        elif operation == 'delete':
            if doubly_object.delete_at(int(index)):
                flash(f"The log in the {index} was successlly deleted", 'success')
            else:
                flash('Error, check the index, index may not be in the list', 'danger')

        elif operation == 'update':
            log = request.form.get('log')
            if doubly_object.update_at(int(index), log):
                flash(f"Log Entry at index {index} updated to: {log}", 'success')
            else:
                flash('Error, check the index, index may not be in the list', 'danger')

        elif operation == 'access':
            log = doubly_object.get_at(int(index))
            if log:
                flash(f"Log Entry at index {index} is: {log}", 'success')
            else:
                flash('Error, check the index, index may not be in the list', 'danger')

        return redirect(url_for('main.double_linked_list'))
    
    return render_template('double_linked_list.html', logs=current_doubly_linked_list)

@main.route('/double_linked_list/regenerate', methods=['POST'])
def regenerate_double_linked_list():
    try:
        subprocess.run([sys.executable, 'app/scripts/script_double_linked_list.py'], check=True)
        doubly_object.load_doubly_linked_list()
        flash('Double Linked List has been reset to default.', 'success')
    except subprocess.CalledProcessError:
        flash('Error regenerating Double Linked List.', 'danger')
    return redirect(url_for('main.double_linked_list'))

@main.route('/queue', methods=['GET', 'POST'])
def queue():
    if request.method == 'POST':
        log = request.form.get('enqueue_log')
        if log:
            if queue_object.enqueue(log):
                flash('Log has been successfully been added to the queue', 'success')
            else:
                flash('There was a problem enqueuing the access attempt. Please check the format (IP, reason).', 'danger')
        return redirect(url_for('main.queue'))
    return render_template('queue.html', queue=queue_object.get_queue())

@main.route('/queue/dequeue', methods=['POST'])
def dequeue_queue():
    if queue_object.dequeue():
        flash('Access attempt has been remove, (dequeue).', 'success')
    else:
        flash('The queue is already empty. Regenerate the queue to be able to dequeue items.', 'danger')
    return redirect(url_for('main.queue'))

@main.route('/queue/regenerate', methods=['POST'])
def regenerate_queue():
    try:
        subprocess.run([sys.executable, 'app/scripts/script_queue.py'], check=True)
        queue_object.load_queue()
        flash('Queue has been reset to default.', 'success')
    except subprocess.CalledProcessError:
        flash('Error regenerating queue.', 'danger')
    return redirect(url_for('main.queue'))

@main.route('/quicksort_binary_search', methods=['GET', 'POST'])
def quicksort_binary_search():
    logs = sorting_instance.get_logs()  # This will get the logs from their current state
    return render_template('quicksort_binary_search.html', logs=logs)

@main.route('/sort_logs', methods=['POST'])
def sort_logs():
    sorting_instance.sort_logs()  # Sort the logs using quicksort
    flash("Logs have been sorted.", 'success')
    return redirect(url_for('main.quicksort_binary_search'))

@main.route('/shuffle_logs', methods=['POST'])
def shuffle_logs():
    sorting_instance.disorganize_logs()  # Shuffle the logs randomly
    flash("Logs have been shuffled.", 'info')
    return redirect(url_for('main.quicksort_binary_search'))

@main.route('/search_log', methods=['POST'])
def search_log():
    log = request.form.get('log_entry')
    if log:
        index = sorting_instance.search_log(log)
        if isinstance(index, int):
            flash(f"Log entry found at position {index + 1}.", 'success')
        else:
            flash("Log entry not found.", 'danger')
    else:
        flash("Please enter a log entry to search.", 'warning')
    return redirect(url_for('main.quicksort_binary_search'))

@main.route('/stack', methods=['GET', 'POST'])
def stack():
    if request.method == 'POST':
        push_log = request.form.get('push_log')
        if push_log:
            if stack_object.push(push_log):
                flash('log has been successfully pushed to the stack.', 'success')
            else:
                flash('There was a problem pushing the log to the stack (maybe is empty?).', 'danger')
        return redirect(url_for('main.stack'))
    return render_template('stack.html', stack=stack_object.get_stack())

@main.route('/stack/pop', methods=['POST'])
def pop_stack():
    if stack_object.pop():
        flash('Log has been successfully popped from the stack.', 'success')
    else:
        flash('The stack is already empty. Add logs to be able to pop.', 'danger')
    return redirect(url_for('main.stack'))

@main.route('/stack/regenerate', methods=['POST'])
def regenerate_stack():
    try:
        subprocess.run([sys.executable, 'app/scripts/script_stack.py'], check=True)
        stack_object.load_stack()
        flash('Stack has been reset to default.', 'success')
    except subprocess.CalledProcessError:
        flash('Error regenerating stack.', 'danger')
    return redirect(url_for('main.stack'))


@main.route('/binary_tree', methods=['GET', 'POST'])
def binary_tree():
    """
    Handles binary tree operations and displays the tree structure graphically.
    """
    if request.method == 'POST':
        operation = request.form.get('operation')
        value = request.form.get('value')
        
        if not value:
            flash("Please enter a log entry value", 'danger')
            return redirect(url_for('main.binary_tree'))
        
        try:
            if operation == 'insert':
                binary_tree_instance.insert(value)
                flash(f"Log '{value}' has been inserted into the tree.", 'success')
            elif operation == 'delete':
                if binary_tree_instance.delete(value):
                    flash(f"Log '{value}' has been deleted from the tree.", 'success')
                else:
                    flash(f"Log '{value}' not found in the tree for deletion.", 'danger')
            elif operation == 'search':
                position = binary_tree_instance.search(value)
                if position != -1:
                    flash(f"Log '{value}' was found in the tree at position {position}.", 'success')
                else:
                    flash(f"Log '{value}' not found in the tree.", 'danger')
        except Exception as e:
            flash(f"An error occurred: {e}", 'danger')
        
        # After the operation, regenerate the tree image
        binary_tree_instance.generate_tree_image()
        return redirect(url_for('main.binary_tree'))

    # Display the tree structure (image) on GET requests
    return render_template(
        'binary_tree.html',
        tree_image=url_for('static', filename='img/binary_tree.png')  # Updated path to the tree image
    )
    
@main.route('/binary_tree/regenerate', methods=['POST'])
def regenerate_binary_tree():
    try:
        # Run the Python script to regenerate binary tree logs
        subprocess.run([sys.executable, 'app/scripts/script_binary_tree.py'], check=True)
        binary_tree_instance.load_logs()
        flash("Binary tree logs have been regenerated.", "success")
    except subprocess.CalledProcessError as e:
        flash(f"Failed to regenerate binary tree logs: {e}", "danger")
    return redirect(url_for("main.binary_tree"))

@main.route('/graph', methods=['GET', 'POST'])
def graph():
    """
    Handles operations for adding nodes, edges, and calculating the MST using Kruskal's algorithm.
    """
    mst_edges = []
    message = ""
    
    if request.method == 'POST':
        operation = request.form.get('operation')

        if operation == 'add_node':
            node = request.form.get('node')
            if node:
                graph_instance.add_node(node)
                flash(f"Node '{node}' added to the graph.", 'success')
            else:
                flash("Please provide a node name.", 'danger')

        elif operation == 'add_edge':
            node1 = request.form.get('node1')
            node2 = request.form.get('node2')
            weight = request.form.get('weight')

            if node1 and node2 and weight:
                try:
                    weight = int(weight)
                    graph_instance.add_edge(node1, node2, weight)
                    flash(f"Edge between '{node1}' and '{node2}' with weight {weight} added.", 'success')
                except ValueError:
                    flash("Weight must be a number.", 'danger')
            else:
                flash("Please provide both nodes and a weight for the edge.", 'danger')

        elif operation == 'kruskal':
            mst_edges = graph_instance.kruskal()
            if mst_edges:
                flash("Minimum Spanning Tree (MST) generated using Kruskal's algorithm.", 'success')
            else:
                flash("Graph is empty or no MST could be generated.", 'danger')

        graph_instance.generate_graph_image(mst_edges if operation == 'kruskal' else None)
        return redirect(url_for('main.graph'))

    return render_template(
        'graph.html',
        graph_image=url_for('static', filename='img/graph.png'),
        mst_edges=mst_edges
    )