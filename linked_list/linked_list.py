from linked_list.node import Node


class LinkedList:
    def __init__(self):
        self.first_node = None
        self.last_node = None
        self.size = 0

    def append(self, new_value):
        """Add a new element at the end of the list."""
        self.size += 1
        new_node = Node(new_value)
        if self.first_node is None:
            self.first_node = new_node
        else:
            self.last_node.next_node = new_node
            new_node.previous_node = self.last_node
        self.last_node = new_node

    def get_size(self):
        """Return size of the list."""
        return self.size

    def get_value(self, index):
        """Go through the list and compare current index with searching index."""
        self._assert_index(index)
        middle_value = self.size // 2
        if index + 1 <= middle_value:
            current_node = self.first_node
            current_index = 0
            while current_index != index:
                current_index += 1
                current_node = current_node.next_node
        else:
            current_node = self.last_node
            current_index = self.size - 1
            while current_index != index:
                current_index -= 1
                current_node = current_node.previous_node
        return current_node.value

    def remove(self, index):
        self._assert_index(index)
        middle_value = self.size // 2
        if index + 1 <= middle_value:
            if index == 0:
                self.first_node = self.first_node.next_node
            if index == self.size - 1:
                self.last_node = self.last_node.previous_node
            else:
                current_node = self.first_node
                current_index = 0
                while current_index != index - 1:
                    current_index += 1
                    current_node = current_node.next_node
                current_node.next_node = current_node.next_node.next_node
        else:
            if index == self.size - 1:
                self.last_node = self.last_node.previous_node
            if index == middle_value:
                self.first_node = self.first_node.next_node
                self.last_node = self.first_node
            else:
                current_node = self.last_node
                current_index = self.size - 1
                while current_index != index - 1:
                    current_index -= 1
                    current_node = current_node.previous_node
                current_node.next_node = current_node.next_node.next_node
        self.size -= 1

    def _assert_index(self, index):
        if self.size == 0:
            raise ValueError("List is empty!")
        elif index is None:
            raise TypeError("Index is absent!")
        elif type(index) is not int:
            raise TypeError("Index must be int!")
        elif index < 0:
            raise ValueError("Index cannot be less than 0!")
        elif index >= self.size:
            raise ValueError("Index is too big for current list!")


