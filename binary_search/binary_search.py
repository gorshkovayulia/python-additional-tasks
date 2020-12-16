from bubble_sorting.bubble_sorting import sorting


def binary_search(list, value):

    if value is None:
        raise TypeError("The list cannot be None")

    middle = len(list) // 2
    low = 0
    high = len(list) - 1

    while list[middle] != value and low <= high:
        if value > list[middle]:
            low = middle + 1
        else:
            high = middle - 1
        middle = (low + high) // 2

    if low > high:
        return -1
    else:
        return middle