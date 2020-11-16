class Dimensions():

    def __init__(self, number_of_rows, number_of_columns):
        """Initiate attributes for a plate"""
        self.number_of_rows = number_of_rows
        self.number_of_columns = number_of_columns

class PlateCell():

    def __init__(self, cell_number, dimensions):
        self.cell_number = int(cell_number)
        self.dimensions = dimensions

    def calculate_row_and_column(self):
        """Calculate row and column based on cell number"""
        if self.cell_number > self.dimensions.number_of_rows * self.dimensions.number_of_columns:
            raise AttributeError("Cell number is too big for current dimension!")
        elif self.cell_number < 0:
            raise AttributeError("Cell number cannot be negative!")
        else:
            self.row = (self.cell_number % self.dimensions.number_of_rows)
            self.column = (self.cell_number // self.dimensions.number_of_rows) % self.dimensions.number_of_columns
            return [self.row, self.column]

    def as_string(self):
        """Return human readable coordinate"""
        self.calculated_row_and_column = self.calculate_row_and_column()
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
        letter = letters[self.calculated_row_and_column[0]]
        coordinate = letter + str(self.calculated_row_and_column[1] + 1)
        return coordinate
        # Old version -->
        # for index, value in enumerate(letters):
        #     if index == self.calculated_row_and_column[0]:
        #         return str(value + str(self.calculated_row_and_column[1] + 1))

    def to_higher_density(self):
        """
        Needed for plate stamping - to know where this cell will end up after the transfer to a bigger plate.
        :return: a new PlateCell, the one that corresponds to a higher density
                 (e.g. 96 if current was 24, 384 if current was 96, etc)
        """
        self.calculated_row_and_column = self.calculate_row_and_column()
        self.new_row = self.calculated_row_and_column[0] + 2
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'AA', 'AB', 'AC', 'AD', 'AE', 'AF']
        letter = letters[self.new_row]
        coordinate = letter + str(self.calculated_row_and_column[1] + 1)
        return coordinate
        # Old version -->
        # for index, value in enumerate(letters):
        #     if index == self.new_row:
        #         return str(value + str(self.calculated_row_and_column[1] + 1))

# dimensions = Dimensions(16, 24)
# cell = PlateCell(385, dimensions)
# test = cell.as_string()
# print(test)
# test_2 = cell.to_higher_density()
# row_and_column = cell.calculate_row_and_column()
# print(row_and_column)
# cell.to_higher_density()        # returns 1536 plate cell (because 1536 is the next density), in this case: D01


