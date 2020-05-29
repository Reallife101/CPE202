from queue_array import Queue


class TreeNode:
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right


class BinarySearchTree:

    def __init__(self):  # Returns empty BST
        self.root = None

    def is_empty(self):  # returns True if tree is empty, else False
        return self.root is None

    def search(self, key):  # returns True if key is in a node of the tree, else False
        if self.is_empty():
            return False
        return self.search_helper(key, self.root)

    def search_helper(self, key, node):
        if node.key == key:
            return True
        if key > node.key and node.right is not None:
            return self.search_helper(key, node.right)
        elif key < node.key and node.left is not None:
            return self.search_helper(key, node.left)
        else:
            return False

    def insert(self, key, data=None):  # inserts new node w/ key and data
        # If an item with the given key is already in the BST, 
        # the data in the tree will be replaced with the new data
        if self.root is None:
            self.root = TreeNode(key, data)
        else:
            self.insert_helper(key, data, self.root)

    def insert_helper(self, key, data, node):
        if node.key == key:
            node.data = data
        elif key > node.key:
            if node.right is None:
                node.right = TreeNode(key, data)
            else:
                self.insert_helper(key, data, node.right)
        elif key < node.key:
            if node.left is None:
                node.left = TreeNode(key, data)
            else:
                self.insert_helper(key, data, node.left)

    def find_min(self):  # returns a tuple with min key and data in the BST
        # returns None if the tree is empty
        if self.is_empty():
            return None
        node = self.root
        while node.left is not None:
            node = node.left
        return node.key, node.data

    def find_max(self):  # returns a tuple with max key and data in the BST
        # returns None if the tree is empty
        if self.is_empty():
            return None
        node = self.root
        while node.right is not None:
            node = node.right
        return node.key, node.data

    def tree_height(self):  # return the height of the tree
        # returns None if tree is empty
        if self.is_empty():
            return None
        if self.root.left is None and self.root.right is None:
            return 0
        return self.tree_height_helper(self.root, 0)

    def tree_height_helper(self, node, height):
        if node is not None:
            left = self.tree_height_helper(node.left, height + 1)
            right = self.tree_height_helper(node.right, height + 1)
            return max(left, right, height)
        else:
            return height - 1

    def inorder_list(self):  # return Python list of BST keys representing in-order traversal of BST
        if self.is_empty():
            return []
        return self.inorder_list_helper(self.root)

    def inorder_list_helper(self, node):
        final_list = []
        if node is not None:
            final_list = final_list + self.inorder_list_helper(node.left)
            final_list.append(node.key)
            final_list = final_list + self.inorder_list_helper(node.right)
        return final_list

    def preorder_list(self):  # return Python list of BST keys representing pre-order traversal of BST
        if self.is_empty():
            return []
        return self.preorder_list_helper(self.root)

    def preorder_list_helper(self, node):
        final_list = []
        if node is not None:
            final_list.append(node.key)
            final_list = final_list + self.preorder_list_helper(node.left)
            final_list = final_list + self.preorder_list_helper(node.right)
        return final_list

    def level_order_list(self):  # return Python list of BST keys representing level-order traversal of BST
        # You MUST use your queue_array data structure from lab 3 to implement this method
        q = Queue(25000)  # Don't change this!
        final_list = []

        if self.is_empty():
            return []

        q.enqueue(self.root)
        while not (q.is_empty()):
            node = q.dequeue()
            final_list.append(node.key)
            if node.left is not None:
                q.enqueue(node.left)
            if node.right is not None:
                q.enqueue(node.right)

        return final_list
