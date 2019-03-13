#inheritance
class Employee:
    
    raiseAmt=1.04
    
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@company.com'
        
    def fullname(self):
        return self.first+' '+self.last
    
    def applyRaise(self):
        self.pay=int(self.pay*self.raiseAmt) #Employee.raiseAmt=1.04
                                             #always
class Developer(Employee):#Developer inherits from Employee
    
    raiseAmt=1.10
    
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang=prog_lang
        
class Manager(Employee):
     #list of people they supervises
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees
        
    def addEmp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
       
    def removeEmp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
        
    def printEmp(self):
        print('\n==Start==\n')
        for emp in self.employees:
            print('--> ',emp.fullname())
        print('\n==End==\n')

#method resolution order: Developer->Employee->builtins.object
#print(help(Developer))

dev1=Developer('Sarthak','Singh',25000,'Python')
dev2=Developer('Ashok','Chopra',34000,'Java')

print(dev1.email)
print(dev1.prog_lang)
print(dev2.email)
print(dev2.prog_lang)
#it takes raiseAmt as 1.10 and not what was in superclass 1.04
print(dev1.pay)
dev1.applyRaise()
print(dev1.pay)

mgr1=Manager('Sapriti','Kumar',90000,[dev1])
print(mgr1.email)
mgr1.addEmp(dev2)
mgr1.printEmp()
mgr1.removeEmp(dev1)
mgr1.printEmp()
