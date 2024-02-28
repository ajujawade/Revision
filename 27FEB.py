info = {
    "firstName" : "Ajay",
    "lastName"  : "Jawade",
    "age"       : 20,
    "rollNo"    : 1234
}

print(info)
print(info["firstName"])

y = info.setdefault("city","pune")
print(y)
print(info)

info1 = dict.fromkeys(["keyone","keytwo","keythree"])
print(info1)

students = [
    {
    "firstName" : "Ajay",
    "lastName"  : "Jawade",
    "age"       : 20,
    "skills"    : ["c","c++","python","js","sql"]
},
{
    "firstName" : "Rajkumar",
    "lastName"  : "Bawanr",
    "age"       : 23,
    "skills"    : ["c","c++","sql"]
},
{
    "firstName" : "Harshal",
    "lastName"  : "Thawari",
    "age"       : 18,
    "skills"    : ["c","c++"]
},
{
    "firstName" : "Tony",
    "lastName"  : "Jawade",
    "age"       : 21,
    "skills"    : ["python","js","sql"]
}
]
print(students[3]["firstName"])

for x in students:
    print(x["firstName"])
    
    
# Students with Python Skill

for x in students:
    if "python" in x["skills"]:
        print(x["firstName"])
   
#  Skill == python and age > 18  
        
for x in students:
    if x["age"] > 20 and x["skills"] =="python":
        print(x["firstName"])
        
# name and number of skills

for x in students:
    print(x["firstName"]+":"+str(len(x["skills"])))

# average age of all students

total = 0

for x in students:
    total = total + x["age"]

average = total/len(students)
print(average)
