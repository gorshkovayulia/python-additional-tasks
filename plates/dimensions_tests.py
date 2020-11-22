import unittest
from dimensions import Dimensions

class TestDimensions(unittest.TestCase):
    """Tests for Dimensions class"""

    def test_row_from_4_x_6_dimension_is_saved(self):
        dimensions = Dimensions(4, 6)
        self.assertEqual(4, dimensions.number_of_rows)

    def test_column_from_4_x_6_dimension_is_saved(self):
        dimensions = Dimensions(4, 6)
        self.assertEqual(6, dimensions.number_of_columns)

    def test_row_from_8_x_12_dimension_is_saved(self):
        dimensions = Dimensions(8, 12)
        self.assertEqual(8, dimensions.number_of_rows)

    def test_column_from_8_x_12_dimension_is_saved(self):
        dimensions = Dimensions(8, 12)
        self.assertEqual(12, dimensions.number_of_columns)

    def test_row_from_16_x_24_dimension_is_saved(self):
        dimensions = Dimensions(16, 24)
        self.assertEqual(16, dimensions.number_of_rows)

    def test_column_from_16_x_24_dimension_is_saved(self):
        dimensions = Dimensions(16, 24)
        self.assertEqual(24, dimensions.number_of_columns)

    def test_not_existing_dimension_raises_value_error(self):
        try:
            dimensions = Dimensions(7, 8)
            self.fail("Should be an exception")
        except ValueError as e:
            str(e)
            self.assertEqual("(7, 8) tuple is not acceptable! Available tuples are ((4, 6), (8, 12), (16, 24))", str(e))

    def test_dimension_with_zero_values_raises_value_error(self):
        try:
            dimensions = Dimensions(0, 0)
            self.fail("Should be an exception")
        except ValueError as e:
            str(e)
            self.assertEqual("(0, 0) tuple is not acceptable! Available tuples are ((4, 6), (8, 12), (16, 24))", str(e))

    def test_dimension_with_none_value_raises_value_error(self):
        try:
            dimensions = Dimensions(None, 0)
            self.fail("Should be an exception")
        except ValueError as e:
            str(e)
            self.assertEqual("(None, 0) tuple is not acceptable! Available tuples are ((4, 6), (8, 12), (16, 24))", str(e))

    def test_dimension_with_decimal_values_raises_value_error(self):
        try:
            dimensions = Dimensions(1.5, 5.2)
            self.fail("Should be an exception")
        except ValueError as e:
            str(e)
            self.assertEqual("(1.5, 5.2) tuple is not acceptable! Available tuples are ((4, 6), (8, 12), (16, 24))", str(e))

    def test_not_existing_dimension_with_negative_values_raises_value_error(self):
        try:
            dimensions = Dimensions(-7, -8)
            self.fail("Should be an exception")
        except ValueError as e:
            str(e)
            self.assertEqual("(-7, -8) tuple is not acceptable! Available tuples are ((4, 6), (8, 12), (16, 24))", str(e))

    def test_384_size_is_returned_for_16_rows_and_24_columns(self):
        dimensions = Dimensions(16, 24)
        self.assertEqual(384, dimensions.get_capacity())

if __name__ == "__main__":
    unittest.main()