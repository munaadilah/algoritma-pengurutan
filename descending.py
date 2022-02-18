from array import array


def quickSort(arr):
    if len(arr) <= 1:
        return arr

    left = []
    right = []
    equal = []
    pivot = arr[-1]

    for num in arr:
        if num > pivot:
            left.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            right.append(num)

    return quickSort(left) + equal + quickSort(right)

arrayBeelumUrut = [6, 5, 3, 1, 8, 7, 2, 4]
arrayTerurut = quickSort(arrayBeelumUrut)

print(arrayTerurut)