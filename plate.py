class Dimensions:

    def __init__(self, number_of_rows, number_of_columns):
        """Initiate attributes for a plate"""
        self.number_of_rows = number_of_rows
        self.number_of_columns = number_of_columns

    def get_capacity(self):
        """Calculate the size of the plate"""
        plate_size = self.number_of_rows * self.number_of_columns
        return plate_size


class PlateCell:

    def __init__(self, cell_number, dimensions):
        self.cell_number = cell_number
        self.dimensions = dimensions
        if not self.cell_number:
            raise TypeError("Cell number cannot be None!")
        if type(self.cell_number) is not int:
            raise TypeError("Cell number should be int!")
        if self.cell_number < 0:
            raise ValueError("Сell number cannot be negative!")
        if self.cell_number == 0:
            raise ValueError("Сell number cannot equal zero!")
        if self.cell_number > self.dimensions.get_capacity():
            raise ValueError(str(self.cell_number) + " cell number is too big for " + "(" + str(
                self.dimensions.number_of_rows) + ", " + str(self.dimensions.number_of_columns) + ")" + " dimension!")

    def calculate_row_and_column(self):
        """
        Calculate row and column based on cell number.
        The numbering goes from top to bottom (not left to right).
        """
        row = (self.cell_number - 1) % self.dimensions.number_of_rows
        column = (self.cell_number - 1) // self.dimensions.number_of_rows
        return row + 1, column + 1

    def as_string(self):
        """Return human readable coordinate"""
        (row, column) = self.calculate_row_and_column()
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
        return letters[row - 1] + str(column)

    def to_higher_density(self):
        """
        Needed for plate stamping - to know where this cell will end up after the transfer to a bigger plate.
        :return: a new PlateCell, the one that corresponds to a higher density
                 (e.g. 96 if current was 24, 384 if current was 96, etc)
        """
        (row, column) = self.calculate_row_and_column()
        new_row = (row - 1) * 2
        new_column = (column - 1) * 2
        return(new_row + 1, new_column + 1)

dimensions = Dimensions(16, 24)
cell = PlateCell(2, dimensions)
# test = cell.as_string()
# print(cell.cell_number)
# print(test)
test_2 = cell.to_higher_density()
# row_and_column = cell.calculate_row_and_column()
print(test_2)
# cell.to_higher_density()        # returns 1536 plate cell (because 1536 is the next density), in this case: D01
