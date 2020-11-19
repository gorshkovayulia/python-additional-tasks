import unittest
from plate import PlateCell
from plate import Dimensions

class TestPlateCell(unittest.TestCase):
    """Tests for PlateCell class"""

    def test_first_row_and_first_column_are_returned_for_the_first_cell(self):
        dimensions = Dimensions(16, 24)
        cell = PlateCell(1, dimensions)
        row_and_column = cell.calculate_row_and_column()
        self.assertEqual((1, 1), row_and_column)

    def test_sixteenth_row_and_twelfth_column_are_returned_for_the_middle_cell(self):
        dimensions = Dimensions(16, 24)
        cell = PlateCell(192, dimensions)
        row_and_column = cell.calculate_row_and_column()
        self.assertEqual((16, 12), row_and_column)

    def test_sixteenth_row_and_twenty_fourth_column_are_returned_for_the_last_cell(self):
        dimensions = Dimensions(16, 24)
        cell = PlateCell(384, dimensions)
        row_and_column = cell.calculate_row_and_column()
        self.assertEqual((16, 24), row_and_column)

    def test_zero_cell_number_raises_value_error(self):
        dimensions = Dimensions(16, 24)
        try:
            cell = PlateCell(0, dimensions)
            number = cell.cell_number()
            self.fail("Should be an exception")
        except ValueError as e:
            str(e)
            self.assertEqual("Сell number cannot equal zero!", str(e))

    def test_negative_cell_number_raises_value_error(self):
        dimensions = Dimensions(16, 24)
        try:
            cell = PlateCell(-5, dimensions)
            number = cell.cell_number()
            self.fail("Should be an exception")
        except ValueError as e:
            str(e)
            self.assertEqual("Сell number cannot be negative!", str(e))

    def test_not_existing_cell_number_raises_value_error(self):
        dimensions = Dimensions(16, 24)
        try:
            cell = PlateCell(385, dimensions)
            number = cell.cell_number()
            self.fail("Should be an exception")
        except ValueError as e:
            str(e)
            self.assertEqual("385 cell number is too big for (16, 24) dimension!", str(e))

    def test_decimal_cell_number_raises_value_error(self):
        dimensions = Dimensions(16, 24)
        try:
            cell = PlateCell(1.65, dimensions)
            number = cell.cell_number()
            self.fail("Should be an exception")
        except TypeError as e:
            str(e)
            self.assertEqual("Сell number should be int!", str(e))

    def test_type_error_appears_in_case_absent_cell_number(self):
        dimensions = Dimensions(16, 24)
        try:
            cell = PlateCell(dimensions)
            number = cell.cell_number()
            self.fail("Should be an exception")
        except TypeError as e:
            str(e)
            self.assertEqual("__init__() missing 1 required positional argument: 'dimensions'", str(e))

    def test_type_error_appears_in_case_none_value_as_cell_number(self):
        dimensions = Dimensions(16, 24)
        try:
            cell = PlateCell(None, dimensions)
            number = cell.cell_number()
            self.fail("Should be an exception")
        except TypeError as e:
            str(e)
            self.assertEqual("Cell number cannot be None!", str(e))

    def test_value_error_appears_in_case_cell_number_is_text(self):
        dimensions = Dimensions(16, 24)
        try:
            cell = PlateCell('test', dimensions)
            number = cell.cell_number()
            self.fail("Should be an exception")
        except TypeError as e:
            str(e)
            self.assertEqual("Сell number should be int!", str(e))

    def test_A1_coordinate_is_returned_for_the_first_cell_on_384_plate(self):
        dimensions = Dimensions(16, 24)
        cell = PlateCell(1, dimensions)
        coordinate = cell.as_string()
        self.assertEqual('A1', coordinate)

    def test_P12_coordinate_is_returned_for_the_middle_cell_on_384_plate(self):
        dimensions = Dimensions(16, 24)
        cell = PlateCell(192, dimensions)
        coordinate = cell.as_string()
        self.assertEqual('P12', coordinate)

    def test_P24_coordinate_is_returned_for_the_last_cell_on_384_plate(self):
        dimensions = Dimensions(16, 24)
        cell = PlateCell(384, dimensions)
        coordinate = cell.as_string()
        self.assertEqual('P24', coordinate)

    def test_A1_coordinate_is_returned_for_the_first_cell_on_1536_plate


if __name__ == "__main__":
    unittest.main()