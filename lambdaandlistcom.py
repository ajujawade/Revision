# def add(x,y):
#     return x+y

# e = add(9,8)
# print(e)

# add = lambda x,y:x+y

# res = add(34,6)

# print(res)


# names = ['Ajay','Tony','Aditya','Tejas']

# def changeName(lst):
#     lst[0] = "Sam"
#     return lst

# updatedlist = changeName(names)
# print(updatedlist)

# city = ['pune','nagpur','kolkata']

# city2 = city

# city[1] = 'wardha'

# print(city)
# print(city2)


# listA = [1,2,3,4,5]

# n =  []

# for i in listA:
#     n.append(i*5)
    
# print(n)

# listB = [1,2,3,4,5]

# new = [i*5 for i in listB]
# print(new)

# listC = [44,55,66,77,88,99,11,22,33,44,55,7,8,9]

# listD = []

# for x in listC:
#     if x > 50:
#      listD.append(x)
     
# print(listD)

# newli = [i for i in listC if i >50]
# print(newli)

# new = [x for x in listD if x%2 == 0]
# print(new)

# names = ['ajay','sarika','snehal','raj']

# cap = [x.capitalize() for x in names ]
# print(cap)

# upp = [x.upper() for x in names ]
# print(upp)

# out = [i[0] for i in names ]
# print(out)


listofDict = [{
    
    "firstName" : "Ajay",
    "lastName"  : "Jawade",
    "age"       : 20,
    "vehicle"   : True
},
{
    "firstName" : "Tejas",
    "lastName"  : "Jawade",
    "age"       : 16,
    "vehicle"   : True  
},
{
    "firstName" : "Aditya",
    "lastName"  : "Jawade",
    "age"       : 13,
    "vehicle"   : False
}]

firstName = [i["firstName"] for i in listofDict]
print(firstName)

lastName = [i['lastName'] for i in listofDict]
print(lastName)


num = [11,22,33,44]

out1 = ["Even" if i%2 == 0 else "Odd" for i in num]

print(out1)

out2 = [i['firstName'] if i['age']>18 and i['vehicle']== True else None for i in listofDict]

print(out2)

out3 = [x for x in out2 if x!=None]
print(out3)

out4 = [x['firstName'] + ":" + ("Can Drive" if x['age'] > 18 and x['vehicle']==True else "Cannot Drive") for x in listofDict ]
print(out4)




