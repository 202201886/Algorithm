mylist = [["co", 1, "Q"], ["bar", 0, "Z"], ["after", 3, "X"], ["data", 2, "Y"]]

sortlist = sorted(mylist)
print(sortlist)
print(mylist)

mylist.sort()
print(mylist) 
print(sorted(mylist, reverse=True))

print(sorted(mylist, key=lambda x:x[1]))  # sorted by index1 
print(sorted(mylist, key=lambda x:len(x[0])))  #sorted by length of index0