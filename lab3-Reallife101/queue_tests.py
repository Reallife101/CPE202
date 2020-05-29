import unittest
from queue_array import Queue


# from queue_linked import Queue


class TestLab1(unittest.TestCase):
    def test_queue(self):
        """Trivial test to ensure method names and parameters are correct"""
        q = Queue(5)
        q.is_empty()
        q.is_full()
        q.enqueue('thing')
        q.dequeue()
        q.size()

    def test_queue_full(self):
        """Testing everything  can think of"""
        q = Queue(5)
        q.enqueue(0)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        self.assertFalse(q.is_empty())
        self.assertTrue(q.is_full())
        self.assertRaises(IndexError, q.enqueue, 5)  # used to check for exception

        self.assertEqual(q.dequeue(), 0)
        self.assertEqual(q.size(), 4)

        # dequeue second time
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.size(), 3)

        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 3)
        self.assertEqual(q.dequeue(), 4)

        self.assertTrue(q.is_empty())

        self.assertRaises(IndexError, q.dequeue)  # used to check for exception

        q.enqueue(0)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        self.assertFalse(q.is_empty())
        self.assertTrue(q.is_full())
        self.assertRaises(IndexError, q.enqueue, 5)  # used to check for exception

        self.assertEqual(q.dequeue(), 0)
        self.assertEqual(q.size(), 4)

    def test_none1(self):
        """Testing None"""
        q = Queue(5)
        q.enqueue(None)
        q.enqueue(1)
        self.assertFalse(q.is_empty())
        self.assertFalse(q.is_full())
        self.assertEqual(q.size(), 2)


if __name__ == '__main__':
    unittest.main()
