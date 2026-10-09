#not allow duplicate values
#no order

set1 = {1, 2, 3}
set2 = {2, 4, 5}

set1|set2
set1.union(set2)

set1&set2
set1.intersection(set2) 

set1-set2
set2-set1
set1.difference(set2)

set1.add(4)  #set1 = {1, 2, 3, 4}
set1.update(set2)  #set1 = {1, 2, 3, 4, 5}
set1.pop() #pop an arbitrary set element
set1.discard(3)  #set1 = {2, 4, 5}
#set1.remove(3) -> KeyError
set1.remove(2)  #set1 = {4, 5}
set2 = set1.copy()  #set2 = {4, 5}
set1.clear()  #set1 = {}

"""
lst = [1, 2, 3, 2, 1, 5, 4, 1, 3, 2, 4, 5, 1, 2, 4, 5, 2]
lst_result = list(set(lst))
print(lst_result)  -> not allow duplicate values

list -> []
set -> {}
tuple -> () 
"""