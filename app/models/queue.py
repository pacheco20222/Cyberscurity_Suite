class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)  # Remove the first item
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def get_queue(self):
        return self.queue