import math as m #alias
#from math import sqrt,pow
#sqrt(9)
#pow(4,5)
print('convert decimal to binary')
print(bin(25)) #0b11001
print(0b0101)#bin to dec
print(oct(25))#dec to oct
print(0o31)#oct to dec
print(hex(25))#dec to hex
print(0xa)#hex to dec

#to get ASCII code of a Char
print(ord('A'))
#to convert Char to ASCII code
print(chr(66))

#dec to any base
def decToAnyBase(num,base):
    s=['A','B','C','D','E','F']
    res=''
    while num>0:
        rem=num%base
        if rem>9:
            res+=s[rem-10]
        else:
            res+=str(rem)
        num=num//base
    return res[::-1]

n=int(input('Enter a number: '))
b=int(input('Enter a base: '))
print(decToAnyBase(n,b))

#from any base to decimal
def val(p):
    if p>='0' and p<='9':
        return ord(p)-ord('0')
    return (10+ord(p)-ord('A'))
def anyBaseToDecimal(s,base):
    k=c=0
    for i in range(len(s)-1,-1,-1):
       k+=base**c*val(s[i])
       c+=1
    return k

sp=input('Enter a string: ')
b=int(input('Enter a base: '))
print(anyBaseToDecimal(sp,b))

#math func
#help('math')
print(m.sqrt(9))
print(m.floor(4.6))
print(m.ceil(4.6))
print(m.pi) #pi
print(m.e) #epsilon
print(m.tau) #tau const value
print(m.fabs(-3.4))#absolute value(non negative value)
print(m.factorial(5))# raises valueError if x is -ve or non-integral(5.4)
print(m.gcd(4,2))
print(m.log(10,2))#log 10 base 2
print(m.log10(10))#log 10 base 10
print(m.pow(2,3))
