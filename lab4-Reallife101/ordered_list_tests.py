import unittest
from ordered_list import *


class TestLab4(unittest.TestCase):

    def test_simple(self):
        t_list = OrderedList()
        t_list.add(10)
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.size(), 1)
        self.assertEqual(t_list.index(10), 0)
        self.assertTrue(t_list.search(10))
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.python_list_reversed(), [10])
        self.assertTrue(t_list.remove(10))
        t_list.add(10)
        self.assertEqual(t_list.pop(0), 10)

    def test_simple_everything(self):
        """Testing for 100% coverage"""
        t_list = OrderedList()
        t_list.add(10)
        self.assertFalse(t_list.add(10))
        self.assertTrue(t_list.add(30))
        self.assertFalse(t_list.add(30))
        self.assertTrue(t_list.add(40))
        self.assertTrue(t_list.add(50))
        self.assertTrue(t_list.add(20))
        self.assertEqual(t_list.size(), 5)
        self.assertEqual(t_list.python_list(), [10, 20, 30, 40, 50])
        self.assertEqual(t_list.python_list_reversed(), [50, 40, 30, 20, 10])
        self.assertFalse(t_list.remove(60))
        self.assertEqual(t_list.index(60), None)  # doesn't exist
        self.assertEqual(t_list.index(30), 2)
        self.assertRaises(IndexError, t_list.pop, -1)  # used to check for exception
        self.assertEqual(t_list.pop(2), 30)
        self.assertFalse(t_list.search(60))

    def test_simple_everything_1(self):
        """Testing for 100% coverage"""
        t_list = OrderedList()
        t_list.add(10)
        t_list.add(20)
        t_list.add(30)
        t_list.add(5)

        self.assertEqual(t_list.python_list(), [5, 10, 20, 30])

    def test_simple_everything_2(self):
        """index issue"""
        t_list = OrderedList()
        self.assertEqual(t_list.python_list_reversed(), [])

    def test_simple_everything_3(self):
        """Testing for failing other people's test"""
        t_list = OrderedList()
        self.assertTrue(t_list.is_empty())
        self.assertEqual(t_list.python_list(), [])
        self.assertEqual(t_list.python_list_reversed(), [])
        self.assertRaises(IndexError, t_list.pop, 0)  # used to check for exception
        self.assertEqual(t_list.index(60), None)  # doesn't exist

        t_list.add(10)
        self.assertFalse(t_list.add(10))
        self.assertEqual(t_list.size(), 1)
        self.assertEqual(t_list.index(10), 0)
        self.assertTrue(t_list.search(10))
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.python_list_reversed(), [10])
        self.assertEqual(t_list.pop(0), 10)
        t_list.add(10)
        self.assertTrue(t_list.remove(10))
        self.assertFalse(t_list.remove(10))
        self.assertRaises(IndexError, t_list.pop, 0)  # used to check for exception
        self.assertRaises(IndexError, t_list.pop, -1)  # used to check for exception
        self.assertRaises(IndexError, t_list.pop, 1)  # used to check for exception
        t_list.add(10)

        t_list.add(20)
        self.assertFalse(t_list.add(20))
        self.assertEqual(t_list.size(), 2)
        self.assertEqual(t_list.index(10), 0)
        self.assertEqual(t_list.index(20), 1)
        self.assertTrue(t_list.search(10))
        self.assertTrue(t_list.search(20))
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.python_list(), [10, 20])
        self.assertEqual(t_list.python_list_reversed(), [20, 10])
        self.assertEqual(t_list.pop(1), 20)
        t_list.add(20)
        self.assertTrue(t_list.remove(20))
        self.assertFalse(t_list.remove(20))
        self.assertRaises(IndexError, t_list.pop, -1)  # used to check for exception
        self.assertRaises(IndexError, t_list.pop, 1)  # used to check for exception
        self.assertTrue(t_list.add(20))

        self.assertTrue(t_list.add(15))
        self.assertEqual(t_list.python_list(), [10, 15, 20])
        self.assertEqual(t_list.python_list_reversed(), [20, 15, 10])
        self.assertEqual(t_list.size(), 3)
        self.assertEqual(t_list.index(10), 0)
        self.assertEqual(t_list.index(15), 1)
        self.assertEqual(t_list.index(20), 2)
        self.assertRaises(IndexError, t_list.pop, -1)
        self.assertEqual(t_list.pop(0), 10)
        self.assertTrue(t_list.remove(20))
        self.assertTrue(t_list.remove(15))
        self.assertTrue(t_list.is_empty())
        self.assertEqual(t_list.python_list(), [])

    def test_simple_everything_3(self):
        """Testing for failing other people's test"""
        t_list = OrderedList()
        self.assertTrue(t_list.is_empty())
        self.assertEqual(t_list.python_list(), [])
        self.assertEqual(t_list.python_list_reversed(), [])
        self.assertRaises(IndexError, t_list.pop, 0)  # used to check for exception
        self.assertEqual(t_list.index(60), None)  # doesn't exist

        t_list.add("poop")
        self.assertFalse(t_list.add("poop"))
        self.assertEqual(t_list.size(), 1)
        self.assertEqual(t_list.index("poop"), 0)
        self.assertTrue(t_list.search("poop"))
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.python_list(), ["poop"])
        self.assertEqual(t_list.python_list_reversed(), ["poop"])
        self.assertEqual(t_list.pop(0), "poop")
        t_list.add("poop")
        self.assertTrue(t_list.remove("poop"))
        self.assertFalse(t_list.remove("poop"))
        self.assertRaises(IndexError, t_list.pop, 0)  # used to check for exception
        self.assertRaises(IndexError, t_list.pop, -1)  # used to check for exception
        self.assertRaises(IndexError, t_list.pop, 1)  # used to check for exception
        t_list.add("poop")


if __name__ == '__main__':
    unittest.main()
