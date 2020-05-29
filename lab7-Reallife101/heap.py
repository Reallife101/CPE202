class MaxHeap:

    def __init__(self, capacity=50):
        '''Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be created.'''
        self.heap = [0] * (capacity + 1)
        self.capacity = capacity
        self.current_size = 0

    def enqueue(self, item):
        '''inserts "item" into the heap, returns true if successful, false if there is no room in the heap
           "item" can be any primitive or ***object*** that can be compared with other 
           items using the < operator'''
        if self.is_full():
            return False
        self.heap.append(item)
        self.current_size += 1
        self.perc_up(self.current_size)
        return True

    def peek(self):
        '''returns max without changing the heap, returns None if the heap is empty'''
        if self.is_empty():
            return None
        return self.heap[1]

    def dequeue(self):
        '''returns max and removes it from the heap and restores the heap property
           returns None if the heap is empty'''
        if self.is_empty():
            return None
        item = self.heap[1]
        self.heap[1] = self.heap[self.current_size]
        self.current_size = self.current_size - 1
        self.heap.pop()
        self.perc_down(1)
        return item

    def contents(self):
        '''returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)'''
        return self.heap[1:]

    def build_heap(self, alist):
        '''Discards all items in the current heap and builds a heap from 
        the items in alist using the bottom-up construction method.  
        If the capacity of the current heap is less than the number of 
        items in alist, the capacity of the heap will be increased to accommodate 
        exactly the number of items in alist'''

        i = len(alist) // 2
        self.current_size = len(alist)
        if len(alist) > self.capacity:
            self.capacity = len(alist)
        self.heap = [0] + alist[:]
        while (i > 0):
            self.perc_down(i)
            i = i - 1

    def is_empty(self):
        '''returns True if the heap is empty, false otherwise'''
        return self.current_size == 0

    def is_full(self):
        '''returns True if the heap is full, false otherwise'''
        return self.current_size == self.get_capacity()

    def get_capacity(self):
        '''this is the maximum number of a entries the heap can hold
        1 less than the number of entries that the array allocated to hold the heap can hold'''
        return self.capacity

    def get_size(self):
        '''the actual number of elements in the heap, not the capacity'''
        return self.current_size

    def perc_down(self, i):
        '''where the parameter i is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes.'''
        while (i * 2) <= self.current_size:
            if i * 2 + 1 > self.current_size:
                mc = i * 2
            else:
                if self.heap[i * 2] > self.heap[i * 2 + 1]:  # was <
                    mc = i * 2
                else:
                    mc = i * 2 + 1

            if self.heap[i] < self.heap[mc]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[mc]
                self.heap[mc] = tmp
            i = mc

    def perc_up(self, i):
        '''where the parameter i is an index in the heap and perc_up moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes.'''
        while i // 2 > 0:
            if self.heap[i] > self.heap[i // 2]:
                hold = self.heap[i // 2]
                self.heap[i // 2] = self.heap[i]
                self.heap[i] = hold
            i = i // 2

    def heap_sort_ascending(self, alist):
        '''perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, then mutate alist to put the items in ascending order'''

        n = len(alist)

        for i in range(n, -1, -1):
            self.heapify(alist, n, i)

        for i in range(n - 1, 0, -1):
            alist[i], alist[0] = alist[0], alist[i]  # swap
            self.heapify(alist, i, 0)

    def heapify(self, alist, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and alist[i] < alist[l]:
            largest = l

        if r < n and alist[largest] < alist[r]:
            largest = r

        if largest != i:
            alist[i], alist[largest] = alist[largest], alist[i]

            self.heapify(alist, n, largest)



