import unittest

# Use the imports below to test either your array-based stack
# or your link-based version
# from stack_array import Stack
from stack_linked import Stack


class TestLab2(unittest.TestCase):
    def test_simple(self):
        stack = Stack(5)
        stack.push(0)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(), 1)

    def test_simple_1(self):
        stack = Stack(5)
        stack.push(0)
        stack.push(1)
        stack.push(2)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(), 3)
        self.assertEqual(stack.peek(), 2)
        # Pop time
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.size(), 2)
        self.assertEqual(stack.peek(), 1)
        # Pop second time
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.size(), 1)
        self.assertEqual(stack.peek(), 0)

    def test_max(self):
        """Testing everything  can think of"""
        stack = Stack(5)
        stack.push(0)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        self.assertFalse(stack.is_empty())
        self.assertTrue(stack.is_full())
        self.assertRaises(IndexError, stack.push, 5)  # used to check for exception

        self.assertEqual(stack.pop(), 4)
        self.assertEqual(stack.size(), 4)
        self.assertEqual(stack.peek(), 3)
        # Pop second time
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.size(), 3)
        self.assertEqual(stack.peek(), 2)

        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.pop(), 0)

        self.assertTrue(stack.is_empty())
        self.assertRaises(IndexError, stack.peek)

        self.assertRaises(IndexError, stack.pop)  # used to check for exception

        stack.push(0)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        self.assertFalse(stack.is_empty())
        self.assertTrue(stack.is_full())
        self.assertRaises(IndexError, stack.push, 5)  # used to check for exception

        self.assertEqual(stack.pop(), 4)
        self.assertEqual(stack.size(), 4)
        self.assertEqual(stack.peek(), 3)

    def test_none1(self):
        """Testing None"""
        stack = Stack(5)
        stack.push(None)
        stack.push(1)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(), 2)


if __name__ == '__main__':
    unittest.main()
