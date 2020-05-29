class Node:
    """Node for use with doubly-linked list"""

    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class OrderedList:
    """A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of list)"""

    def __init__(self):
        """Use ONE dummy node as described in class
           ***No other attributes***
           DO NOT have an attribute to keep track of size"""
        self.head = Node(None)
        self.head.next = self.head
        self.head.prev = self.head

    def is_empty(self):
        """Returns True if OrderedList is empty
            MUST have O(1) performance"""
        return self.head.next == self.head

    def add(self, item):
        """Adds an item to OrderedList, in the proper location based on ordering of items
           from lowest (at head of list) to highest (at tail of list) and returns True.
           If the item is already in the list, do not add it again and return False.
           MUST have O(n) average-case performance"""
        return self.add_helper(item, self.head.next)

    def add_helper(self, item, node):
        """Helps remove do things recursively"""
        if node.item == item or node.next.item == item:
            return False
        new_node = Node(item)
        if node.next == self.head or node.item < item < node.next.item:
            node.next.prev = new_node
            new_node.next = node.next
            new_node.prev = node
            node.next = new_node
            return True
        if node.item > item and node.prev == self.head:
            node.prev = new_node
            new_node.next = node
            new_node.prev = self.head
            self.head.next = new_node
            return True
        return self.add_helper(item, node.next)

    def remove(self, item):
        """Removes the first occurrence of an item from OrderedList. If item is removed (was in the list)
          returns True.  If item was not removed (was not in the list) returns False
           MUST have O(n) average-case performance"""

        return self.remove_helper(item, self.head.next)

    def remove_helper(self, item, node):
        """Helps remove do things recursively"""
        if node.item == item:
            node.prev.next = node.next
            node.next.prev = node.prev
            return True
        if node == self.head:
            return False
        return self.remove_helper(item, node.next)

    def index(self, item):
        """Returns index of the first occurrence of an item in OrderedList (assuming head of list is index 0).
           If item is not in list, return None
           MUST have O(n) average-case performance"""
        node = self.head.next
        current_index = 0
        while node != self.head:
            if node.item == item:
                return current_index
            current_index += 1
            node = node.next
        return None

    def pop(self, index):
        """Removes and returns item at index (assuming head of list is index 0).
           If index is negative or >= size of list, raises IndexError
           MUST have O(n) average-case performance"""
        node = self.head.next
        current_index = 0
        if index < 0 or index >= self.size():
            raise IndexError
        while node != self.head:
            if current_index == index:
                node.next.prev = node.prev
                node.prev.next = node.next
                return node.item
            current_index += 1
            node = node.next

    def search(self, item):
        """Searches OrderedList for item, returns True if item is in list, False otherwise"
           To practice recursion, this method must call a RECURSIVE method that
           will search the list
           MUST have O(n) average-case performance"""

        return self.search_helper(item, self.head.next)

    def search_helper(self, item, node):
        """Helps search do things recursively"""
        if node.item == item:
            return True
        if node.next == self.head:
            return False
        return self.search_helper(item, node.next)

    def python_list(self):
        """Return a Python list representation of OrderedList, from head to tail
           For example, list with integers 1, 2, and 3 would return [1, 2, 3]
           MUST have O(n) performance"""
        node = self.head.next
        list1 = []
        while node != self.head:
            list1.append(node.item)
            node = node.next
        return list1

    def python_list_reversed(self):
        """Return a Python list representation of OrderedList, from tail to head, using recursion
           For example, list with integers 1, 2, and 3 would return [3, 2, 1]
           To practice recursion, this method must call a RECURSIVE method that
           will return a reversed list
           MUST have O(n) performance"""
        if self.is_empty():
            return []
        return self.python_list_reversed_helper(self.python_list())

    def python_list_reversed_helper(self, list2):
        if len(list2) == 1:
            return [list2[0]]
        list1 = [list2[0]]
        del list2[0]

        return self.python_list_reversed_helper(list2) + list1

    def size(self):
        """Returns number of items in the OrderedList
           To practice recursion, this method must call a RECURSIVE method that
           will count and return the number of items in the list
           MUST have O(n) performance"""
        return self.size_helper(self.head.next)

    def size_helper(self, node):
        """Helps size do things recursively"""
        if node == self.head:
            return 0
        return 1 + self.size_helper(node.next)
