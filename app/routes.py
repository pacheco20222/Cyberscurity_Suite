from flask import Blueprint, render_template, request, redirect, url_for
from .models.hash_table import HashTable
from .models.stack import Stack
from .models.queue import Queue
from .models.sorting import Sorting
from .models.array import Array

main = Blueprint('main', __name__)
hash_table_instance = HashTable()
stack_instance = Stack()
queue_instance = Queue()
sorting_instance = Sorting()
array_instance = Array()

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/array')
def array():
    return render_template('array.html')

@main.route('/stack', methods=['GET', 'POST'])
def stack():
    if request.method == 'POST':
        item = request.form.get('push_item')
        if item:
            stack_instance.push(item)
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

@main.route('/binary_tree')
def binary_tree():
    return render_template('binary_tree.html')

@main.route('/sorting', methods=['GET', 'POST'])
def sorting():
    if request.method == 'POST':
        raw_input = request.form.get('numbers')
        if raw_input:
            try:
                # Convert the input string to a list of integers
                numbers = list(map(int, raw_input.split(',')))
                sorted_list = sorting_instance.quicksort(numbers)  # Sort the list
            except ValueError:
                sorted_list = ['Invalid input. Please enter numbers separated by commas.']
        return render_template('sorting.html', sorted_list=sorted_list)

    return render_template('sorting.html', sorted_list=sorted_list)

@main.route('/graph')
def graph():
    return render_template('graph.html')

@main.route('/linked_list')
def linked_list():
    return render_template('linked_list.html')
