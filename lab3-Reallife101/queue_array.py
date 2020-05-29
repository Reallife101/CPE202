class Queue:
    """Implements an array-based, efficient first-in first-out Abstract Data Type
       using a Python array (faked using a List)"""

    def __init__(self, capacity):
        """Creates an empty Queue with a capacity"""
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = 0
        self.back = 0
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
            self.items[self.back] = item
            self.num_items += 1
            self.back += 1
            if self.back == self.capacity:  # If hit the end of list, wrap around
                self.back = 0
        else:  # If full, raise error
            raise IndexError

    def dequeue(self):
        """If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError"""
        if self.is_empty():  # If empty, raise error
            raise IndexError
        else:
            self.num_items -= 1
            data = self.items[self.front]
            self.front += 1
            if self.front == self.capacity:  # If hit the end of list, wrap around
                self.front = 0
            return data

    def size(self):
        """Returns the number of elements currently in the Queue, not the capacity"""
        return self.num_items
