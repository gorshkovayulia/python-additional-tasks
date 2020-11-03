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
        return ("No value")
        # print("No value")

    else:
        return middle
        # print("ID =", middle)

# list = [100, 50, 20, 10]
# index = binary_search(list, 50)
# print(index)