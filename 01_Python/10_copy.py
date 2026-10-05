import copy

o = [1, [2, 3], 4]
s = copy.copy(o)  #shallow copy
d = copy.deepcopy(o)  #deep copy
o[1][0] = 200
print('o: ', o)
print('s: ', s)
print('d: ', d)