# lambda function

add = lambda x,y:x+y

result = add(12,8)
print(result)


# square

square = lambda x:x**2

result = square(21)
print(result)

# function as parameter to another function

add = lambda x,y : x+y

def addition(fn,x,y):
    result = fn(x,y)
    return result

res = addition(add,34,6)
print(res)

sub = lambda x,y:x-y

def substraction(fn,x,y):
    result = fn(x,y)
    return(result)
    
res = substraction(sub,20,8)

print(res)

# Program 4
# Function as a return type

def add():
    return lambda x,y:x+y

add = add()

result = add(35,9)

print(result)


dmas = lambda x,y:[x+y,x-y,x*y,x/y,x%y]

def cal(fn,x,y):
    result = fn(x,y)
    return result

result = cal(dmas,20,10)
print(result)

    



