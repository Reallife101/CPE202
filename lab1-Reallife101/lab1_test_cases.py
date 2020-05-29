import unittest
from lab1 import *


# A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """Testing for raise Value if the list is empty"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_max_list_iter_general_test(self):
        """Just checking to make sure that the code itself works with a basic case"""
        self.assertEqual(max_list_iter([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_list_iter([1, 5, 7, 8, 10]), 10)
        self.assertEqual(max_list_iter([2, 5, 7, 10, 12]), 12)

    def test_max_list_iter_out_of_order_test(self):
        """check to see if code works for lists not in order"""
        self.assertEqual(max_list_iter([10, 5, 7, 8, 1]), 10)
        self.assertEqual(max_list_iter([2, 10, 7, 8, 1]), 10)
        self.assertEqual(max_list_iter([2, 3, 10, 8, 1]), 10)
        self.assertEqual(max_list_iter([2, 4, 7, 10, 1]), 10)
        self.assertEqual(max_list_iter([2, 5, 7, 8, 10]), 10)

    def test_max_list_iter_double_max_test(self):
        """Checking case of multiple maxes"""
        self.assertEqual(max_list_iter([10, 5, 7, 8, 10]), 10)

    def test_max_list_of_1_test(self):
        """Checking case of multiple maxes"""
        self.assertEqual(max_list_iter([5]), 5)  # given list of 1, find 1

    def test_max_of_neg_test(self):
        """Checking case of only negatives in list"""
        self.assertEqual(max_list_iter([-1, -2, -3, -4, -5]), -1)  # Biggest of negatives

    def test_max_Empty_List_of_None_test(self):
        """Checking case of multiple maxes"""
        self.assertEqual(max_list_iter([]), None)  # Empty List

    # Testing Reverse Recursion Function
    def test_reverse_rec(self):
        """Checking for basic coding functioning"""
        self.assertEqual(reverse_rec([1, 2, 3]), [3, 2, 1])
        self.assertEqual(reverse_rec([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])

    def test_reverse_rec_neg(self):
        """Checking for function when negative"""
        self.assertEqual(reverse_rec([-1, -2, -3]), [-3, -2, -1])
        self.assertEqual(reverse_rec([-1, -2, -3, -4, -5]), [-5, -4, -3, -2, -1])

    def test_reverse_rec_out_of_order(self):
        """Checking for function when list is out of order"""
        self.assertEqual(reverse_rec([-1, -3, -2]), [-2, -3, -1])

    def test_reverse_rec_empty(self):
        """Checking for function when list is empty"""
        self.assertEqual(reverse_rec([]), [])

    def test_reverse_rec_none(self):
        """Checking for function when list is None"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(tlist)

    # Testing Binary Search Function
    def test_bin_search(self):
        """Checking for basic coding functioning"""
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(4, 0, len(list_val) - 1, list_val), 4)
        self.assertEqual(bin_search(10, 0, len(list_val) - 1, list_val), 8)

    def test_bin_search_None(self):
        """Checking for None"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            self.assertEqual(bin_search(4, 0, 10, tlist), 4)

    def test_bin_search_DNE(self):
        """Checking for answers where it should be none"""
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(10, 0, len(list_val) - 2, list_val), None)  # DNE
        self.assertEqual(bin_search(4, 5, len(list_val) - 1, list_val), None)  # DNE

    def test_bin_search_Find_First_Value(self):
        """Checking for being able find the target if it is the first value"""
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(0, 0, len(list_val) - 1, list_val), 0)  # First Value find

    def test_bin_search_Find_First_Value2(self):
        """Checking for being able find the target if it is the first value"""
        list_val = [3, 4, 5, 6, 7, 8, 9, 10, 11]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(3, 0, len(list_val) - 1, list_val), 0)  # First Value find

    def test_bin_search_0_to_0(self):
        """Checking for being able to handle going from 0 to 0"""
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(4, 0, 0, list_val), None)  # Handle going from 0 to 0

    def test_bin_search_Empty_List(self):
        """Checking for being able to handle an Empty List"""
        self.assertEqual(bin_search(4, 0, 0, []), None)  # handle Empty List
        self.assertEqual(bin_search(4, 0, len([4]) - 1, [4]), 0)  # Finding 1 result in a list of 1

    def test_bin_search_none(self):
        """Checking for function when list is None"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(tlist)

    def test_bin_search_all_sameish(self):
        """Checking for function when all numbers are the target besides a few"""
        list_val = [0, 4, 4, 10]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(4, 0, len(list_val) - 1, list_val), 1 or 2)  
        
    def test_bin_search_high_low(self):
        """Checking for being able to handle target at start and end"""
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(0, 0, len(list_val) - 1, list_val), 0)
        self.assertEqual(bin_search(10, 0, len(list_val) - 1, list_val), 8)

if __name__ == "__main__":
    unittest.main()
