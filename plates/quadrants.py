class Quadrants:

    def __init__(self, start_row, start_column):
        if start_row is None or start_column is None:
            raise TypeError("Start row or start column are absent!")
        elif start_row < 0 or start_column < 0:
            raise ValueError("Start row and start column cannot be less than 0!")
        elif start_row > 1 or start_column > 1:
            raise ValueError("Start row and start column cannot be more than 1!")
        elif type(start_row) is not int or type(start_column) is not int:
            raise TypeError("Start row and start column should be int!")
        else:
            self.start_row = start_row
            self.start_column = start_column