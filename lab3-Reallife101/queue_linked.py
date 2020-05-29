class Node:
    def __init__(self, item):
        self.data = item
        self.next = None


class Queue:
    """Implements an link-based ,efficient first-in first-out Abstract Data Type"""

    def __init__(self, capacity):
        """Creates an empty Queue with a capacity"""
        self.capacity = capacity
        self.front = None
        self.back = None
        self.num_items = 0

    def is_empty(self):
        """Returns True if the Queue is empty, and False otherwise"""
        if self.num_items == 0:
            return True
        return False

    def is_full(self):
        """Returns True if the Queue is full, and False otherwise"""
        if self.capacity == self.num_items:
            return True
        return False

    def enqueue(self, item):
        """If Queue is not full, enqueues (adds) item to Queue
           If Queue is full when enqueue is attempted, raises IndexError"""
        if not self.is_full():
            current_node = Node(item)
            if self.back is not None:
                self.back.next = current_node
            if self.front is None:
                self.front = current_node
            self.back = current_node
            self.num_items += 1
        else:
            raise IndexError

    def dequeue(self):
        """If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError"""
        if self.is_empty():
            raise IndexError
        else:
            self.num_items -= 1
            data = self.front.data
            self.front = self.front.next
            return data

    def size(self):
        """Returns the number of elements currently in the Queue, not the capacity"""
        return self.num_items
