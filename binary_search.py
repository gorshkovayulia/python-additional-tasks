from bubble_sorting import sorting

def binary_search(list, value):
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
        print("No value")
    else:
        print("ID = ", middle)


# list = [10, 0, -1,  2, 4, 3]
# sorting(list)
# binary_search(list, 10)
