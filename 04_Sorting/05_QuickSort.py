def quick_sort(arr):  #O(nlogn)
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

a = [50, 4, 8, 94, 11, 20, 1, 3, 66]
print(quick_sort(a))