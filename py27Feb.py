# x =10
# print(x)

# x = 100
# print(x)

# a = 10
# b = 5

# def calculator(x,y):
#     print(x+y)
#     print(x-y)
#     print(x*y)
#     print(x/y)
#     print(x%y)

# e1 = calculator(10,5)
# print(e1)

# str = "ajay"

# e2 = str.split(2)
# print(e2)


# listA = ["Ajay","Aman","Shubham","Dollar"]
# print(listA)


# listA.append("Rajkumar")
# print(listA)

# listA.extend(["Shami"])
# print(listA)

# listA.insert(1,"Aju")
# print(listA)
    
# listA.remove("Shubham")
# print(listA)

# listA.pop()
# print(listA)

# e1 = listA.index("Aju")
# print(e1)

# listA.append("Ajay")
# e2 = listA.count("Ajay")
# print(e2)

# listA.reverse()
# print(listA)

# listB = listA.copy()

# listB[0] = "Aju"

# print(listA)
# print(listB)

# dict = {
#     "firstName" : "Ajay",
#     "lastName"  : "Jawade",
#     "age"       : 21
# }

# print(dict)

# for x in dict:
#     print(dict[x])

# # keys
# for keys in dict.keys():
#     print(keys)
    
# for values in dict.values():
#     print(values)
    
# print(dict.keys())

# for k,v in dict.items():
#     print(k,v)
    
# for items in dict.items():
#     print(items)
    
# print(dict.items())
    


# # CRUD

# # # retrive

# # print(dict["age"])

# # # update

# # dict["age"] = 20
# # print(dict)

# # # add

# # dict["address"] = "Pune"
# # print(dict)

# # # delete

# # dict.pop("lastName")
# # print(dict)


# # dict.popitem()
# # print(dict)

# dict.setdefault("Pincode", 442908)

# print(dict)

# dict.update({"Pincode":440015,"Friend":"Aju"})
# print(dict)

# # dictA = dict

# # dictA["age"] = 18
# dictA = dict.copy()

# dictA["age"] = 18
# print(dictA)
# print(dict)
# dictA = {
#     "color" : "red",
#     "type"  : "sedane"
# }

# print("Hello")
# print(dictA.get("color"))
# print("bye")
# a = dictA.get("typee")
# b = dictA["color"]

# print(a)
# print(b)

####################################################################################################################

# TUPLE

# tup = (11,22,22,33,44,55)
# print(tup)
# print(type(tup))

# c = tup.count(22)
# print(c)

# i = tup.index(33)
# print(i)

# for x in range(len(tup)):
#     print(tup[x])
    
# for x in tup:
#     print(x)

# #############################################################################################################

# SET

set1 = {11,22,33,44,55,66}

# print(set1[0])

print(set1)
print(type(set1))

set1.update({0,9,8,7,6,5,43,21})
print(set1)

set1.remove(0)

print(set1)

set1.pop()
print(set1)

set1.pop()
print(set1)

set1.discard(10)
print(set1)

set1.add(10)
print(set1)

set1.update([90,80,70,60])
print(set1)


set1.add(40)
print(set1)

set2 = {70,80,60,90,10,20,30,40}
diff = set1.difference(set2)

print(diff)


diff1 = set1.difference_update(set2)
print(diff1)






