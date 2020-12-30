import unittest

from plates.plate_cell import PlateCell
from plates.dimensions import Dimensions
from plates.quadrant import Quadrant


class TestPlateCell(unittest.TestCase):

    def test_zero_cell_number_raises_type_error(self):
        dimensions = Dimensions(16, 24)
        try:
            cell = PlateCell(0, dimensions)
            cell.cell_number()
            self.fail("Should be an exception")
        except TypeError as e:
            self.assertEqual("Cell number cannot be None!", str(e))

    def test_type_error_appears_in_case_none_value_as_cell_number(self):
        dimensions = Dimensions(16, 24)
        try:
            cell = PlateCell(None, dimensions)
            cell.cell_number()
            self.fail("Should be an exception")
        except TypeError as e:
            self.assertEqual("Cell number cannot be None!", str(e))

    def test_decimal_cell_number_raises_type_error(self):
        dimensions = Dimensions(16, 24)
        try:
            cell = PlateCell(1.65, dimensions)
            cell.cell_number()
            self.fail("Should be an exception")
        except TypeError as e:
            self.assertEqual("Cell number should be int!", str(e))

    def test_type_error_appears_in_case_cell_number_is_text(self):
        dimensions = Dimensions(16, 24)
        try:
            cell = PlateCell('test', dimensions)
            cell.cell_number()
            self.fail("Should be an exception")
        except TypeError as e:
            self.assertEqual("Cell number should be int!", str(e))

    def test_not_existing_cell_number_raises_value_error(self):
        dimensions = Dimensions(16, 24)
        try:
            cell = PlateCell(385, dimensions)
            cell.cell_number()
            self.fail("Should be an exception")
        except ValueError as e:
            self.assertEqual("385 cell number is too big for (16, 24) dimension!", str(e))

    def test_negative_cell_number_raises_value_error(self):
        dimensions = Dimensions(16, 24)
        try:
            cell = PlateCell(-5, dimensions)
            cell.cell_number()
            self.fail("Should be an exception")
        except ValueError as e:
            self.assertEqual("Cell number cannot be less than zero!", str(e))

    def test_first_row_and_first_column_are_returned_for_the_first_cell_in_384_plate_in_case_first_quadrant(self):
        dimensions = Dimensions(16, 24)
        cell = PlateCell(1, dimensions)
        self.assertEqual((0, 0), cell.calculate_row_and_column())

    def test_sixteenth_row_and_twelfth_column_are_returned_for_the_middle_cell_in_384_plate_in_case_first_quadrant(self):
        dimensions = Dimensions(16, 24)
        cell = PlateCell(192, dimensions)
        self.assertEqual((15, 11), cell.calculate_row_and_column())

    def test_sixteenth_row_and_twenty_fourth_column_are_returned_for_the_last_cell_in_384_plate_in_case_first_quadrant(self):
        dimensions = Dimensions(16, 24)
        cell = PlateCell(384, dimensions)
        self.assertEqual((15, 23), cell.calculate_row_and_column())

    def test_A01_coordinate_is_returned_for_the_first_cell_on_384_plate(self):
        dimensions = Dimensions(16, 24)
        cell = PlateCell(1, dimensions)
        self.assertEqual('A01', cell.as_string())

    def test_P09_coordinate_is_returned_for_the_middle_cell_on_384_plate(self):
        dimensions = Dimensions(16, 24)
        cell = PlateCell(144, dimensions)
        self.assertEqual('P09', cell.as_string())

    def test_P24_coordinate_is_returned_for_the_last_cell_on_384_plate(self):
        dimensions = Dimensions(16, 24)
        cell = PlateCell(384, dimensions)
        self.assertEqual('P24', cell.as_string())

    def test_first_cell_on_384_plate_corresponds_first_cell_on_1536_plate_in_case_first_quadrant(self):
        dimensions = Dimensions(16, 24)
        quadrant = Quadrant(0, 0)
        cell = PlateCell(1, dimensions)
        self.assertEqual(1, cell.to_higher_density(quadrant))

    def test_middle_cell_on_384_plate_corresponds_735_cell_on_1536_plate_in_case_first_quadrant(self):
        dimensions = Dimensions(16, 24)
        quadrant = Quadrant(0, 0)
        cell = PlateCell(192, dimensions)
        self.assertEqual(735, cell.to_higher_density(quadrant))

    def test_last_cell_on_384_plate_corresponds_1503_cell_on_1536_plate_in_case_first_quadrant(self):
        dimensions = Dimensions(16, 24)
        quadrant = Quadrant(0, 0)
        cell = PlateCell(384, dimensions)
        self.assertEqual(1503, cell.to_higher_density(quadrant))

    def test_first_cell_on_384_plate_corresponds_33_cell_on_1536_plate_in_case_second_quadrant(self):
        dimensions = Dimensions(16, 24)
        quadrant = Quadrant(0, 1)
        cell = PlateCell(1, dimensions)
        self.assertEqual(33, cell.to_higher_density(quadrant))

    def test_middle_cell_on_384_plate_corresponds_767_cell_on_1536_plate_in_case_second_quadrant(self):
        dimensions = Dimensions(16, 24)
        quadrant = Quadrant(0, 1)
        cell = PlateCell(192, dimensions)
        self.assertEqual(767, cell.to_higher_density(quadrant))

    def test_last_cell_on_384_plate_corresponds_1535_cell_on_1536_plate_in_case_second_quadrant(self):
        dimensions = Dimensions(16, 24)
        quadrant = Quadrant(0, 1)
        cell = PlateCell(384, dimensions)
        self.assertEqual(1535, cell.to_higher_density(quadrant))

    def test_first_cell_on_384_plate_corresponds_2_cell_on_1536_plate_in_case_third_quadrant(self):
        dimensions = Dimensions(16, 24)
        quadrant = Quadrant(1, 0)
        cell = PlateCell(1, dimensions)
        self.assertEqual(2, cell.to_higher_density(quadrant))

    def test_middle_cell_on_384_plate_corresponds_736_cell_on_1536_plate_in_case_third_quadrant(self):
        dimensions = Dimensions(16, 24)
        quadrant = Quadrant(1, 0)
        cell = PlateCell(192, dimensions)
        self.assertEqual(736, cell.to_higher_density(quadrant))

    def test_last_cell_on_384_plate_corresponds_1504_cell_on_1536_plate_in_case_third_quadrant(self):
        dimensions = Dimensions(16, 24)
        quadrant = Quadrant(1, 0)
        cell = PlateCell(384, dimensions)
        self.assertEqual(1504, cell.to_higher_density(quadrant))

    def test_first_cell_on_384_plate_corresponds_first_cell_on_1536_plate_in_case_fourth_quadrant(self):
        dimensions = Dimensions(16, 24)
        quadrant = Quadrant(1, 1)
        cell = PlateCell(1, dimensions)
        self.assertEqual(34, cell.to_higher_density(quadrant))

    def test_middle_cell_on_384_plate_corresponds_768_cell_on_1536_plate_in_case_fourth_quadrant(self):
        dimensions = Dimensions(16, 24)
        quadrant = Quadrant(1, 1)
        cell = PlateCell(192, dimensions)
        self.assertEqual(768, cell.to_higher_density(quadrant))

    def test_last_cell_on_384_plate_corresponds_last_cell_on_1536_plate_in_case_fourth_quadrant(self):
        dimensions = Dimensions(16, 24)
        quadrant = Quadrant(1, 1)
        cell = PlateCell(384, dimensions)
        self.assertEqual(1536, cell.to_higher_density(quadrant))

    def test_1_cell_number_is_returned_for_A1_coordinate_on_96_plate(self):
        self.assertEqual(1, PlateCell.parse_string("A01", Dimensions(8, 12)))

    def test_96_cell_number_is_returned_for_H12_coordinate_on_96_plate(self):
        self.assertEqual(96, PlateCell.parse_string("H12", Dimensions(8, 12)))

if __name__ == "__main__":
    unittest.main()