a = "Python is fun"
print(len(a))  # 13
print(a[0]+a[7]+a[10])  # Pif
print(a[:6])  # Python
print(a[-3:])  # fun

s = "This is the class of Python programming!"
s.startswith('t')  # False
s.startswith('T')  # True
s.endswith('!')  # True

s.count('i')  # 3
s.count('t')  # 2

s.index('i')  # 2
s.index('i', 3)  # 5 (starts searching from index 3)
s.index('class')  # 12 (if not found, raises ValueError)

s.find("class")  # 12
s.find("Python")  # 21 (if not found, returns -1)

s.upper()  # 'THIS IS THE CLASS OF PYTHON PROGRAMMING!'
s.lower()  # 'this is the class of python programming!' 

#string split
a = "Hello World Python is Fun!!"
words = a.split()  # ['Hello', 'World', 'Python', 'is', 'Fun!!']
b = '123.0\t12.99\t78.12\t-0.345'
nums = b.split('\t')  # ['123.0', '12.99', '78.12', '-0.345']

#string join
a = ['Hello', 'World', 'Python', 'programming']
x = ' '.join(a)
print(x)  # Hello World Python programming