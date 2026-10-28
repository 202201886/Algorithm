def selection_sort(arr):  #O(n^2)
     n = len(arr)
     
     for i in range(n): #i = 0~8
          big = 0
          for j in range(n-i): #j = 0~8, 0~7 ... 
               if arr[j] >= big:
                    big, index = arr[j], j
          arr[index] = arr[n-i-1]
          arr[n-i-1] = big           
     return arr           
  
a = [50, 4, 8, 94, 11, 20, 1, 3, 66]
print(selection_sort(a))