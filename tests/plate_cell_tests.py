import unittest
from plate_cell import PlateCell
from dimensions import Dimensions
from quadrants import Quadrants

class TestPlateCell(unittest.TestCase):
    """Tests for PlateCell class"""

    def test_first_row_and_first_column_are_returned_for_the_first_cell_in_384_plate_in_case_first_quadrant(self):
        dimensions = Dimensions(16, 24)
        quadrants = Quadrants(0, 0)
        cell = PlateCell(1, dimensions, quadrants)
        self.assertEqual((0, 0), cell.calculate_row_and_column())

    def test_sixteenth_row_and_twelfth_column_are_returned_for_the_middle_cell_in_384_plate_in_case_first_quadrant(self):
        dimensions = Dimensions(16, 24)
        quadrants = Quadrants(0, 0)
        cell = PlateCell(192, dimensions, quadrants)
        self.assertEqual((15, 11), cell.calculate_row_and_column())

    def test_sixteenth_row_and_twenty_fourth_column_are_returned_for_the_last_cell_in_384_plate_in_case_first_quadrant(self):
        dimensions = Dimensions(16, 24)
        quadrants = Quadrants(0, 0)
        cell = PlateCell(384, dimensions, quadrants)
        self.assertEqual((15, 23), cell.calculate_row_and_column())

    def test_first_row_and_first_column_are_returned_for_the_first_cell_in_96_plate(self):
        dimensions = Dimensions(8, 12)
        quadrants = Quadrants(0, 0)
        cell = PlateCell(1, dimensions, quadrants)
        self.assertEqual((0, 0), cell.calculate_row_and_column())

    def test_eighth_row_and_sixth_column_are_returned_for_the_middle_cell_in_96_plate(self):
        dimensions = Dimensions(8, 12)
        quadrants = Quadrants(0, 0)
        cell = PlateCell(48, dimensions, quadrants)
        self.assertEqual((7, 5), cell.calculate_row_and_column())

    def test_eighth_row_and_twelfth_column_are_returned_for_the_last_cell_in_96_plate(self):
        dimensions = Dimensions(8, 12)
        quadrants = Quadrants(0, 0)
        cell = PlateCell(96, dimensions, quadrants)
        self.assertEqual((7, 11), cell.calculate_row_and_column())

    def test_first_row_and_first_column_are_returned_for_the_first_cell_in_24_plate(self):
        dimensions = Dimensions(4, 6)
        quadrants = Quadrants(0, 0)
        cell = PlateCell(1, dimensions, quadrants)
        self.assertEqual((0, 0), cell.calculate_row_and_column())

    def test_fourth_row_and_third_column_are_returned_for_the_middle_cell_in_24_plate(self):
        dimensions = Dimensions(4, 6)
        quadrants = Quadrants(0, 0)
        cell = PlateCell(12, dimensions, quadrants)
        self.assertEqual((3, 2), cell.calculate_row_and_column())

    def test_fourth_row_and_sixth_column_are_returned_for_the_last_cell_in_24_plate(self):
        dimensions = Dimensions(4, 6)
        quadrants = Quadrants(0, 0)
        cell = PlateCell(24, dimensions, quadrants)
        self.assertEqual((3, 5), cell.calculate_row_and_column())

    def test_not_existing_cell_number_in_case_384_plate_raises_value_error(self):
        dimensions = Dimensions(16, 24)
        quadrants = Quadrants(0, 0)
        try:
            cell = PlateCell(385, dimensions, quadrants)
            cell.cell_number()
            self.fail("Should be an exception")
        except ValueError as e:
            str(e)
            self.assertEqual("385 cell number is too big for (16, 24) dimension!", str(e))

    def test_not_existing_cell_number_in_case_96_plate_raises_value_error(self):
        dimensions = Dimensions(8, 12)
        quadrants = Quadrants(0, 0)
        try:
            cell = PlateCell(97, dimensions, quadrants)
            cell.cell_number()
            self.fail("Should be an exception")
        except ValueError as e:
            str(e)
            self.assertEqual("97 cell number is too big for (8, 12) dimension!", str(e))

    def test_not_existing_cell_number_in_case_24_plate_raises_value_error(self):
        dimensions = Dimensions(4, 6)
        quadrants = Quadrants(0, 0)
        try:
            cell = PlateCell(25, dimensions, quadrants)
            cell.cell_number()
            self.fail("Should be an exception")
        except ValueError as e:
            str(e)
            self.assertEqual("25 cell number is too big for (4, 6) dimension!", str(e))

    def test_zero_cell_number_raises_value_error(self):
        dimensions = Dimensions(16, 24)
        quadrants = Quadrants(0, 0)
        try:
            cell = PlateCell(0, dimensions, quadrants)
            cell.cell_number()
            self.fail("Should be an exception")
        except TypeError as e:
            str(e)
            self.assertEqual("Cell number cannot be None!", str(e))

    def test_type_error_appears_in_case_none_value_as_cell_number(self):
        dimensions = Dimensions(16, 24)
        quadrants = Quadrants(0, 0)
        try:
            cell = PlateCell(None, dimensions, quadrants)
            cell.cell_number()
            self.fail("Should be an exception")
        except TypeError as e:
            str(e)
            self.assertEqual("Cell number cannot be None!", str(e))

    def test_negative_cell_number_raises_value_error(self):
        dimensions = Dimensions(16, 24)
        quadrants = Quadrants(0, 0)
        try:
            cell = PlateCell(-5, dimensions, quadrants)
            cell.cell_number()
            self.fail("Should be an exception")
        except ValueError as e:
            str(e)
            self.assertEqual("Cell number cannot be less than zero!", str(e))

    def test_decimal_cell_number_raises_value_error(self):
        dimensions = Dimensions(16, 24)
        quadrants = Quadrants(0, 0)
        try:
            cell = PlateCell(1.65, dimensions, quadrants)
            cell.cell_number()
            self.fail("Should be an exception")
        except TypeError as e:
            str(e)
            self.assertEqual("Cell number should be int!", str(e))

    def test_value_error_appears_in_case_cell_number_is_text(self):
        dimensions = Dimensions(16, 24)
        quadrants = Quadrants(0, 0)
        try:
            cell = PlateCell('test', dimensions, quadrants)
            cell.cell_number()
            self.fail("Should be an exception")
        except TypeError as e:
            str(e)
            self.assertEqual("Cell number should be int!", str(e))

    def test_A01_coordinate_is_returned_for_the_first_cell_on_384_plate(self):
        dimensions = Dimensions(16, 24)
        quadrants = Quadrants(0, 0)
        cell = PlateCell(1, dimensions, quadrants)
        self.assertEqual('A01', cell.as_string())

    def test_P09_coordinate_is_returned_for_the_middle_cell_on_384_plate(self):
        dimensions = Dimensions(16, 24)
        quadrants = Quadrants(0, 0)
        cell = PlateCell(144, dimensions, quadrants)
        self.assertEqual('P09', cell.as_string())

    def test_P24_coordinate_is_returned_for_the_last_cell_on_384_plate(self):
        dimensions = Dimensions(16, 24)
        quadrants = Quadrants(0, 0)
        cell = PlateCell(384, dimensions, quadrants)
        self.assertEqual('P24', cell.as_string())

    def test_A01_coordinate_is_returned_for_the_first_cell_on_96_plate(self):
        dimensions = Dimensions(8, 12)
        quadrants = Quadrants(0, 0)
        cell = PlateCell(1, dimensions, quadrants)
        self.assertEqual('A01', cell.as_string())

    def test_H06_coordinate_is_returned_for_the_middle_cell_on_96_plate(self):
        dimensions = Dimensions(8, 12)
        quadrants = Quadrants(0, 0)
        cell = PlateCell(48, dimensions, quadrants)
        self.assertEqual('H06', cell.as_string())

    def test_H12_coordinate_is_returned_for_the_last_cell_on_96_plate(self):
        dimensions = Dimensions(8, 12)
        quadrants = Quadrants(0, 0)
        cell = PlateCell(96, dimensions, quadrants)
        self.assertEqual('H12', cell.as_string())

    def test_A01_coordinate_is_returned_for_the_first_cell_on_24_plate(self):
        dimensions = Dimensions(4, 6)
        quadrants = Quadrants(0, 0)
        cell = PlateCell(1, dimensions, quadrants)
        self.assertEqual('A01', cell.as_string())

    def test_D03_coordinate_is_returned_for_the_middle_cell_on_24_plate(self):
        dimensions = Dimensions(4, 6)
        quadrants = Quadrants(0, 0)
        cell = PlateCell(12, dimensions, quadrants)
        self.assertEqual('D03', cell.as_string())

    def test_D06_coordinate_is_returned_for_the_last_cell_on_24_plate(self):
        dimensions = Dimensions(4, 6)
        quadrants = Quadrants(0, 0)
        cell = PlateCell(24, dimensions, quadrants)
        self.assertEqual('D06', cell.as_string())

    def test_first_cell_on_384_plate_corresponds_first_cell_on_1536_plate_in_case_first_quadrant(self):
        dimensions = Dimensions(16, 24)
        quadrants = Quadrants(0, 0)
        cell = PlateCell(1, dimensions, quadrants)
        self.assertEqual(1, cell.to_higher_density())

    def test_middle_cell_on_384_plate_corresponds_735_cell_on_1536_plate_in_case_first_quadrant(self):
        dimensions = Dimensions(16, 24)
        quadrants = Quadrants(0, 0)
        cell = PlateCell(192, dimensions, quadrants)
        self.assertEqual(735, cell.to_higher_density())

    def test_last_cell_on_384_plate_corresponds_1503_cell_on_1536_plate_in_case_first_quadrant(self):
        dimensions = Dimensions(16, 24)
        quadrants = Quadrants(0, 0)
        cell = PlateCell(384, dimensions, quadrants)
        self.assertEqual(1503, cell.to_higher_density())

    def test_first_cell_on_384_plate_corresponds_33_cell_on_1536_plate_in_case_second_quadrant(self):
        dimensions = Dimensions(16, 24)
        quadrants = Quadrants(0, 1)
        cell = PlateCell(1, dimensions, quadrants)
        self.assertEqual(33, cell.to_higher_density())

    def test_middle_cell_on_384_plate_corresponds_767_cell_on_1536_plate_in_case_second_quadrant(self):
        dimensions = Dimensions(16, 24)
        quadrants = Quadrants(0, 1)
        cell = PlateCell(192, dimensions, quadrants)
        self.assertEqual(767, cell.to_higher_density())

    def test_last_cell_on_384_plate_corresponds_1535_cell_on_1536_plate_in_case_second_quadrant(self):
        dimensions = Dimensions(16, 24)
        quadrants = Quadrants(0, 1)
        cell = PlateCell(384, dimensions, quadrants)
        self.assertEqual(1535, cell.to_higher_density())

    def test_first_cell_on_384_plate_corresponds_2_cell_on_1536_plate_in_case_third_quadrant(self):
        dimensions = Dimensions(16, 24)
        quadrants = Quadrants(1, 0)
        cell = PlateCell(1, dimensions, quadrants)
        self.assertEqual(2, cell.to_higher_density())

    def test_middle_cell_on_384_plate_corresponds_736_cell_on_1536_plate_in_case_third_quadrant(self):
        dimensions = Dimensions(16, 24)
        quadrants = Quadrants(1, 0)
        cell = PlateCell(192, dimensions, quadrants)
        self.assertEqual(736, cell.to_higher_density())

    def test_last_cell_on_384_plate_corresponds_1504_cell_on_1536_plate_in_case_third_quadrant(self):
        dimensions = Dimensions(16, 24)
        quadrants = Quadrants(1, 0)
        cell = PlateCell(384, dimensions, quadrants)
        self.assertEqual(1504, cell.to_higher_density())

    def test_first_cell_on_384_plate_corresponds_first_cell_on_1536_plate_in_case_fourth_quadrant(self):
        dimensions = Dimensions(16, 24)
        quadrants = Quadrants(1, 1)
        cell = PlateCell(1, dimensions, quadrants)
        self.assertEqual(34, cell.to_higher_density())

    def test_middle_cell_on_384_plate_corresponds_768_cell_on_1536_plate_in_case_fourth_quadrant(self):
        dimensions = Dimensions(16, 24)
        quadrants = Quadrants(1, 1)
        cell = PlateCell(192, dimensions, quadrants)
        self.assertEqual(768, cell.to_higher_density())

    def test_last_cell_on_384_plate_corresponds_last_cell_on_1536_plate_in_case_fourth_quadrant(self):
        dimensions = Dimensions(16, 24)
        quadrants = Quadrants(1, 1)
        cell = PlateCell(384, dimensions, quadrants)
        self.assertEqual(1536, cell.to_higher_density())

    def test_first_cell_on_96_plate_corresponds_first_cell_on_384_plate_in_case_first_quadrant(self):
        dimensions = Dimensions(8, 12)
        quadrants = Quadrants(0, 0)
        cell = PlateCell(1, dimensions, quadrants)
        self.assertEqual(1, cell.to_higher_density())

    def test_middle_cell_on_96_plate_corresponds_175_cell_on_384_plate_in_case_first_quadrant(self):
        dimensions = Dimensions(8, 12)
        quadrants = Quadrants(0, 0)
        cell = PlateCell(48, dimensions, quadrants)
        self.assertEqual(175, cell.to_higher_density())

    def test_last_cell_on_96_plate_corresponds_367_cell_on_384_plate_in_case_first_quadrant(self):
        dimensions = Dimensions(8, 12)
        quadrants = Quadrants(0, 0)
        cell = PlateCell(96, dimensions, quadrants)
        self.assertEqual(367, cell.to_higher_density())

    def test_first_cell_on_96_plate_corresponds_17_cell_on_384_plate_in_case_second_quadrant(self):
        dimensions = Dimensions(8, 12)
        quadrants = Quadrants(0, 1)
        cell = PlateCell(1, dimensions, quadrants)
        self.assertEqual(17, cell.to_higher_density())

    def test_middle_cell_on_96_plate_corresponds_191_cell_on_384_plate_in_case_second_quadrant(self):
        dimensions = Dimensions(8, 12)
        quadrants = Quadrants(0, 1)
        cell = PlateCell(48, dimensions, quadrants)
        self.assertEqual(191, cell.to_higher_density())

    def test_last_cell_on_96_plate_corresponds_95_cell_on_383_plate_in_case_second_quadrant(self):
        dimensions = Dimensions(8, 12)
        quadrants = Quadrants(0, 1)
        cell = PlateCell(96, dimensions, quadrants)
        self.assertEqual(383, cell.to_higher_density())

    def test_first_cell_on_96_plate_corresponds_2_cell_on_384_plate_in_case_third_quadrant(self):
        dimensions = Dimensions(8, 12)
        quadrants = Quadrants(1, 0)
        cell = PlateCell(1, dimensions, quadrants)
        self.assertEqual(2, cell.to_higher_density())

    def test_middle_cell_on_96_plate_corresponds_40_cell_on_384_plate_in_case_third_quadrant(self):
        dimensions = Dimensions(8, 12)
        quadrants = Quadrants(1, 0)
        cell = PlateCell(48, dimensions, quadrants)
        self.assertEqual(176, cell.to_higher_density())

    def test_last_cell_on_96_plate_corresponds_88_cell_on_384_plate_in_case_third_quadrant(self):
        dimensions = Dimensions(8, 12)
        quadrants = Quadrants(1, 0)
        cell = PlateCell(96, dimensions, quadrants)
        self.assertEqual(368, cell.to_higher_density())

    def test_first_cell_on_96_plate_corresponds_18_cell_on_384_plate_in_case_fourth_quadrant(self):
        dimensions = Dimensions(8, 12)
        quadrants = Quadrants(1, 1)
        cell = PlateCell(1, dimensions, quadrants)
        self.assertEqual(18, cell.to_higher_density())

    def test_middle_cell_on_96_plate_corresponds_48_cell_on_384_plate_in_case_fourth_quadrant(self):
        dimensions = Dimensions(8, 12)
        quadrants = Quadrants(1, 1)
        cell = PlateCell(48, dimensions, quadrants)
        self.assertEqual(192, cell.to_higher_density())

    def test_last_cell_on_96_plate_corresponds_384_cell_on_384_plate_in_case_fourth_quadrant(self):
        dimensions = Dimensions(8, 12)
        quadrants = Quadrants(1, 1)
        cell = PlateCell(96, dimensions, quadrants)
        self.assertEqual(384, cell.to_higher_density())

    def test_first_cell_on_24_plate_corresponds_first_cell_on_96_plate_in_case_first_quadrant(self):
        dimensions = Dimensions(4, 6)
        quadrants = Quadrants(0, 0)
        cell = PlateCell(1, dimensions, quadrants)
        self.assertEqual(1, cell.to_higher_density())

    def test_middle_cell_on_24_plate_corresponds_39_cell_on_96_plate_in_case_first_quadrant(self):
        dimensions = Dimensions(4, 6)
        quadrants = Quadrants(0, 0)
        cell = PlateCell(12, dimensions, quadrants)
        self.assertEqual(39, cell.to_higher_density())

    def test_last_cell_on_24_plate_corresponds_87_cell_on_96_plate_in_case_first_quadrant(self):
        dimensions = Dimensions(4, 6)
        quadrants = Quadrants(0, 0)
        cell = PlateCell(24, dimensions, quadrants)
        self.assertEqual(87, cell.to_higher_density())

    def test_first_cell_on_24_plate_corresponds_9_cell_on_96_plate_in_case_second_quadrant(self):
        dimensions = Dimensions(4, 6)
        quadrants = Quadrants(0, 1)
        cell = PlateCell(1, dimensions, quadrants)
        self.assertEqual(9, cell.to_higher_density())

    def test_middle_cell_on_24_plate_corresponds_47_cell_on_96_plate_in_case_second_quadrant(self):
        dimensions = Dimensions(4, 6)
        quadrants = Quadrants(0, 1)
        cell = PlateCell(12, dimensions, quadrants)
        self.assertEqual(47, cell.to_higher_density())

    def test_last_cell_on_24_plate_corresponds_95_cell_on_96_plate_in_case_second_quadrant(self):
        dimensions = Dimensions(4, 6)
        quadrants = Quadrants(0, 1)
        cell = PlateCell(24, dimensions, quadrants)
        self.assertEqual(95, cell.to_higher_density())

    def test_first_cell_on_24_plate_corresponds_2_cell_on_96_plate_in_case_third_quadrant(self):
        dimensions = Dimensions(4, 6)
        quadrants = Quadrants(1, 0)
        cell = PlateCell(1, dimensions, quadrants)
        self.assertEqual(2, cell.to_higher_density())

    def test_middle_cell_on_24_plate_corresponds_40_cell_on_96_plate_in_case_third_quadrant(self):
        dimensions = Dimensions(4, 6)
        quadrants = Quadrants(1, 0)
        cell = PlateCell(12, dimensions, quadrants)
        self.assertEqual(40, cell.to_higher_density())

    def test_last_cell_on_24_plate_corresponds_88_cell_on_96_plate_in_case_third_quadrant(self):
        dimensions = Dimensions(4, 6)
        quadrants = Quadrants(1, 0)
        cell = PlateCell(24, dimensions, quadrants)
        self.assertEqual(88, cell.to_higher_density())

    def test_first_cell_on_24_plate_corresponds_10_cell_on_96_plate_in_case_fourth_quadrant(self):
        dimensions = Dimensions(4, 6)
        quadrants = Quadrants(1, 1)
        cell = PlateCell(1, dimensions, quadrants)
        self.assertEqual(10, cell.to_higher_density())

    def test_middle_cell_on_24_plate_corresponds_39_cell_on_96_plate_in_case_fourth_quadrant(self):
        dimensions = Dimensions(4, 6)
        quadrants = Quadrants(1, 1)
        cell = PlateCell(12, dimensions, quadrants)
        self.assertEqual(48, cell.to_higher_density())

    def test_last_cell_on_24_plate_corresponds_96_cell_on_96_plate_in_case_fourth_quadrant(self):
        dimensions = Dimensions(4, 6)
        quadrants = Quadrants(1, 1)
        cell = PlateCell(24, dimensions, quadrants)
        self.assertEqual(96, cell.to_higher_density())

if __name__ == "__main__":
    unittest.main()