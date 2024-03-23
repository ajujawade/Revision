

# class Person:
    
#     count = 0
#     country = "India" 
#     def __init__(self,fn,ln,age,salary):
        
#         self.firstName = fn
#         self.lastName =ln
#         self.age = age
#         self.salary = salary
        
#         Person.count = Person.count + 1
        
#     def displayName(self):
#         print(self.firstName + " " + self.lastName)
        
#     def updateAge(self,ag):
#         self.age = ag
    
#     def updateSalary(self,sal):
#         self.salary = sal
        
#     @classmethod
#     def updateCountry(self,cntry):
#         self.country = cntry
        
#     @staticmethod
#     def countObj():
#         print(Person.count)
        
# ajay = Person("Ajay","Jawade",20,100000)

# tony = Person("Tony","Stark",30,8000000000)

# aditya = Person("Aditya","Sorde",22,900000)

# ajay.displayName()
# tony.displayName()
# aditya.displayName()

# print(ajay.country)
# print(tony.country)
# print(aditya.country)

# Person.updateCountry("Bharat")

# print(ajay.country)
# print(tony.country)
# print(aditya.country)

# Person.countObj()






class Person:
    
    country = "India"
    count = 0
    
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln
        Person.count = Person.count + 1
        
    def displayName(self):
        print(self.firstName + " " +self.lastName)
        
    @classmethod
    def updateCountry(self,cntry):
        self.country = cntry
        
    @staticmethod
    def countobj():
        return Person.count
        
ajay = Person("Ajay","Jawade")
tony = Person("Tony","Jawade")


ajay.displayName()

c = ajay.countobj()
print(c)

ajay.updateCountry("Bharat")


tony.country = "US"

print(ajay.country)
print(tony.country)








