# class is blueprint
class Calculator:
    def __init__(self):  #constructor(auto execution)
        self.result = 0  #initializing

    def adder(self, num):
        self.result += num
        return self.result

cal1 = Calculator()  #making a object & result = 0
cal1.adder(3)

#constructor isn't necessary
class MyClass:
    a = 10
    def func(self):
        print('Hello')

print(MyClass.a)
MyClass.a = 200

ob = MyClass()
ob.func()

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x,self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)  

p1 = Point(2,3)
p2 = Point(-1,2)
print(p1 + p2)  #(1,5) 