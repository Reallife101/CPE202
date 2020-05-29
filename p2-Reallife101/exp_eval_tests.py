# Start of unittest - add to completely test functions in exp_eval

import unittest
from exp_eval import *


class test_expressions(unittest.TestCase):
    def test_postfix_eval_01(self):
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)

    def test_postfix_eval_02(self):
        try:
            postfix_eval("blah")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_03(self):
        try:
            postfix_eval("4 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_04(self):
        try:
            postfix_eval("1 2 3 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")


    def test_postfix_eval_expon(self):
        """Testing exponent orders and its variations"""
        self.assertAlmostEqual(postfix_eval(infix_to_postfix("2 ** 3 ** 2")), 512)
        self.assertAlmostEqual(postfix_eval(infix_to_postfix("2 ** 3")), 8)
        self.assertAlmostEqual(postfix_eval(infix_to_postfix("2 ** 3 ** 2 + 5")), 517)
        self.assertAlmostEqual(postfix_eval(infix_to_postfix("5 + 2 ** 3 ** 2")), 517)
        self.assertAlmostEqual(postfix_eval(infix_to_postfix("3 ** 2 ** 1")), 9)


    def test_postfix_eval_basic_op(self):
        """Testing normal operators operands"""
        self.assertAlmostEqual(postfix_eval(infix_to_postfix("4 - 2")), 2)
        self.assertAlmostEqual(postfix_eval(infix_to_postfix("4 * 2")), 8)
        self.assertAlmostEqual(postfix_eval(infix_to_postfix("4 / 2")), 2)

        self.assertRaises(ValueError, postfix_eval, infix_to_postfix("4 / 0"))  # used to check for exception

    def test_postfix_eval_bitshift(self):
        """Testing bitshift operands"""
        self.assertAlmostEqual(postfix_eval(infix_to_postfix("120 << 2")), 480)
        self.assertAlmostEqual(postfix_eval(infix_to_postfix("120 << 2 + 1")), 481)
        self.assertAlmostEqual(postfix_eval(infix_to_postfix("1 + 120 << 2")), 481)

        try:
            postfix_eval("3 3 / 1 >>")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")

        try:
            postfix_eval(infix_to_postfix("( 3 / 3 ) << 3"))
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")

        self.assertAlmostEqual(postfix_eval(infix_to_postfix("120 >> 2")), 30)
        self.assertAlmostEqual(postfix_eval(infix_to_postfix("120 >> 2 + 1")), 31)
        self.assertAlmostEqual(postfix_eval(infix_to_postfix("1 + 120 >> 2")), 31)

    def test_infix_to_postfix_01(self):
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")
        self.assertEqual(infix_to_postfix("6"), "6")
        self.assertEqual(infix_to_postfix("3 + 4 * 2 / ( 1 - 5 ) ** 2 ** 3"), "3 4 2 * 1 5 - 2 3 ** ** / +")

    def test_infix_to_postfix_02(self):
        """testing the basic functions"""
        self.assertEqual(infix_to_postfix("3 + 4 * 2 / ( 1 - 5 ) ** 2 ** 3"), "3 4 2 * 1 5 - 2 3 ** ** / +")

    def test_prefix_to_postfix(self):
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")


if __name__ == "__main__":
    unittest.main()
