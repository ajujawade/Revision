# program 1

e = dict.fromkeys(["Ajay","Aditya","Raju"])

print(e)

info = {
    "admin":"aditya",
    "ceo": "ajay" ,
    "support":"Raj"
}

info.setdefault("manager",None)

info.update({"support":"ajay"})
print(info)

listName = ["ajay","aditya","raj"]

listName[0]="tony"
print(listName)
print(type(listName))


tupName = ("Ajay","Aditya","Tejas")
print(tupName)
print(type(tupName))


for x in tupName:
    print(x)
    
print(tupName[0])
# tupName[0] = "Tony"

tupleA = (11,22)
tupleB = ("Ajay","Tony")
tupleC = (["ajay","sam"],["raj","samvidhan"])
tupleD = 11,12

print(tupleC)
print(type(tupleD))    

names = ("ajay","tony","seema")

print(names[0])
print(names[1])
print(names[2])    


for x in range(len(names)):
    print(names[x])
    
for x in names:
    print(x)

i=0
while (i<len(names)):
    print(names[i])
    i = i+1

tupleE = (11,22,33)
a,b,c = tupleE

print(a)
print(b)
print(c)

tupleF = (11,22,33)
# print(len(tuple))
e = len(tupleF)
print(e)

f = list(tupleF)
print(f)
f.append(55)
print(f)

f = tuple(f)
print(f)

g = (11,8,22,33,44,55,66,77,8)
print(g)

e2 = g.count(8)
print(e2)

e3 = g.index(8)
print(e3)

e4 = ([11,22,33],[33,44,55],[55,66,77])
print(e4)
