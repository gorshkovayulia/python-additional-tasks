import unittest
from plate import PlateCell
from plate import Dimensions

class TestPlateCell(unittest.TestCase):
    """Tests for PlateCell class"""

    """Tests for 'calculate_row_and_column' method"""

    def test_first_row_and_first_column_are_returned_for_the_first_cell(self):
        dimensions = Dimensions(16, 24)
        cell = PlateCell(0, dimensions)
        row_and_column = cell.calculate_row_and_column()
        self.assertEqual([0, 0], row_and_column)

    def test_sixteenth_row_and_twelfth_column_are_returned_for_the_middle_cell(self):
        dimensions = Dimensions(16, 24)
        cell = PlateCell(191, dimensions)
        row_and_column = cell.calculate_row_and_column()
        self.assertEqual([15, 11], row_and_column)

    def test_sixteenth_row_and_twenty_fourth_column_are_returned_for_the_last_cell(self):
        dimensions = Dimensions(16, 24)
        cell = PlateCell(383, dimensions)
        row_and_column = cell.calculate_row_and_column()
        self.assertEqual([15, 23], row_and_column)

    def test_zero_row_and_zero_column_are_returned_for_0_cell(self):
        dimensions = Dimensions(16, 24)
        cell = PlateCell(0, dimensions)
        row_and_column = cell.calculate_row_and_column()
        self.assertEqual([0, 0], row_and_column)

    def test_correct_row_and_column_are_returned_for_decimal_cell_number(self):
        dimensions = Dimensions(16, 24)
        cell = PlateCell(1.65, dimensions)
        row_and_column = cell.calculate_row_and_column()
        self.assertEqual([1, 0], row_and_column)

    def test_negative_cell_number_raises_error(self):
        dimensions = Dimensions(16, 24)
        try:
            cell = PlateCell(-5, dimensions)
            self.fail("Should be an exception")
        except AttributeError as e:
            str(e)
        self.assertEqual("Cell number cannot be negative!", str(e))

    def test_not_existing_cell_number_raises_error(self):
        dimensions = Dimensions(16, 24)
        try:
            cell = PlateCell(385, dimensions)
            self.fail("Should be an exception")
        except AttributeError as e:
            str(e)
            self.assertEqual("Cell number is too big for current dimension!", str(e))

    def test_type_error_appears_in_case_absent_cell_number(self):
        dimensions = Dimensions(16, 24)
        try:
            cell = PlateCell(dimensions)
            self.fail("Should be an exception")
        except TypeError as e:
            str(e)
            self.assertEqual("__init__() missing 1 required positional argument: 'dimensions'", str(e))

    def test_type_error_appears_in_case_none_value_as_cell_number(self):
        dimensions = Dimensions(16, 24)
        try:
            cell = PlateCell(None, dimensions)
            self.fail("Should be an exception")
        except TypeError as e:
            str(e)
            self.assertEqual("int() argument must be a string, a bytes-like object or a number, not 'NoneType'", str(e))

    def test_value_error_appears_in_case_cell_number_is_text(self):
        dimensions = Dimensions(16, 24)
        try:
            cell = PlateCell('test', dimensions)
            self.fail("Should be an exception")
        except ValueError as e:
            str(e)
            self.assertEqual("invalid literal for int() with base 10: 'test'", str(e))


    """Tests for 'as_string' method"""

    def test_correct_coordinate_for_the_first_cell_should_be_returned(self):
        dimensions = Dimensions(16, 24)
        cell = PlateCell(0, dimensions)
        coordinate = cell.as_string()
        self.assertEqual('A1', coordinate)

    def test_correct_coordinate_for_the_middle_cell_should_be_returned(self):
        dimensions = Dimensions(16, 24)
        cell = PlateCell(191, dimensions)
        coordinate = cell.as_string()
        self.assertEqual('P12', coordinate)

    def test_correct_coordinate_for_the_last_cell_should_be_returned(self):
        dimensions = Dimensions(16, 24)
        cell = PlateCell(383, dimensions)
        coordinate = cell.as_string()
        self.assertEqual('P24', coordinate)

    def test_none_is_returned_in_case_row_is_equal_to_0(self):
        dimensions = Dimensions(16, 24)
        cell = PlateCell(0, dimensions)
        coordinate = cell.as_string()
        self.assertEqual(None, coordinate)

    # """Tests for 'to_higher_density' method"""

if __name__ == "__main__":
    unittest.main()