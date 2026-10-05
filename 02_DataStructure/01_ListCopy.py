# Reference
a = [1,2,3]
b = a
b.append(5)
print('a: ', a)  #a: [1, 2, 3, 5]
print('b: ', b)  #b: [1, 2, 3, 5]

# Shallow Copy(not in list)
a = [1,2,3]
b = a[:]
b.append(5)
print('')
print('a: ', a)  #a: [1, 2, 3]
print('b: ', b)  #b: [1, 2, 3, 5]

a = [[1,2],[3,4]]
b = a[:]
b.append(5)
print('') 
print('a: ', a)  #a: [[1, 2], [3, 4]]
print('b: ', b)  #b: [[1, 2], [3, 4], 5]

# Shallow Copy(in list)
a = [[1,2],[3,4]]
b = a[:]
a[1].append(5)
print('')
print('a: ', a)  #a: [[1, 2], [3, 4, 5]]
print('b: ', b)  #b: [[1, 2], [3, 4, 5]]

# Deep Copy
import copy

a = [[1,2],[3,4]]
b = copy.deepcopy(a)
a[1].append(5)
print('')
print('a: ', a) #a: [[1, 2], [3, 4, 5]]
print('b: ', b) #b: [[1, 2], [3, 4]]