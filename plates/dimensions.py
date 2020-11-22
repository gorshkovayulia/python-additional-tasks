available_dimensions = ((4, 6), (8, 12), (16, 24))

class Dimensions:

    def __init__(self, number_of_rows, number_of_columns):
        """Initiate attributes for a plate"""
        dimension = (number_of_rows, number_of_columns)
        if dimension not in available_dimensions:
            raise ValueError(str(dimension) + " tuple is not acceptable!" + " Available tuples are " + str(available_dimensions))
        else:
            self.number_of_rows = number_of_rows
            self.number_of_columns = number_of_columns

    def get_capacity(self):
        """Сalculate size of the plate"""
        return self.number_of_rows * self.number_of_columns

    def get_tuple(self):
        """Return a tuple"""
        dimension = (self.number_of_rows, self.number_of_columns)
        return dimension


