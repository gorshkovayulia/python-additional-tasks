import unittest
from bubble_and_merge_sorting.bubble_and_merge_sorting import BubbleSorter, MergeSorter


class BubbleSorterTestCase(unittest.TestCase):

    def test_list_with_integers_should_be_sorted_in_ascending_order(self):
        list = [10, 4, -2, 0, 10]
        bubble_sorter = BubbleSorter()
        bubble_sorter.sort(list)
        self.assertEqual([-2, 0, 4, 10, 10], list)

    def test_list_with_decimal_numbers_should_be_sorted_in_ascending_order(self):
        list = [4.88, -2.5, 4.89, 3.7]
        bubble_sorter = BubbleSorter()
        bubble_sorter.sort(list)
        self.assertEqual([-2.5, 3.7, 4.88, 4.89], list)

    def test_list_with_negative_numbers_should_be_sorted_in_ascending_order(self):
        list = [-1, -0.58, -100, -2.64]
        bubble_sorter = BubbleSorter()
        bubble_sorter.sort(list)
        self.assertEqual([-100, -2.64, -1, -0.58], list)

    def test_sorting_of_list_with_one_number_returns_list_with_one_number(self):
        list = [5]
        bubble_sorter = BubbleSorter()
        bubble_sorter.sort(list)
        self.assertEqual([5], list)

    def test_list_with_words_should_be_sorted_in_alphabetical_order(self):
        list = ['karl', 'joseph', 'mike']
        bubble_sorter = BubbleSorter()
        bubble_sorter.sort(list)
        self.assertEqual(['joseph', 'karl', 'mike'], list)

    def test_list_with_capitalized_words_should_be_sorted_in_aplhabetical_order(self):
        list = ['KARL', 'ALFRED', 'GREG', 'RYAN']
        bubble_sorter = BubbleSorter()
        bubble_sorter.sort(list)
        self.assertEqual(['ALFRED', 'GREG', 'KARL', 'RYAN'], list)

    def test_list_with_words_where_there_are_lowercase_and_uppercase_letters_should_be_sorted_in_alphabetical_order(self):
        list = ['karl', 'KARL', 'Karl', 'kArl']
        bubble_sorter = BubbleSorter()
        bubble_sorter.sort(list)
        self.assertEqual(['KARL', 'Karl', 'kArl', 'karl'], list)

    def test_list_with_elements_where_there_are_letters_and_numbers_should_be_sorted_by_numbers_and_than_by_letters_in_alph_order(self):
        list = ['Karl9', 'karl1', 'kArl5', '0Karl', '-2karl', '0KArl']
        bubble_sorter = BubbleSorter()
        bubble_sorter.sort(list)
        self.assertEqual(['-2karl', '0KArl', '0Karl', 'Karl9', 'kArl5', 'karl1'], list)

    def test_sorting_of_list_with_one_word_returns_list_with_one_word(self):
        list = ['Karl']
        bubble_sorter = BubbleSorter()
        bubble_sorter.sort(list)
        self.assertEqual(['Karl'], list)

    def test_sorting_of_list_with_words_and_numbers_raises_TypeError(self):
        list = ['Niki', 10, 'Emma']
        bubble_sorter = BubbleSorter()
        try:
            bubble_sorter.sort(list)
            self.fail("Should be an error")
        except TypeError as e:
            str(e)
            self.assertEqual("'>' not supported between instances of 'str' and 'int'", str(e))

    def test_sorting_of_empty_list_does_not_raise_error(self):
        list = []
        bubble_sorter = BubbleSorter()
        bubble_sorter.sort(list)
        self.assertEqual([], list)

    def test_sorting_of_none_value_raises_TypeError(self):
        list = None
        bubble_sorter = BubbleSorter()
        try:
            bubble_sorter.sort(list)
            self.fail("Should be an exception")
        except TypeError as e:
            str(e)
            self.assertEqual("No list!", str(e))


