x=4
#we cannot make var constant in python
print(x+3)
print('address of x ',id(x))#internal address of var
print('Hello World') #print func ends with \n by default.
print(" 'hello' 'world' ")
print(' "hello" "world" ')
print('hello \'world\' ')
print('hello\tworld')
print('hello\nWorld')

#compare strings
s1='abc'
s2='abc'
if s1==s2:
    print('same')
else:
    print('not same')

#string to int
s='18'
print(int(s),type(int(s)))

p='SARTHAK'
print(len(p))
print(p[6]) #indexing p[6] = 'K' 
print(p[0:4]) #p[0] to p[3] = 'SART'
print(p[-2]) #parse from right to left 1:K ,2:A
print(p[3:]) #from 3 till end
print(p[-3:])#last 3 element in string
print(p[:5]) #from start till index 4
print(p[:]) #from start till end
print(p[3:10]) #prints till end without giving INDEX_OUT_OF_BOUND.
print(p[::-1]) #reverse a string
print(p[2:-1])#index 2 to 2nd last index 'RTHA'

#Strings are immutable in Python
k=3.14
v=(4/3)*k*(x**3)
print(type(x)) #find type of a variable.
print('volume of a sphere of radius ',x,' = ',v);

#FORMAT SPECIFIER.
print('volume of a sphere of radius %.2f is %.2f' %(x,v))
print(type(x)) #find type of a variable.

print(f'volume of a sphere of radius {x} is {v}')

for i in range(1,4):
    for j in range (1,i+1):
        print('*',end="") #print without newLine.
    print()  #it contains \n by default

y=8    
if(y%2==0):
    print("EVEN")
else:
    print("ODD")
    
y=6
if(y%3==0):
    print("Multiple Of 3")
elif(y%5==0):
    print("Multiple Of 5")
else:
    print("Not a multiple of 3 Or 5")
    
q=7
if(q==7):
    print("Its seven")

#COMPLEX NO.
u=3+5j
print(u)
print(type(u))

pq,rs,uv=1,2,3
print(pq,rs,uv)
qp=1;sr=2;vu=3
print(qp,sr,vu)
aa=bb=cc='same'
print(aa,bb,cc)

#STRING LIBRARIES
print('String Functions')
k='sarthak singh'
print(k[1]) # a
print(k[2:7]) # rthak
k=k.upper()
print(k.isupper())
print(k)
k=k.replace('S','T')
print(k)
po=k.split()
print(po)
print(type(po))

print(' amplitude '.strip())#remove whitespaces from ends of the string
mp='123abca#'
print(mp.startswith('1'))
print(mp.endswith('#'))
print(mp.index('a'))
print(mp.rindex('a'))
print('123abc'.isalnum())# contain only digit and alphabet 
print('123'.isdigit())#contains digit alone
print('abc'.isalpha())#contains alphabet alone
print('apple'.count('p'))
print('apple app'.capitalize())#only 1st word 1st letter capitalized
print('apple app'.title())#1st letter of every word capitalized
print('app'.swapcase())
print(mp.find('abc',0,len(mp)))#find substring from startpos to endpos
print('the cat is not a dog'.find('not'))#return start index 
print('the cat is not a dog'.find('man'))#not found return -1

num_word='123456789'
#[begin:end:step]
print(num_word[::2]) #13579
print(num_word[1::2]) #2468
print(num_word[1:7:2]) #246
print(num_word[::-1])#987654321
print(num_word[::-2])#97531
