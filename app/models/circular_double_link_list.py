class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class CircularDoubleLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            new_node.prev = self.head
        else:
            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node

    def delete(self, value):
        if self.head is None:
            return False
        current = self.head
        while True:
            if current.value == value:
                if current == self.head and current.next == self.head:
                    self.head = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    if current == self.head:
                        self.head = current.next
                return True
            current = current.next
            if current == self.head:
                break
        return False

    def traverse(self):
        result = []
        if self.head is None:
            return result
        current = self.head
        while True:
            result.append(current.value)
            current = current.next
            if current == self.head:
                break
        return result
