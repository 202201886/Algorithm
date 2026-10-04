lst1 = [1, 5, 1]
lst2 = ['Hello', 'Python']
lst2.append(0.999)  #append 0.999 to lst2

print(lst1 + lst2)
print(2 * lst1)
print(lst2[-1])  #lst2[-1] is last element of lst2

lst1.count(1)      #2
lst2.index(0.999)  #2

lst1.extend(lst2)  #extend lst1 with lst2
print(lst1)    
print(lst2)

lst1.insert(0, 100)  #insert 100 at index 0
lst1.insert(3, 70)
print(lst1)

lst2.reverse() #reverse the order of lst2
print(lst2)

lst1.remove(1)  #remove first occurrence of 1 from lst1
print(lst1)

lst3 = lst1.copy()  #copy lst1 to lst3
print(lst3)
lst1.remove(1)
print(lst1)
print(lst3) #not affected by the removal of 1 from lst1

lst3.clear()  #clear all elements from lst3
print(lst3)

lst3 = [4, 2, 5, 0.99, -100, 77, 100, -123.456]
lst3.sort()  #sort lst3 in ascending order
print(lst3)

a = len(lst3)  #length of lst3
print(a)

#List Indexing
l = [1, 2, 3, 4, 5]
l[1] = 20   # [1, 20, 3, 4, 5]
l[3] *= 10  # [1, 20, 3, 40, 5]
l[-1] -= 5  # [1, 20, 3, 40, 0]

#List Slicing
lst = [1, 2, 3, 40, 500, 0.6, 7, 80, 9000]
lst[1:4]  # [2, 3, 40]

a = lst[:]
print(a)     #[1, 2, 3, 40, 500, 0.6, 7, 80, 9000]

a = lst[::2]  
print(a)     # [1, 3, 500, 7, 9000]

a = lst[:-1]
print(a)     # [1, 2, 3, 40, 500, 0.6, 7, 80]

a = lst[::-1]
print(a)     # [9000, 80, 7, 0.6, 500, 40, 3, 2, 1]

