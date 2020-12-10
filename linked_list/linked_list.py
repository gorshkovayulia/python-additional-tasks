from node import Node


class LinkedList:
    def __init__(self):
        self.first_node = None
        self.last_node = None
        self.length_of_list = 0

    def append(self, new_value):
        """Add a new element at the end of the list."""
        if new_value is None:
            raise TypeError("Value is absent!")
        else:
            self.length_of_list += 1
            if self.first_node is None:
                self.first_node = Node(new_value)
                self.last_node = self.first_node
            else:
                self.last_node.next_node = Node(new_value)

    def get_size(self):
        """Return size of the list."""
        self.length_of_list = 0
        if self.first_node is not None:
            self.length_of_list += 1
            current_node = self.first_node
            while current_node.next_node is not None:
                current_node = current_node.next_node
                self.length_of_list += 1
            return self.length_of_list
        else:
            return self.length_of_list

    def get_value(self, value_index):
        """Go through the list and compare index of node with index of value."""
        if value_index is None:
            raise TypeError("Value index is absent!")
        elif type(value_index) is not int:
            raise TypeError("Value index must be int!")
        elif value_index < 0:
            raise ValueError("Value index cannot be less than 0!")
        elif self.first_node is None:
            raise ValueError("List is empty!")
        current_node = self.first_node
        node_index = 0   # define a variable that corresponds index of node
        while node_index <= value_index:
            if node_index == value_index:
                return current_node.value
            else:
                node_index += 1
                current_node = self.first_node.next_node
        return value_index


