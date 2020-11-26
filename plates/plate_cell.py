from dimensions import Dimensions
from quadrants import Quadrants


class PlateCell:
    
    LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                        'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'AA', 'AB', 'AC', 'AD', 'AE', 'AF']

    def __init__(self, cell_number, dimensions):
        self.dimensions = dimensions
        if not cell_number:
            raise TypeError("Cell number cannot be None!")
        elif type(cell_number) is not int:
            raise TypeError("Cell number should be int!")
        elif cell_number < 0:
            raise ValueError("Cell number cannot be less than zero!")
        elif cell_number > self.dimensions.get_capacity():
            raise ValueError(str(cell_number) + " cell number is too big for " + str(self.dimensions.get_tuple()) + " dimension!")
        else:
            self.cell_number = cell_number

    def calculate_row_and_column(self):
        """
        Calculate row and column based on cell number.
        The numbering goes from top to bottom (not left to right).
        """
        row = (self.cell_number - 1) % self.dimensions.number_of_rows
        column = (self.cell_number - 1) // self.dimensions.number_of_rows
        return row, column

    def as_string(self):
        """Return human readable coordinate (e.g. A01, C12, AA01 etc)."""
        (row, column) = self.calculate_row_and_column()
        if column < 9:
            return self.LETTERS[row] + str(0) + str(column + 1)
        else:
            return self.LETTERS[row] + str(column + 1)

    def to_higher_density(self, quadrants):
        """
        Needed for plate stamping - to know where this cell will end up after the transfer to a bigger plate.
        Return: a new PlateCell, the one that corresponds to a higher density (e.g. 96 if current was 24, 384 if current was 96, etc).
        """
        (row, column) = self.calculate_row_and_column()
        new_row = row * 2
        new_column = column * 2
        if self.dimensions.number_of_rows == 4:
            new_index = ((new_column + quadrants.start_column) * 8) + new_row + quadrants.start_row
            return new_index + 1
        elif self.dimensions.number_of_rows == 8:
            new_index = ((new_column + quadrants.start_column) * 16) + new_row + quadrants.start_row
            return new_index + 1
        elif self.dimensions.number_of_rows == 16:
            new_index = ((new_column + quadrants.start_column) * 32) + new_row + quadrants.start_row
            return new_index + 1