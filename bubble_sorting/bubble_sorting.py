def sorting(list):

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