class Dimensions:

    def __init__(self, number_of_rows, number_of_columns):
        """Initiate attributes for a plate"""
        if number_of_rows is None or number_of_columns is None:
            raise TypeError("Number of rows or number of columns are absent!")
        elif number_of_rows <= 0 or number_of_columns <= 0:
            raise ValueError("Number of rows and number of columns cannot be less or equal 0!")
        elif type(number_of_rows) is not int or type(number_of_columns) is not int:
            raise TypeError("Number of rows and number of columns should be int!")
        else:
            self.number_of_rows = number_of_rows
            self.number_of_columns = number_of_columns

    def get_capacity(self):
        """Сalculate size of the plate"""
        return self.number_of_rows * self.number_of_columns

    def get_tuple_with_dimensions(self):
        """Return a tuple"""
        dimension = (self.number_of_rows, self.number_of_columns)
        return dimension


