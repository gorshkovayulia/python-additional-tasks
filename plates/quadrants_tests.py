import unittest
from quadrants import Quadrants

class TestQuadrants(unittest.TestCase):
    """Tests for Quadrants class"""

    def test_start_row_with_0_value_is_saved(self):
        quadrants = Quadrants(0, 0)
        self.assertEqual(0, quadrants.start_row)

    def test_start_column_with_0_value_is_saved(self):
        quadrants = Quadrants(0, 0)
        self.assertEqual(0, quadrants.start_column)

    def test_start_row_with_1_value_is_saved(self):
        quadrants = Quadrants(1, 0)
        self.assertEqual(1, quadrants.start_row)

    def test_start_column_with_1_value_is_saved(self):
        quadrants = Quadrants(0, 1)
        self.assertEqual(1, quadrants.start_column)

    def test_negative_start_row_raises_value_error(self):
        try:
            quadrants = Quadrants(-1, 0)
            self.fail("Should be an exception")
        except ValueError as e:
            str(e)
            self.assertEqual("Start row and start column cannot be less than 0!", str(e))

    def test_negative_start_column_raises_value_error(self):
        try:
            quadrants = Quadrants(0, -1)
            self.fail("Should be an exception")
        except ValueError as e:
            str(e)
            self.assertEqual("Start row and start column cannot be less than 0!", str(e))

    def test_negative_start_column_and_start_row_raise_value_error(self):
        try:
            quadrants = Quadrants(-1, -1)
            self.fail("Should be an exception")
        except ValueError as e:
            str(e)
            self.assertEqual("Start row and start column cannot be less than 0!", str(e))

    def test_value_error_appears_if_start_row_is_more_than_1(self):
        try:
            quadrants = Quadrants(2, 0)
            self.fail("Should be an exception")
        except ValueError as e:
            str(e)
            self.assertEqual("Start row and start column cannot be more than 1!", str(e))

    def test_value_error_appears_if_start_column_is_more_than_1(self):
        try:
            quadrants = Quadrants(0, 2)
            self.fail("Should be an exception")
        except ValueError as e:
            str(e)
            self.assertEqual("Start row and start column cannot be more than 1!", str(e))

    def test_value_error_appears_if_start_row_and_start_column_are_more_than_1(self):
        try:
            quadrants = Quadrants(2, 2)
            self.fail("Should be an exception")
        except ValueError as e:
            str(e)
            self.assertEqual("Start row and start column cannot be more than 1!", str(e))

    def test_type_error_appears_if_start_row_is_decimal_number(self):
        try:
            quadrants = Quadrants(0.5, 1)
            self.fail("Should be an exception")
        except TypeError as e:
            str(e)
            self.assertEqual("Start row and start column should be int!", str(e))

    def test_type_error_appears_if_start_column_is_decimal_number(self):
        try:
            quadrants = Quadrants(1, 0.5)
            self.fail("Should be an exception")
        except TypeError as e:
            str(e)
            self.assertEqual("Start row and start column should be int!", str(e))

    def test_type_error_appears_if_start_column_and_start_row_are_decimal_numbers(self):
        try:
            quadrants = Quadrants(0.5, 0.5)
            self.fail("Should be an exception")
        except TypeError as e:
            str(e)
            self.assertEqual("Start row and start column should be int!", str(e))

    def test_type_error_appears_if_start_row_is_none(self):
        try:
            quadrants = Quadrants(None, 1)
            self.fail("Should be an exception")
        except TypeError as e:
            str(e)
            self.assertEqual("Start row or start column are absent!", str(e))

    def test_type_error_appears_if_start_column_is_none(self):
        try:
            quadrants = Quadrants(1, None)
            self.fail("Should be an exception")
        except TypeError as e:
            str(e)
            self.assertEqual("Start row or start column are absent!", str(e))

    def test_type_error_appears_if_start_column_and_start_row_are_none(self):
        try:
            quadrants = Quadrants(None, None)
            self.fail("Should be an exception")
        except TypeError as e:
            str(e)
            self.assertEqual("Start row or start column are absent!", str(e))

    def test_type_error_appears_if_start_row_is_text(self):
        try:
            quadrants = Quadrants('test', 1)
            self.fail("Should be an exception")
        except TypeError as e:
            str(e)
            self.assertEqual("'<' not supported between instances of 'str' and 'int'", str(e))

    def test_type_error_appears_if_start_column_is_text(self):
        try:
            quadrants = Quadrants(1, 'test')
            self.fail("Should be an exception")
        except TypeError as e:
            str(e)
            self.assertEqual("'<' not supported between instances of 'str' and 'int'", str(e))

    def test_type_error_appears_if_start_column_and_start_row_are_text(self):
        try:
            quadrants = Quadrants('test', 'test')
            self.fail("Should be an exception")
        except TypeError as e:
            str(e)
            self.assertEqual("'<' not supported between instances of 'str' and 'int'", str(e))

if __name__ == "__main__":
    unittest.main()