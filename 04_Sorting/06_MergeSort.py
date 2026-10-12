def merge_sort(arr):

    if len(arr) <= 1: 
        return arr

    n = len(arr) // 2
    left = merge_sort(arr[:n])
    right = merge_sort(arr[n:])

    result = []
    while left and right:
        result.append(left.pop(0) if left[0] < right[0] else right.pop(0))

    return result + left + right


word = list('algorithm')
result = merge_sort(word)
print(''.join(result))