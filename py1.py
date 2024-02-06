'''x = 10
print(x)

a = 23
b = 4

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)

def Calculator(x,y):
 print(a + b)
 print(a - b)
 print(a * b)
 print(a / b)
 print(a % b)
 
Calculator(20,3)
Calculator(24,3)

def Cal(x,y):
    return x+y

a1 = Cal(9,3)
print(a1)
Cal(a1,2)


def cal():
    print("Hello")
    
cal()
cal()

str = "   ajay jawade    "
print(str)

cap = str.capitalize()
print(cap)

upp = str.upper()
print(upp)

low = str.lower()
print(low)

titl = str.title()
print(titl)

ltr = str.lstrip()
print(ltr)

rtr = str.rstrip()
print(rtr)

trm = str.strip()
print(trm)

str1 = "Ajay"
print(str1.isalpha())

str2 = "Ajay06"
print(str2.isalnum())

str3 = "123"
print(str3.isdigit())

str4 = "1.23"
print(str4.isnumeric())

for x in str:
    print(x)
    
    
for x in range(len(str)):
    print(str[x])
    '''

'''str = "Ajay Jawade"
print(str[3:2:1])
print(str[0::])
print(str[0:3:2])
print(str[0:len(str):2])
print(str[1::2])

names =['ajay','jawade',45,54,65,'raju']

print(names)

names.append("Tony")
print(names)

names.remove(45)
print(names)

names.insert(0,"Bhalu")
print(names)

names.pop()
print(names)

#names2 = names
#names2.insert(0,"Kalu")
#print(names2)

names2 = names.copy()

print(names)
print(names2)

names2.append("Gullu")
print(names2)

ind = names.index("jawade")
print(ind)

names.extend(["Ajay","Ajay","tony","Kaju"])
print(names)

cou = names.count("Ajay")
print(cou)


names2.clear()
print(names2)

print("Ajay" in names)

names.reverse()
print(names)

'''
dict = {
    "first_name" : "Ajay",
    "last_name"  : "Jawade",
    "age"        : 20,
    "class"      : "BCA"
}

# Retrive

print(dict)

for key in dict.keys():
    print(key)
    
for value in dict.values():
    print(value)
    
for k,v in dict.items():
    print(k,v)

print(dict.keys())
print(dict.values())
print(dict.items())

#UPDATE

dict["age"] = 18

print(dict)

#Delete

dict.pop("last_name")
print(dict)

dict.popitem()
print(dict)

#ADD

dict["address"] = "Upparwahi"

print(dict)

a1 = dict.get("first_name")
print(a1)