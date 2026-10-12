def insertion_sort2(arr, i=1):  #O(n^2)
    if i >= len(arr):
        return arr

    key = arr[i]
    j = i - 1

    while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key

    return insertion_sort2(arr, i + 1)


a = [50, 4, 8, 94, 11, 20, 1, 3, 66]
print(insertion_sort2(a))