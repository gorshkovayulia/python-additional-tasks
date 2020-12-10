import unittest
from linked_list.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):

    def test_attempt_to_add_none_value_raises_type_error(self):
        linkedlist = LinkedList()
        try:
            linkedlist.append(None)
            self.fail("Should be an exception")
        except TypeError as e:
            self.assertEqual("Value is absent!", str(e))

    def test_possible_to_add_negative_value(self):
        linkedlist = LinkedList()
        linkedlist.append(-2.89)
        self.assertEqual(1, linkedlist.length_of_list)

    def test_possible_to_add_zero_value(self):
        linkedlist = LinkedList()
        linkedlist.append(0)
        self.assertEqual(1, linkedlist.length_of_list)

    def test_possible_to_add_text_value(self):
        linkedlist = LinkedList()
        linkedlist.append('test')
        self.assertEqual(1, linkedlist.length_of_list)

    def test_possible_to_add_several_values(self):
        linkedlist = LinkedList()
        linkedlist.append('test')
        linkedlist.append('01test')
        self.assertEqual(2, linkedlist.length_of_list)

    def test_length_of_list_is_0_in_case_first_node_is_none(self):
        linkedlist = LinkedList()
        self.assertEqual(0, linkedlist.get_size())

    def test_length_of_list_is_1_in_case_only_first_node_is_present(self):
        linkedlist = LinkedList()
        linkedlist.append('test')
        self.assertEqual(1, linkedlist.get_size())

    def test_type_error_appears_if_searching_index_is_none(self):
        linkedlist = LinkedList()
        try:
            linkedlist.get_value(None)
            self.fail("Should be an exception")
        except TypeError as e:
            self.assertEqual("Value index is absent!", str(e))

    def test_type_error_appears_if_searching_index_is_string_type(self):
        linkedlist = LinkedList()
        try:
            linkedlist.get_value('test')
            self.fail("Should be an exception")
        except TypeError as e:
            self.assertEqual("Value index must be int!", str(e))

    def test_type_error_appears_if_searching_index_is_float_type(self):
        linkedlist = LinkedList()
        try:
            linkedlist.get_value(0.15)
            self.fail("Should be an exception")
        except TypeError as e:
            self.assertEqual("Value index must be int!", str(e))

    def test_value_error_appears_if_searching_index_is_negative(self):
        linkedlist = LinkedList()
        try:
            linkedlist.get_value(-1)
            self.fail("Should be an exception")
        except ValueError as e:
            self.assertEqual("Value index cannot be less than 0!", str(e))

    def test_looking_for_value_in_empty_list_raises_type_error(self):
        linkedlist = LinkedList()
        try:
            linkedlist.get_value(10)
            self.fail("Should be an exception")
        except ValueError as e:
            self.assertEqual("List is empty!", str(e))

    def test_10_value_is_returned_for_the_only_node(self):
        linkedlist = LinkedList()
        linkedlist.append(10)
        self.assertEqual(10, linkedlist.get_value(0))

    def test_10_value_is_returned_for_the_last_node(self):
        linkedlist = LinkedList()
        linkedlist.append('test')
        linkedlist.append(10)
        self.assertEqual(10, linkedlist.get_value(1))

    def test_10_value_is_returned_for_the_middle_node(self):
        linkedlist = LinkedList()
        linkedlist.append(1)
        linkedlist.append(10)
        linkedlist.append(100)
        self.assertEqual(10, linkedlist.get_value(1))

    def test_possible_to_remove_first_node(self):
        linkedlist = LinkedList()
        linkedlist.append(1)
        linkedlist.append(10)
        linkedlist.append(100)
        linkedlist.remove(0)
        self.assertEqual(2, linkedlist.get_size())

    def test_possible_to_remove_middle_node(self):
        linkedlist = LinkedList()
        linkedlist.append(1)
        linkedlist.append(10)
        linkedlist.append(100)
        linkedlist.remove(1)
        self.assertEqual(2, linkedlist.get_size())

    def test_possible_to_remove_last_node(self):
        linkedlist = LinkedList()
        linkedlist.append(1)
        linkedlist.append(10)
        linkedlist.append(100)
        linkedlist.remove(2)
        self.assertEqual(2, linkedlist.get_size())

    def test_possible_to_remove_the_only_node(self):
        linkedlist = LinkedList()
        linkedlist.append(1)
        linkedlist.remove(0)
        self.assertEqual(0, linkedlist.get_size())

    def test_attempt_to_remove_node_from_empty_list_raises_type_error(self):
        linkedlist = LinkedList()
        try:
            linkedlist.remove(1)
            self.fail("Should be an exception")
        except TypeError as e:
            self.assertEqual("The list does not have any elements!", str(e))

if __name__ == "__main__":
    unittest.main()