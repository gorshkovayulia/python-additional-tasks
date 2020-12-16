import unittest
from bubble_sorting.bubble_sorting import sorting

class BubbleSortingTestCase(unittest.TestCase):
    """Tests for bubble sorting"""

    def test_list_with_integers_should_be_sorted_in_ascending_order(self):
        list = [10, 4, -2, 0, 10]
        sorting(list)
        self.assertEqual([-2, 0, 4, 10, 10], list)

    def test_list_with_decimal_numbers_should_be_sorted_in_ascending_order(self):
        list = [4.88, -2.5, 4.89, 3.7]
        sorting(list)
        self.assertEqual([-2.5, 3.7, 4.88, 4.89], list)

    def test_list_with_negative_numbers_should_be_sorted_in_ascending_order(self):
        list = [-1, -0.58, -100, -2.64]
        sorting(list)
        self.assertEqual([-100, -2.64, -1, -0.58], list)

    def test_sorting_of_list_with_one_number_returns_list_with_one_number(self):
        list = [5]
        sorting(list)
        self.assertEqual([5], list)

    def test_list_with_words_should_be_sorted_in_alphabetical_order(self):
        list = ['karl', 'joseph', 'mike']
        sorting(list)
        self.assertEqual(['joseph', 'karl', 'mike'], list)

    def test_list_with_capitalized_words_should_be_sorted_in_aplhabetical_order(self):
        list = ['KARL', 'ALFRED', 'GREG', 'RYAN']
        sorting(list)
        self.assertEqual(['ALFRED', 'GREG', 'KARL', 'RYAN'], list)

    def test_list_with_words_where_there_are_lowercase_and_uppercase_letters_should_be_sorted_in_alphabetical_order(self):
        list = ['karl', 'KARL', 'Karl', 'kArl']
        sorting(list)
        self.assertEqual(['KARL', 'Karl', 'kArl', 'karl'], list)

    def test_list_with_elements_where_there_are_letters_and_numbers_should_be_sorted_by_numbers_and_than_by_letters_in_alph_order(self):
        list = ['Karl9', 'karl1', 'kArl5', '0Karl', '-2karl', '0KArl']
        sorting(list)
        self.assertEqual(['-2karl', '0KArl', '0Karl', 'Karl9', 'kArl5', 'karl1'], list)

    def test_sorting_of_list_with_one_word_returns_list_with_one_word(self):
        list = ['Karl']
        sorting(list)
        self.assertEqual(['Karl'], list)

    def test_sorting_of_list_with_words_and_numbers_raises_TypeError(self):
        list = ['Niki', 10, 'Emma']
        try:
            sorting(list)
            self.fail("Should be an error")
        except TypeError as e:
            str(e)
            self.assertEqual("'>' not supported between instances of 'str' and 'int'", str(e))

    def test_sorting_of_empty_list_does_not_raise_error(self):
        list = []
        sorting(list)
        self.assertEqual([], list)

    def test_sorting_of_none_value_raises_TypeError(self):
        list = None
        try:
            sorting(list)
            self.fail("Should be an exception")
        except TypeError as e:
            str(e)
            self.assertEqual("No list!", str(e))

if __name__ == "__main__":
    unittest.main()