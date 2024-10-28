from flask import Blueprint, render_template, request, redirect, url_for
from flask import flash
import subprocess
import os
from app.models.stack import Stack
from app.models.queue import Queue
from app.models.array import Array
from app.models.binary_tree import BinaryTree
from app.models.graph import Graph
from app.models.quicksort_binary_search import Sorting
from app.models.double_link_list import DoublyLinkedList

main = Blueprint('main', __name__)
stack_object = Stack()
queue_object = Queue()
array_object = Array()
binary_tree_instance = BinaryTree()
graph_instance = Graph()
sorting_instance = Sorting()
live_list = DoublyLinkedList()


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/stack', methods=['GET', 'POST'])
def stack():
    if request.method == 'POST':
        push_log = request.form.get('push_log')
        if push_log:
            if stack_object.push(push_log):
                flash('Login attempt has successfully been pushed to the stack', 'success')
            else:
                flash('There was a problem pushing the login attempt to the stack. Check format (username, status)', 'danger')
        return redirect(url_for('main.stack'))
    return render_template('stack.html', stack=stack_object.get_stack())

@main.route('/stack/pop', methods=['POST'])
def pop_stack():
    if stack_object.pop():
        flash('Login attempt has been popped from the stack', 'success')
    else:
        flash('The stack is already empty. Push a login attempt to try and pop', 'danger')
    return redirect(url_for('main.stack'))

@main.route('/stack/regenerate', methods=['POST'])
def regenerate_stack():
    try:
        # Call the Python script to regenerate the file
        subprocess.run(["python", "app/scripts/script_stack.py"], check=True)
        
        # Reload the stack to reflect the regenerated logs immediately
        stack_object.load_stack()
        
        flash("Stack logs have been regenerated.", "success")
    except subprocess.CalledProcessError as e:
        flash(f"Failed to regenerate stack logs: {e}", "danger")
    return redirect(url_for("main.stack"))


@main.route('/queue', methods=['GET', 'POST'])
def queue():
    if request.method == 'POST':
        log = request.form.get('enqueue_log')
        if log:
            if queue_object.enqueue(log):
                flash('Access attempt has successfully been enqueued.', 'success')
            else:
                flash('There was a problem enqueuing the access attempt. Please check the format (IP, reason).', 'danger')
        return redirect(url_for('main.queue'))
    return render_template('queue.html', queue=queue_object.get_queue())

@main.route('/queue/dequeue', methods=['POST'])
def dequeue_queue():
    if queue_object.dequeue():
        flash('Access attempt has been dequeued.', 'success')
    else:
        flash('The queue is already empty. Enqueue an access attempt to try and dequeue.', 'danger')
    return redirect(url_for('main.queue'))

@main.route('/queue/regenerate', methods=['POST'])
def regenerate_queue():
    try:
        # Run the Python script to regenerate queue logs
        subprocess.run(["python", "app/scripts/script_queue.py"], check=True)
        flash("Queue logs have been regenerated.", "success")
    except subprocess.CalledProcessError as e:
        flash(f"Failed to regenerate queue logs: {e}", "danger")
    return redirect(url_for("main.queue"))


@main.route('/binary_tree', methods=['GET', 'POST'])
def binary_tree():
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
                if binary_tree_instance.search(value):
                    flash(f"Log '{value}' was found in the tree.", 'success')
                else:
                    flash(f"Log '{value}' not found in the tree.", 'danger')
        except Exception as e:
            flash(f"An error occurred: {e}", 'danger')
        return redirect(url_for('main.binary_tree'))

    # For GET requests, perform the traversals to show the current tree structure
    inorder = binary_tree_instance.inorder_traversal()
    preorder = binary_tree_instance.preorder_traversal()
    postorder = binary_tree_instance.postorder_traversal()

    return render_template(
        'binary_tree.html',
        inorder=inorder,
        preorder=preorder,
        postorder=postorder
    )


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

@main.route('/quicksort_binary_search', methods=['GET', 'POST'])
def quicksort_binary_search():
    logs = sorting_instance.get_logs()  # Fetch logs to display
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
    log_entry = request.form.get('log_entry')
    if log_entry:
        index = sorting_instance.search_log(log_entry)
        if isinstance(index, int):
            flash(f"Log entry found at position {index + 1}.", 'success')
        else:
            flash("Log entry not found.", 'danger')
    else:
        flash("Please enter a log entry to search.", 'warning')
    return redirect(url_for('main.quicksort_binary_search'))


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

@main.route('/double_linked_list', methods=['GET', 'POST'])
def double_linked_list():
    live_list_items = live_list.to_list()  # Changed variable name for clarity
    
    if request.method == 'POST':
        index = request.form.get('index')
        operation = request.form.get('operation')

        if operation == 'insert':
            log = request.form.get('log')
            if live_list.insert_at(int(index), log):
                flash(f"Log Entry '{log}' inserted at index {index}", 'success')
            else:
                flash('Invalid index', 'danger')

        elif operation == 'delete':
            if live_list.delete_at(int(index)):
                flash(f"Log Entry at index {index} deleted", 'success')
            else:
                flash('Invalid index', 'danger')

        elif operation == 'update':
            log = request.form.get('log')
            if live_list.update_at(int(index), log):
                flash(f"Log Entry at index {index} updated to: {log}", 'success')
            else:
                flash('Invalid index', 'danger')

        elif operation == 'access':
            log = live_list.get_at(int(index))
            if log:
                flash(f"Log Entry at index {index} is: {log}", 'success')
            else:
                flash('Invalid index', 'danger')

        elif operation == 'clear':
            live_list.clear()
            flash('All log entries have been cleared', 'success')

        return redirect(url_for('main.double_linked_list'))

    return render_template('double_linked_list.html', logs=live_list_items)
