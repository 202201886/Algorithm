def bubble_sort(arr):  #O(n^2)
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

a = [50, 4, 8, 94, 11, 20, 1, 3, 66]
print(bubble_sort(a))