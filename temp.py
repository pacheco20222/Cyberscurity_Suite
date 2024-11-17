from flask import Blueprint, render_template, request, redirect, url_for
from flask import flash
import subprocess
from app.models.array import  Array
from app.models.double_link_list import DoublyLinkedList
from app.models.queue import Queue
from app.models.quicksort_binary_search import Sorting

main = Blueprint('main', __name__)
array_object = Array() # The array 
doubly_object = DoublyLinkedList() # The doubly linked list
queue_object = Queue() # This is the queue
sorting_instance = Sorting() # Sorting object

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/array', method=['GET', 'POST'])
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
