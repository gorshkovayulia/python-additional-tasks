import unittest
from binary_search import binary_search

class BinarySearchTestCase(unittest.TestCase):
    """Tests for binary search."""

    def test_looking_for_value_in_list_sorted_in_ascending_order_returns_correct_index(self):
        list = [-1, 0, 3, 44, 87, 100]
        id = binary_search(list, 0)
        self.assertEqual(id, 1)

    def test_correct_index_is_returned_in_case_the_searching_value_corresponds_to_the_calculated_middle_value_of_list(self):
        list = [2, 3, 4, 10]
        id = binary_search(list, 4)
        self.assertEqual(id, 2)

    def test_looking_for_value_in_list_with_odd_number_of_elements_returns_correct_index(self):
        list = [2, 8, 10, 88, 70]
        id = binary_search(list, 10)
        self.assertEqual(id, 2)

    def test_looking_for_index_for_the_smallest_number_in_list_returns_zero_index(self):
        list = [-5, 10, 120, 300]
        id = binary_search(list, -5)
        self.assertEqual(id, 0)

    def test_looking_for_index_for_the_biggest_number_in_list_returns_the_biggest_index(self):
        list = [-5, 10, 120, 300]
        id = binary_search(list, 300)
        self.assertEqual(id, 3)

    def test_looking_for_value_in_list_with_one_element_returns_zero_index(self):
        list = [5]
        id = binary_search(list, 5)
        self.assertEqual(id, 0)

    def test_looking_for_value_of_int_type_in_list_of_strings_raises_error(self):
        list = ['Karl', 'Maria', 'Anna']
        try:
            binary_search(list, 10)
            self.fail('Should be an error')
        except TypeError:
            self.assertEqual("'>' not supported between instances of 'int' and 'str'", "'>' not supported between instances of 'int' and 'str'")

    def test_looking_for_value_in_empty_list_raises_error(self):
        list = []
        try:
            binary_search(list, 5)
            self.fail('Should be an error')
        except IndexError:
            self.assertEqual("list index out of range", "list index out of range")

    def test_looking_for_not_existing_value_does_not_return_index(self):
        list = [2, 5, 10, 87, 700]
        value = binary_search(list, 150)
        self.assertEqual(-1, value)

    def test_looking_for_value_in_list_sorted_in_descending_order_does_not_return_index(self):
        list = [100, 50, 20, 1]
        value = binary_search(list, 100)
        self.assertEqual(-1, value)

    def test_looking_for_none_value_raises_error(self):
        list = [2, 5, 1, 8, 7]
        try:
            binary_search(list, None)
            self.fail('Should be an error')
        except TypeError:
            self.assertEqual("'>' not supported between instances of 'NoneType' and 'int'", "'>' not supported between instances of 'NoneType' and 'int'")

    def test_looking_for_word_in_list_of_numbers_raises_error(self):
        list = [2, 10, 55, 586]
        try:
            binary_search(list, 'test')
            self.fail('Should be an error')
        except TypeError:
            self.assertEqual("'>' not supported between instances of 'str' and 'int'", "'>' not supported between instances of 'str' and 'int'")

if __name__ == "__main__":
    unittest.main()
