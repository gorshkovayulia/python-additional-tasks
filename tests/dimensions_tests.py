import unittest
from dimensions import Dimensions

class TestDimensions(unittest.TestCase):

    def test_dimension_with_none_value_raises_value_error(self):
        try:
            dimensions = Dimensions(None, 24)
            self.fail("Should be an exception")
        except TypeError as e:
            str(e)
            self.assertEqual("Number of rows or number of columns are absent!", str(e))

    def test_dimension_with_zero_values_raises_value_error(self):
        try:
            dimensions = Dimensions(0, 0)
            self.fail("Should be an exception")
        except ValueError as e:
            str(e)
            self.assertEqual("Number of rows and number of columns cannot be less or equal 0!", str(e))

    def test_not_existing_dimension_with_negative_values_raises_value_error(self):
        try:
            dimensions = Dimensions(-7, -8)
            self.fail("Should be an exception")
        except ValueError as e:
            str(e)
            self.assertEqual("Number of rows and number of columns cannot be less or equal 0!", str(e))

    def test_dimension_with_decimal_values_raises_value_error(self):
        try:
            dimensions = Dimensions(1.5, 5.2)
            self.fail("Should be an exception")
        except TypeError as e:
            str(e)
            self.assertEqual("Number of rows and number of columns should be int!", str(e))

    def test_384_size_is_returned_for_16_rows_and_24_columns(self):
        dimensions = Dimensions(16, 24)
        self.assertEqual(384, dimensions.get_capacity())

if __name__ == "__main__":
    unittest.main()