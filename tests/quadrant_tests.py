import unittest
from plates.quadrant import Quadrant

class TestQuadrants(unittest.TestCase):

    def test_negative_start_row_raises_value_error(self):
        try:
            Quadrant(-1, 0)
            self.fail("Should be an exception")
        except ValueError as e:
            self.assertEqual("Start row and start column cannot be less than 0!", str(e))

    def test_negative_start_column_raises_value_error(self):
        try:
            Quadrant(0, -1)
            self.fail("Should be an exception")
        except ValueError as e:
            self.assertEqual("Start row and start column cannot be less than 0!", str(e))

    def test_negative_start_column_and_start_row_raise_value_error(self):
        try:
            Quadrant(-1, -1)
            self.fail("Should be an exception")
        except ValueError as e:
            self.assertEqual("Start row and start column cannot be less than 0!", str(e))

    def test_value_error_appears_if_start_row_is_more_than_1(self):
        try:
            Quadrant(2, 0)
            self.fail("Should be an exception")
        except ValueError as e:
            self.assertEqual("Start row and start column cannot be qreater than 1!", str(e))

    def test_value_error_appears_if_start_column_is_more_than_1(self):
        try:
            Quadrant(0, 2)
            self.fail("Should be an exception")
        except ValueError as e:
            self.assertEqual("Start row and start column cannot be qreater than 1!", str(e))

    def test_value_error_appears_if_start_row_and_start_column_are_more_than_1(self):
        try:
            Quadrant(2, 2)
            self.fail("Should be an exception")
        except ValueError as e:
            self.assertEqual("Start row and start column cannot be qreater than 1!", str(e))

    def test_type_error_appears_if_start_row_is_decimal_number(self):
        try:
            Quadrant(0.5, 1)
            self.fail("Should be an exception")
        except TypeError as e:
            self.assertEqual("Start row and start column must be int!", str(e))

    def test_type_error_appears_if_start_column_is_decimal_number(self):
        try:
            Quadrant(1, 0.5)
            self.fail("Should be an exception")
        except TypeError as e:
            self.assertEqual("Start row and start column must be int!", str(e))

    def test_type_error_appears_if_start_column_and_start_row_are_decimal_numbers(self):
        try:
            Quadrant(0.5, 0.5)
            self.fail("Should be an exception")
        except TypeError as e:
            self.assertEqual("Start row and start column must be int!", str(e))

    def test_type_error_appears_if_start_row_is_none(self):
        try:
            Quadrant(None, 1)
            self.fail("Should be an exception")
        except TypeError as e:
            self.assertEqual("Start row or start column are absent!", str(e))

    def test_type_error_appears_if_start_column_is_none(self):
        try:
            Quadrant(1, None)
            self.fail("Should be an exception")
        except TypeError as e:
            self.assertEqual("Start row or start column are absent!", str(e))

    def test_type_error_appears_if_start_column_and_start_row_are_none(self):
        try:
            Quadrant(None, None)
            self.fail("Should be an exception")
        except TypeError as e:
            self.assertEqual("Start row or start column are absent!", str(e))

    def test_type_error_appears_if_start_row_is_text(self):
        try:
            Quadrant('test', 1)
            self.fail("Should be an exception")
        except TypeError as e:
            self.assertEqual("'<' not supported between instances of 'str' and 'int'", str(e))

    def test_type_error_appears_if_start_column_is_text(self):
        try:
            Quadrant(1, 'test')
            self.fail("Should be an exception")
        except TypeError as e:
            self.assertEqual("'<' not supported between instances of 'str' and 'int'", str(e))

    def test_type_error_appears_if_start_column_and_start_row_are_text(self):
        try:
            Quadrant('test', 'test')
            self.fail("Should be an exception")
        except TypeError as e:
            self.assertEqual("'<' not supported between instances of 'str' and 'int'", str(e))

if __name__ == "__main__":
    unittest.main()