class MergeSorterTestCase(unittest.TestCase):

    def test_sorting_of_empty_list_does_not_raise_error(self):
        list = []
        merge_sorter = MergeSorter()
        self.assertEqual([], merge_sorter.sort(list))

    def test_sorting_of_none_value_raises_TypeError(self):
        list = None
        merge_sorter = MergeSorter()
        try:
            merge_sorter.sort(list)
            self.fail("Should be an exception")
        except TypeError as e:
            str(e)
            self.assertEqual("No list!", str(e))

    def test_sorting_of_list_with_one_element_returns_list_with_one_element(self):
        list = [10]
        merge_sorter = MergeSorter()
        self.assertEqual([10], merge_sorter.sort(list))

    def test_list_with_two_elements_should_be_sorted_in_ascending_order(self):
        list = [5, 0]
        merge_sorter = MergeSorter()
        self.assertEqual([0, 5], merge_sorter.sort(list))

    def test_list_with_the_odd_number_of_elements_should_be_sorted_in_ascending_order(self):
        list = [10, -8, 20.5, 0, 9]
        merge_sorter = MergeSorter()
        self.assertEqual([-8, 0, 9, 10, 20.5], merge_sorter.sort(list))

    def test_list_should_be_sorted_in_ascending_order_if_right_sublist_is_out_of_elements(self):
        list = [10, 8, 9, 3, 1, 2]
        merge_sorter = MergeSorter()
        self.assertEqual([1, 2, 3, 8, 9, 10], merge_sorter.sort(list))

    def test_list_with_decimal_numbers_should_be_sorted_in_ascending_order(self):
        list = [3.1, 2.5, 1.4, 10.7, 9.9, 8.2]
        merge_sorter = MergeSorter()
        self.assertEqual([1.4, 2.5, 3.1, 8.2, 9.9, 10.7], merge_sorter.sort(list))

    def test_sorting_of_list_with_words_and_numbers_raises_TypeError(self):
        list = ['Niki', 10, 'Emma']
        merge_sorter = MergeSorter()
        try:
            merge_sorter.sort(list)
            self.fail("Should be an error")
        except TypeError as e:
            str(e)
            self.assertEqual("'<=' not supported between instances of 'int' and 'str'", str(e))

    def test_list_with_words_should_be_sorted_in_alphabetical_order(self):
        list = ['karl', 'joseph', 'mike']
        merge_sorter = MergeSorter()
        self.assertEqual(['joseph', 'karl', 'mike'], merge_sorter.sort(list))

    def test_list_with_capitalized_words_should_be_sorted_in_aplhabetical_order(self):
        list = ['KARL', 'ALFRED', 'GREG', 'RYAN']
        merge_sorter = MergeSorter()
        self.assertEqual(['ALFRED', 'GREG', 'KARL', 'RYAN'], merge_sorter.sort(list))

    def test_list_with_words_where_there_are_lowercase_and_uppercase_letters_should_be_sorted_in_alphabetical_order(self):
        list = ['karl', 'KARL', 'Karl', 'kArl']
        merge_sorter = MergeSorter()
        self.assertEqual(['KARL', 'Karl', 'kArl', 'karl'], merge_sorter.sort(list))

    def test_list_with_elements_where_there_are_letters_and_numbers_should_be_sorted_by_numbers_and_than_by_letters_in_alph_order(self):
        list = ['Karl9', 'karl1', 'kArl5', '0Karl', '-2karl', '0KArl']
        merge_sorter = MergeSorter()
        self.assertEqual(['-2karl', '0KArl', '0Karl', 'Karl9', 'kArl5', 'karl1'], merge_sorter.sort(list))

    def test_sorting_of_list_with_one_word_returns_list_with_one_word(self):
        list = ['Karl']
        merge_sorter = MergeSorter()
        self.assertEqual(['Karl'], merge_sorter.sort(list))


if __name__ == "__main__":
    unittest.main()