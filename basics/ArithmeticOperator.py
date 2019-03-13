print(5+2)
print(5-2)
print(5*2)
print(5/2) #float division
print(5//2) #integer division 
print(5%2) #remainder
print(5.0%2.0) #floating point number remainder possible
print(2**3) #power of 

#get user input and store it as string
s=input("Enter a String: ")
print(s)
print(type(s))

#get user input as char
m=input('Enter gender M or F: ')[0]
print(m)
print(type(m))

#get command line input
#cmd: python demo.py 3 4   here index is 0,1,2
#import sys
#x=int(sys.argv[1])
#y=int(sys.argv[2])
#print(x+y)

#input integer from user.
age=int(input("Enter your age: "))
print(type(age))
print("After 20 years your age will be : ",(age+20))

#input float from user
salary=float(input("Enter a salary : "))
print(type(salary))
print("adding 234.56 to salary we get : ",(salary+234.56))

#input integer array
a=[]
n=int(input('Enter the length : '))
print("Enter elements ::")
for i in range(0,n,1):
    a.append(int(input()))

#display array
for i in range(0,n,1):
    print(a[i],end=' ')    

#input in 1 line    
p=int(input("Enter length : "))
b=list(map(int,input().split()))
for i in range(0,p):
    print(b[i],end=' ')
print()    
    
#one liner for 2 variable
print('Enter 2 number: ')
w,x=map(int,input().split())
print(w)
print(x)

#int to string
print('Int to String')
u=4
k=str(u)
print(k)
print(type(k))

"""
RELATIONAL OPERATOR   ==,!=,>,<,<=,>=
LOGICAL OPERATOR   and,or,not
BITWISE AND  &
BITWISE OR   |
BITWISE XOR  ^
BITWISE NOT  ~
LEFT SHIFT   <<
RIGHT SHIFT  >>
"""

#while loop
i=1
while (i<6):
  print(i)
  i+=1

#break  
i=1
while (i<6):
  print(i)
  if (i==3):
    break
  i+=1
 
#continue    
i=0
while (i<6):
  i+=1 
  if (i==3):
    continue
  print(i)
  
#function
def my_function(x):
  return (5*x)

print(my_function(3))
print(my_function(5))
print(my_function(9))


#sum of digit
s=input('Enter a number as string: ')
k=0
for i in s:
   k+=int(i)
print(k)

#1D to 2D
n=int(input('Enter rows in square matrix: '))
print('Enter elments ',n*n,' seperated by spaces in 1 line:')
a=list(map(int,input().split()))
lis=[]
for i in range(0,n*n,n):
    lis.append(a[i:i+n])
print('2D output from 1D input:')
print(lis)
  
#extract number from string
p=input('Enter a alphanumeric string: ')
for i in p:
    if i.isdigit()==True:
        print(i,end=' ')
print()

#extract all alphabet digit and special character
s=input('Enter a alphanumericspecialcharacter string: ')
a,b,c='','',''
for i in range(len(s)):
    if s[i].isdigit():
        b+=s[i]
    elif s[i].isalpha():
        a+=s[i]
    else:
        c+=s[i]
print(a) #alphabet
print(b) #numbers
print(c) #special characters

#count vowels
s=input('Enter a string to count vowels: ')
c=0
for i in range(len(s)):
    if s[i] in 'aeiou':
        c+=1
print(c)

#leap year or not
def leap(y):
    if y%4==0 and y%100!=0 or y%400==0:
        return 'Yes'
    return 'No'

y=int(input('Enter a year: '))
print(leap(y))


#prime
def prime(n):
    if n<2:
        return 'No'
    if n==2 or n==3:
        return 'Yes'
    if n%2==0 or n%3==0:
        return 'No'
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 'No'
    return 'Yes'
n=int(input('Enter for prime check: '))
print(prime(n))