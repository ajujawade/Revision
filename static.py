class Bank:
    
    country = "India"
    count = 0
    
    def __init__(self,fn,ln,acc,bal):
    
         self.firstName = fn
         self.lastName = ln
         self.accNo = acc
         self.balance = bal
         self.transactions = []
         Bank.count = Bank.count + 1
    
    def deposit(self,amount):
    
         self.balance = self.balance + amount
         self.transactions.append(amount)
         
    def withdrawl(self,amount):
        
        if(self.balance > amount):
            self.balance = self.balance - amount
            self.transactions.append(-amount)
        else:
            print("Insufficient Balance")
            
    def lastFiveTransaction(self,x):
        return self.transactions[-x::]
    
    @classmethod
    def changeCountry(cls,cl):
        cls.country = cl
        
    @staticmethod
    def countObj():
        return Bank.count
    
ajay = Bank("Ajay","Jawade",123456,5000)

print(ajay.firstName)
print(ajay.lastName)
print(ajay.accNo)
print(ajay.balance)

print(ajay.country)        
ajay.changeCountry("Bharat")
print(ajay.country)

ajay.withdrawl(2000)
ajay.deposit(500)
ajay.deposit(50000)
ajay.deposit(90000)
ajay.withdrawl(10000)
ajay.withdrawl(90000)
print(ajay.balance)
print(ajay.lastFiveTransaction(8))
ajay.countObj() 
