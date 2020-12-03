import unittest
from dimensions import Dimensions

class TestDimensions(unittest.TestCase):

    def test_dimensions_with_none_values_raise_type_error(self):
        try:
            Dimensions(None, None)
            self.fail("Should be an exception")
        except TypeError as e:
            self.assertEqual("Number of rows or number of columns is absent!", str(e))

    def test_dimensions_with_zero_values_raise_value_error(self):
        try:
            Dimensions(0, 0)
            self.fail("Should be an exception")
        except ValueError as e:
            self.assertEqual("Number of rows and number of columns cannot be less or equal 0!", str(e))

    def test_dimensions_with_negative_values_raise_value_error(self):
        try:
            Dimensions(-7, -8)
            self.fail("Should be an exception")
        except ValueError as e:
            self.assertEqual("Number of rows and number of columns cannot be less or equal 0!", str(e))

    def test_dimensions_with_decimal_values_raise_type_error(self):
        try:
            Dimensions(1.5, 5.2)
            self.fail("Should be an exception")
        except TypeError as e:
            self.assertEqual("Number of rows and number of columns must be int!", str(e))

    def test_dimensions_with_str_values_raise_type_error(self):
        try:
            Dimensions('test', 'test')
            self.fail("Should be an exception")
        except TypeError as e:
            self.assertEqual("Number of rows and number of columns must be int!", str(e))

    def test_384_plate_size_is_returned_for_16_rows_and_24_columns(self):
        dimensions = Dimensions(16, 24)
        self.assertEqual(384, dimensions.get_capacity())

if __name__ == "__main__":
    unittest.main()