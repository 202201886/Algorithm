def merge_sort(arr):  #O(nlogn)

    if len(arr) <= 1: 
        return arr

     #deviding
    n = len(arr) // 2
    left = merge_sort(arr[:n])
    right = merge_sort(arr[n:]) 

    #merging
    result = []
    while left and right:
        if left[0] < right[0]:
             result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    return result + left + right

word = list('algorithm')
result = merge_sort(word)
print(''.join(result))