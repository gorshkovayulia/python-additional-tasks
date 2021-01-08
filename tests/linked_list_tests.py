import unittest
from linked_list.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):

    def test_possible_to_add_value_of_any_type(self):
        linkedlist = LinkedList()
        linkedlist.append(None)
        linkedlist.append(0)
        linkedlist.append('test')
        linkedlist.append(-2.89)
        self.assertEqual(4, linkedlist.get_size())

    def test_size_is_0_if_no_elements_have_been_added(self):
        linkedlist = LinkedList()
        self.assertEqual(0, linkedlist.get_size())

    def test_size_is_1_if_one_element_has_been_added(self):
        linkedlist = LinkedList()
        linkedlist.append('test')
        self.assertEqual(1, linkedlist.get_size())

    def test_value_error_appears_if_searching_index_is_0_and_list_is_empty(self):
        linkedlist = LinkedList()
        try:
            linkedlist.get_value(0)
            self.fail("Should be an exception")
        except ValueError as e:
            self.assertEqual("List is empty!", str(e))

    def test_type_error_appears_if_searching_index_is_none(self):
        linkedlist = LinkedList()
        linkedlist.append('test')
        try:
            linkedlist.get_value(None)
            self.fail("Should be an exception")
        except TypeError as e:
            self.assertEqual("Index is absent!", str(e))

    def test_type_error_appears_if_searching_index_is_string_type(self):
        linkedlist = LinkedList()
        linkedlist.append('test')
        try:
            linkedlist.get_value('test')
            self.fail("Should be an exception")
        except TypeError as e:
            self.assertEqual("Index must be int!", str(e))

    def test_type_error_appears_if_searching_index_is_float_type(self):
        linkedlist = LinkedList()
        linkedlist.append('test')
        try:
            linkedlist.get_value(0.15)
            self.fail("Should be an exception")
        except TypeError as e:
            self.assertEqual("Index must be int!", str(e))

    def test_value_error_appears_if_searching_index_is_negative(self):
        linkedlist = LinkedList()
        linkedlist.append('test')
        try:
            linkedlist.get_value(-1)
            self.fail("Should be an exception")
        except ValueError as e:
            self.assertEqual("Index cannot be less than 0!", str(e))

    def test_type_error_appears_when_searching_index_is_greater_than_upped_bound(self):
        linkedlist = LinkedList()
        linkedlist.append('test')
        try:
            linkedlist.get_value(10)
            self.fail("Should be an exception")
        except ValueError as e:
            self.assertEqual("Index is too big for current list!", str(e))

    def test_can_get_first_element(self):
        linkedlist = LinkedList()
        linkedlist.append(10)
        self.assertEqual(10, linkedlist.get_value(0))

    def test_can_get_last_element(self):
        linkedlist = LinkedList()
        linkedlist.append('test')
        linkedlist.append(10)
        self.assertEqual(10, linkedlist.get_value(1))

    def test_can_get_middle_element(self):
        linkedlist = LinkedList()
        linkedlist.append(1)
        linkedlist.append(10)
        linkedlist.append(100)
        linkedlist.append(None)
        self.assertEqual(10, linkedlist.get_value(1))

    def test_attempt_to_remove_element_from_empty_list_raises_value_error(self):
        linkedlist = LinkedList()
        try:
            linkedlist.remove(1)
            self.fail("Should be an exception")
        except ValueError as e:
            self.assertEqual("List is empty!", str(e))

    def test_attempt_to_remove_element_with_none_index_raises_type_error(self):
        linkedlist = LinkedList()
        linkedlist.append('test')
        linkedlist.append(1)
        try:
            linkedlist.remove(None)
            self.fail("Should be an exception")
        except TypeError as e:
            self.assertEqual("Index is absent!", str(e))

    def test_attempt_to_remove_element_with_float_type_index_raises_type_error(self):
        linkedlist = LinkedList()
        linkedlist.append('test')
        linkedlist.append(1)
        try:
            linkedlist.remove(0.15)
            self.fail("Should be an exception")
        except TypeError as e:
            self.assertEqual("Index must be int!", str(e))

    def test_attempt_to_remove_element_with_negative_index_raises_value_error(self):
        linkedlist = LinkedList()
        linkedlist.append('test')
        linkedlist.append(1)
        try:
            linkedlist.remove(-1)
            self.fail("Should be an exception")
        except ValueError as e:
            self.assertEqual("Index cannot be less than 0!", str(e))

    def test_attempt_to_remove_not_existing_element_raises_value_error(self):
        linkedlist = LinkedList()
        linkedlist.append('test')
        linkedlist.append(1)
        linkedlist.append('01test')
        try:
            linkedlist.remove(3)
            self.fail("Should be an exception")
        except ValueError as e:
            self.assertEqual("Index is too big for current list!", str(e))

    def test_can_remove_the_only_element(self):
        linkedlist = LinkedList()
        linkedlist.append(1)
        linkedlist.remove(0)
        self.assertEqual(0, linkedlist.get_size())

    def test_can_remove_the_last_element(self):
        linkedlist = LinkedList()
        linkedlist.append(1)
        linkedlist.append(2)
        linkedlist.remove(1)
        self.assertEqual(1, linkedlist.get_size())

    def test_can_remove_first_element(self):
        linkedlist = LinkedList()
        linkedlist.append(1)
        linkedlist.append(10)
        linkedlist.append(100)
        linkedlist.remove(0)
        self.assertEqual(2, linkedlist.get_size())

    def test_can_remove_middle_element(self):
        linkedlist = LinkedList()
        linkedlist.append(1)
        linkedlist.append(10)
        linkedlist.append(100)
        linkedlist.remove(1)
        self.assertEqual(2, linkedlist.get_size())


if __name__ == "__main__":
    unittest.main()