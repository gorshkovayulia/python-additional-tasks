import unittest
from bubble_sorting import sorting

class ListTestCase(unittest.TestCase):
    """Tests for bubble sorting"""

    def test_sorting_list_with_integers_returns_sorted_list(self):
        list = [4, -2, 0, 10]
        sorting(list)
        self.assertEqual([-2, 0, 4, 10], list)

    def test_sorting_list_with_decimal_numbers_returns_sorted_list(self):
        list = [4.88, -2.5, 4.89, 3.7, 0]
        sorting(list)
        self.assertEqual([-2.5, 0, 3.7, 4.88, 4.89], list)

    def test_sorting_list_with_one_number_returns_list_with_one_number(self):
        list = [5]
        sorting(list)
        self.assertEqual(5,5)

    def test_sorting_list_with_words_returns_sorted_list(self):
        list = ['Karl', 'Joseph', 'Mike']
        sorting(list)
        self.assertEqual(['Joseph', 'Karl', 'Mike'], list)

    def test_sorting_list_with_one_word_returns_list_with_one_word(self):
        list = ['Karl']
        sorting(list)
        self.assertEqual(['Karl'],list)

    def test_sorting_empty_list_returns_empty_list(self):
        list = []
        sorting(list)
        self.assertEqual([], list)

    def test_sorting_none_value_returns_exception(self):
        list = None
        try:
            sorting(list)
            self.fail('Should be an exception')
        except Exception:
            pass

    def test_sorting_list_with_words_and_numbers_returns_error(self):
        list = ['Niki', 10, 'Emma']
        try:
            sorting(list)
            self.fail('Should be an error')
        except TypeError:
            pass

if __name__ == "__main__":
    unittest.main()
