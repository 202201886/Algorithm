t = (1, "Hello", 2017, True)
print(t[0])  # 1
print(t[1])  # Hello

t = (1, 2, 2, 2, 3, 4, 5)
len(t)  # 7
t.index(3)  # 4
t.count(2)  # 3
# t[0] = 100 -> Error: 'tuple' can't be modified

tup = ([3, 4, 5], 'myname')
tup[0][0] = 300  
# ([300, 4, 5], 'myname') -> list in tuple can be modified

message = "Welcome to Python!"
message[0] = 'p'
print(message)  # Error: 'str' instance can't be modified