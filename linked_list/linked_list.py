from element import Element


class LinkedList:
    def __init__(self):
        self.first_element = None
        self.last_element = None
        self.length_of_list = 0

    def append(self, new_value):
        """Add a new element at the end of the list."""
        if new_value is None:
            raise TypeError("Value is absent!")
        self.length_of_list += 1
        if self.first_element is None:
            self.first_element = Element(new_value)
            self.last_element = self.first_element
        else:
            self.last_element.next_element = Element(new_value)

    def get_size(self):
        """Return size of the list."""
        return self.length_of_list

    def get_value(self, index):
        """Go through the list and compare index of element with index of value."""
        if self.length_of_list == 0:
            raise ValueError("List is empty!")
        elif index is None:
            raise TypeError("Index is absent!")
        elif type(index) is not int:
            raise TypeError("Index must be int!")
        elif index < 0:
            raise ValueError("Index cannot be less than 0!")
        elif index + 1 > self.length_of_list:
            raise ValueError("Index is too big for current list!")
        current_element = self.first_element
        index_of_element = 0
        while index_of_element <= index:
            if index_of_element == index:
                return current_element.value
            else:
                index_of_element += 1
                current_element = self.first_element.next_node

    def remove(self, index):
        if self.length_of_list == 0:
            raise ValueError("The list does not have any elements!")
        elif index is None:
            raise TypeError("Index is absent!")
        elif type(index) is not int:
            raise TypeError("Index must be int!")
        elif index < 0:
            raise ValueError("Index cannot be less than 0!")
        elif index + 1 > self.length_of_list:
            raise ValueError("Index is too big for current list!")
        previous_element = None
        current_element = self.first_element
        # index_of_element = 0
        while current_element.value is not None:
            previous_element = current_element
            current_element = current_element.next_element
        if previous_element is None:
            self.first_element = current_element.next_element
