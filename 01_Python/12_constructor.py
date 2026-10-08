# class is blueprint
class Calculator:
    def __init__(self):  #constructor(auto execution)
        self.result = 0  #initializing

    def adder(self, num):
        self.result += num
        return self.result

cal1 = Calculator()  #making an instance & result = 0
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
ob.a = 500  #object variable, not class variable
print(MyClass.a, ob.a)

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "({},{})".format(self.x,self.y)  #x=?, y=? -> (x,y)

    def __add__(self, other):  #self -> p1, other -> p2
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)  #making a new instance 

p1 = Point(2,3)
p2 = Point(-1,2)
print(p1 + p2)  #(1,5)