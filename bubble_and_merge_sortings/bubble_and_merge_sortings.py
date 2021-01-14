from interface import implements, Interface


class Sorter(Interface):

    def sort(self, list):
        """Sort list in ascending order by 'Bubble sort' or 'Merge sort' algorithm."""
        pass


class BubbleSorter(implements(Sorter)):

    def sort(self, list):
        if list is None:
            raise TypeError("No list!")
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(list) - 1):
                if list[i] > list[i + 1]:
                    temp = list[i]
                    list[i] = list[i + 1]
                    list[i + 1] = temp
                    swapped = True


class MergeSorter(implements(Sorter)):

    def _merge(self, left_list, right_list):
        sorted_list = []
        left_list_index = right_list_index = 0
        left_list_length = len(left_list)
        right_list_length = len(right_list)

        for i in range(left_list_length + right_list_length):
            """Compare the first elements of the each sub-list."""
            if left_list_index < left_list_length and right_list_index < right_list_length:
                if left_list[left_list_index] <= right_list[right_list_index]:
                    sorted_list.append(left_list[left_list_index])
                    left_list_index += 1
                else:
                    sorted_list.append(right_list[right_list_index])
                    right_list_index += 1
            elif left_list_index == left_list_length:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
            elif right_list_index == right_list_length:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
        return sorted_list

    def sort(self, list):
        if list is None:
            raise TypeError("No list!")
        if len(list) <= 1:
            return list
        middle = len(list) // 2
        left_list = self.sort(list[:middle])  # Sort and merge left sub-list
        right_list = self.sort(list[middle:])  # Sort and merge right sub-list
        return self._merge(left_list, right_list)  # Merge sorted sub-lists into one sorted list

