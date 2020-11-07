from bubble_sorting import sorting

def binary_search(list, value):

    if list == []:
        raise IndexError("list index out of range")

    if value == None:
        raise TypeError("Value should be 'str' or 'int' type")

    if type(value) == int:
        for i in list:
            if type(i) == int:
                pass
            if type(i) == str:
                raise TypeError("'>' not supported between instances of 'int' and 'str'")

    if type(value) == str:
        for i in list:
            if type(i) == str:
                pass
            if type(i) == int:
                raise TypeError("'>' not supported between instances of 'int' and 'str'")

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


# list = [100, 50, 20, 10]
# index = binary_search(list, 50)
# print(index)