# Simple Function

def addA(x,y):
    return x+y

q1 = addA(11,22)
print(q1)

# Positional Argument

def subA(x,y):
    return x - y

q2 = subA(22,5)

print(q2)

# Default arguments

def mulA(x=5,y=9):
    return x * y

q3 = mulA()
print(q3)

# Variable Length Arguments

def addAll(*args):
    print(args)
    
addAll(1,2,3,4,5,6,7,8)

# Addition of all arguments Passed

def addall(*args):
    
   total = 0
   for i in args:
     total = total + i
   return total

result = addall(2,3,5,12,44,67,3)
print(result)

def greet(*args):
    for i in args:
        print("Welcome "+i)
        
greet("Pune","Nagpur","Chandrapur","Korpana")


def printinfo(**kwargs):
    print(kwargs)
    for i in kwargs:
        print(i)
        
printinfo(firstName="Ajay",lastName ="Jawade",age=20)




