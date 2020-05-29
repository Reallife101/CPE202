from hash_quad import *
import string


class Concordance:

    def __init__(self):
        self.stop_table = None  # hash table for stop words
        self.concordance_table = None  # hash table for concordance

    def load_stop_table(self, filename):
        """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
        Starting size of hash table should be 191: self.stop_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        self.stop_table = HashTable(191)

        try:  # Catching error
            with open(filename, "r") as f:
                for line in f:
                    line = line.lower()
                    line = line.replace("'", "")
                    for char in string.punctuation:
                        line = line.replace(char, " ")
                    words = line.split()
                    for val in words:
                        if val.isalpha():
                            self.stop_table.insert(val)
        except FileNotFoundError as error:
            raise error

    def load_concordance_table(self, filename):
        """ Read words from input text file (filename) and insert them into the concordance hash table, 
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)
        Starting size of hash table should be 191: self.concordance_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""

        self.concordance_table = HashTable(191)

        try:  # Catching error
            with open(filename, "r") as f:
                line_num = 0
                for line in f:
                    line_num += 1
                    line = line.lower()
                    line = line.replace("'", "")
                    for char in string.punctuation:
                        line = line.replace(str(char), " ")
                    words = line.split()

                    res = [i for n, i in enumerate(words) if i not in words[:n]]

                    for val in res:
                        if val.isalpha():
                            if not self.stop_table.in_table(val):
                                if self.concordance_table.in_table(val):
                                    # print(str(val)+" "+ str(self.concordance_table.get_value(val)))
                                    list = self.concordance_table.get_value(val)
                                    list.append(line_num)
                                    self.concordance_table.insert(val, list)
                                else:
                                    # print("val ="+str(val)+" line_num = "+str(line_num))
                                    self.concordance_table.insert(val, [line_num])
                                    # print(str(val)+" "+ str(self.concordance_table.get_value(val)))
        except FileNotFoundError as error:
            raise error

    def write_concordance(self, filename):
        """ Write the concordance entries to the output file(filename)
        See sample output files for format."""
        final_file = open(filename, 'w+')
        keys = self.concordance_table.get_all_keys()
        keys.sort()

        if self.concordance_table.get_num_items() == 0:
            final_file.close()
            return

        final_string = str(keys[0]) + ":"
        for line in self.concordance_table.get_value(keys[0]):
            final_string += " " + str(line)
        final_file.write(final_string)

        for val in keys[1:]:
            final_string = str(val) + ":"
            for line in self.concordance_table.get_value(val):
                final_string += " " + str(line)
            final_file.write("\n" + final_string)

        final_file.close()
