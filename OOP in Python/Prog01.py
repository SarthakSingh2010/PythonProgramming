#empty class
class Employee:
    pass
#create object
emp1=Employee()
#set attribute
emp1.first='Sarthak'
emp1.last='Singh'
emp1.pay=23000
emp1.email=emp1.first+'.'+emp1.last+'@company.com'
#create object
emp2=Employee()
#set attribute
emp2.first='Rohit'
emp2.last='Agarwal'
emp2.pay=34000
emp2.email=emp2.first+'.'+emp2.last+'@company.com'
#get attribute
print('Object Location:')
print(emp1)
print(emp2)
print('First Employee Detail:')
print(emp1.first)
print(emp1.last)
print(emp1.pay)
print(emp1.email)
print('Second Employee Detail:')
print(emp2.first)
print(emp2.last)
print(emp2.pay)
print(emp2.email)