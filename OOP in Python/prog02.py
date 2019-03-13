#create class
class Employee:
    
    numofemp=0  #static variable or class variable
    raiseAmt=1.04 #class variable (shared by all objects)
    
    def __init__(self,first,last,pay): #constructor 2dash init (initialize)
        self.first=first #self.fname=first (allowed)
        self.last=last #self is like this
        self.pay=pay
        self.email=first+'.'+last+'@company.com'
        Employee.numofemp+=1
    
    @classmethod #decorator
    def fromString(cls,s): #name always start with 'from' convention
        first,last,pay=s.split('-') #alternate constructor
        return cls(first,last,pay)
        
    def fullName(self): #create a method (regular method)
        return self.first+' '+self.last #instance variables (unique to obj)
    
    def applyRaise(self):
        self.pay=int(self.pay*Employee.raiseAmt) #using class variable
                                                 #self.raiseAmt(allowed) 
    @classmethod #decorator
    def setRaiseAmt(cls,amt): #class method
        cls.raiseAmt=amt   
    
    @staticmethod #static method
    def isWorkDay(day): #0 denote sunday
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True
        
emp1=Employee('Sarthak','Singh',23000)
emp2=Employee('Rohit','Agarwal',34000)
print(emp1.email)
print(emp2.email)
print(emp1.fullName()) #another way of calling
print(emp2.fullName()) #Employee.fullname(emp2)
#pay raise
print(emp1.pay)
emp1.applyRaise()
print(emp1.pay)
print(Employee.numofemp) #get no. of employees
#set raise amt
Employee.setRaiseAmt(1.05)
print(Employee.raiseAmt)

#make a new emp from this str 'Aman-Jha-25000'
#concept of alternative constructor
emp3=Employee.fromString('Aman-Jha-25000')
print(emp3.email)

#using static method
import datetime
my_date=datetime.date(2019,2,21)
print(Employee.isWorkDay(my_date))