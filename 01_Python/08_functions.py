def funct(x, y=1, z=0):  #default arguments(from back)
    return x + y + z

funct(100)  #101
funct(5, 50)  #55
funct(1, 2, 3)  #6

def funct2(*nums):  #variable size arguments
    result = 0;
    for v in nums:
        result += v
    return result

funct2(1, 2, 3)  #6
funct2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)  #55

def funct3(op, *args):
    if op == 'add':
        result = 0
        for n in args:
            result += n
        return result
    elif op == 'mul':
        result = 1
        for n in args:
            result *= n
    
    return result

funct3('add', 1, 2, 3, 4, 5)  #15
funct3('mul', 3, 4, 5)  #60