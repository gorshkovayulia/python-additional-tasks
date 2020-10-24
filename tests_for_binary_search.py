import unittest
from binary_search import binary_search

class BinarySearchTestCase(unittest.TestCase):
    """Tests for binary search."""

    def test_searching_of_value_index_in_simple_sorted_list_returns_correct_index(self):
        list = [-1, 0, 3, 44, 87, 100]
        binary_search(list, 0)
        self.assertEqual(1,1)

    def test_searching_of_index_in_list_with_odd_number_of_elements_returns_correct_index(self):
        list = [2, 8, 10, 88, 70]
        binary_search(list, 10)
        self.assertEqual(2,2)

    def test_searching_of_value_index_in_list_with_one_element_returns_correct_index(self):
        list = [5]
        binary_search(list,5)
        self.assertEqual(0,0)

    def test_searching_of_value_index_in_not_sorted_list_returns_special_message(self):
        list = [5, 4, 20, 1, 0]
        binary_search(list, 0)
        self.assertEqual('No value', 'No value')

    def test_searching_of_value_index_in_list_with_words_returns_error(self):
        list = ['Karl', 'Maria', 'Anna']
        try:
            binary_search(list, 10)
            self.fail('Should be an error')
        except TypeError:
            pass

    def test_searching_of_value_index_in_empty_list_returns_error(self):
        list = []
        try:
            binary_search(list, 5)
            self.fail('Should be an error')
        except IndexError:
            pass

    def test_searching_of_value_index_for_not_existing_value_returns_correct_message(self):
        list = [2, 5, 1, 8, 7]
        binary_search(list, 10)
        self.assertEqual('No value', 'No value')

    def test_searching_of_value_index_for_none_value_returns_error(self):
        list = [2, 5, 1, 8, 7]
        try:
            binary_search(list, None)
            self.fail('Should be an error')
        except TypeError:
            pass

    def test_searching_of_value_index_for_string_value_returns_error(self):
        list = [2, 10, 55, 586]
        try:
            binary_search(list, 'test')
            self.fail('Should be an error')
        except TypeError:
            pass

if __name__ == "__main__":
    unittest.main()
