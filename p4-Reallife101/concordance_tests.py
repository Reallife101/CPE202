import unittest
import subprocess
from concordance import *


class TestList(unittest.TestCase):


    def test_01(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("file1.txt")
        conc.write_concordance("file1_con.txt")
        err = subprocess.call("diff -wb file1_con.txt file1_sol.txt", shell = True)
        self.assertEqual(err, 0)

    def test_FileNotFound_01(self):
        """Catching error"""
        conc = Concordance()
        try:
            conc.load_stop_table("DNE.txt")
            self.fail()
        except FileNotFoundError as e:
            pass

    def test_FileNotFound_02(self):
        """Catching error"""
        conc = Concordance()
        try:
            conc.load_concordance_table("DNE.txt")
            self.fail()
        except FileNotFoundError as e:
            pass


    def test_02(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("file2.txt")
        conc.write_concordance("file2_con.txt")
        err = subprocess.call("diff -wb file2_con.txt file2_sol.txt", shell = True)
        self.assertEqual(err, 0)


    def test_03(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("declaration.txt")
        conc.write_concordance("declaration_con.txt")
        err = subprocess.call("diff -wb declaration_con.txt declaration_sol.txt", shell = True)
        self.assertEqual(err, 0)

    def test_04(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("empty_file.txt")
        conc.write_concordance("empty_file_con.txt")
        err = subprocess.call("diff -wb empty_file_con.txt empty_file.txt", shell = True)
        self.assertEqual(err, 0)

    def test_05(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("one_char.txt")
        conc.write_concordance("one_char_con.txt")
        err = subprocess.call("diff -wb one_char_con.txt one_char_sol.txt", shell = True)
        self.assertEqual(err, 0)

    def test_06(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("duplicate.txt")
        conc.write_concordance("duplicate_con.txt")
        err = subprocess.call("diff -wb duplicate_con.txt duplicate_sol.txt", shell = True)
        self.assertEqual(err, 0)

    def test_07(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("newline.txt")
        conc.write_concordance("newline_con.txt")
        err = subprocess.call("diff -wb newline_con.txt newline_sol.txt", shell = True)
        self.assertEqual(err, 0)

    # def test_06(self):
    #     conc = Concordance()
    #     try:
    #         conc.load_stop_table("stop_words.txt")
    #         conc.load_concordance_table("dictionary_a-c.txt")
    #         conc.write_concordance("dictionary_a-c_con.txt")
    #         # for key in conc.concordance_table.get_all_keys():
    #         #     conc.concordance_table.get_index(key)
    #         #     conc.concordance_table.get_value(key)
    #         #     conc.concordance_table.in_table(key)
    #         #     conc.concordance_table.insert(key)
    #         #     conc.concordance_table.get_num_items()
    #         #     conc.concordance_table.get_table_size()
    #         #     conc.concordance_table.get_load_factor()
    #
    #         pass
    #     except FileNotFoundError as e:
    #         self.fail()
    #
    # def test_07(self):
    #     conc = Concordance()
    #     try:
    #         conc.load_stop_table("stop_words.txt")
    #         conc.load_concordance_table("War_And_Peace.txt")
    #         conc.write_concordance("War_And_Peace_con.txt")
    #         pass
    #     except FileNotFoundError as e:
    #         self.fail()

        
if __name__ == '__main__':
    unittest.main()
