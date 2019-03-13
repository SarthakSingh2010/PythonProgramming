#problem 1 get a string if ending with 'ing' append 'ly' else append 'ing'
def ss(s):
    if len(s)<3:
        return s
    if s[-3:]=='ing':
        return s+'ly'
    return s+'ing'
print(ss(input('Enter a string: ')))
#problem 2 first 4 element in a list contain '9'
def aa(lis):
    if 9 in lis[0:4]:
        return True
    return False
print(aa(list(map(int,input('Enter a list: ').split()))))
#problem 3 if the list contain [1,2,3]
def bb(lis):
    for i in range(len(lis)-2):
        if lis[i]==1 and lis[i+1]==2 and lis[i+2]==3:
            return True
    return False
print(bb(list(map(int,input('Enter a list: ').split()))))
#problem 4 calc Amt D100 mean deposit 100 ,W100 withdraw, print net bal.
def cc(lis):
    amt=0
    for i in range(len(lis)):
        if lis[i][0]=='D':
            amt+=int(lis[i][1:])
        else:
            amt-=int(lis[i][1:])
    return amt
print(cc(list(input('Enter a list of string: ').split())))
#problem 5 pattern printing
n=int(input('Enter a number: '))
for i in range(1,n+1):
    for j in range(i,1,-1):
        print('.',end='')
    print('*')
#problem 6 if count of 'mat'==count of 'jet' in str return True
s=input('Enter a string: ')
s=s.lower()
if s.count('mat')==s.count('jet'):
    print('True')
else:
    print('False')
#problem 7 [1,2,3,4,5,6,7,8,9,10]-->[10,9,8,7,6,1,2,3,4,5]
def dd(lis):
    n=len(lis)
    k1=lis[:n//2]
    k2=lis[n//2:]
    k3=[]
    for i in range(len(k2)):
        k3.append(k2[-1-i])
    for i in range(len(k1)):
        k3.append(k1[i])
    return k3
print(dd(list(map(int,input('Enter a list: ').split()))))
#problem 8 ((1)) False   ((2)) True
def checkCorrectDepth(lis):
    c=0
    for i in lis:
        if i=='(':
            c+=1
        elif i==')':
            c-=1
        else:
            if int(i)!=c:
                return False
    return True
print(checkCorrectDepth(list(map(str,input('Enter a list: ')))))
#problem 9 represent n as sum of sqaures of 2 number
def fun(n):
    for i in range(1,int(n**0.5)+1):
        for j in range(1, int(n**0.5)+1):
            if (i**2+j**2)==n:
                return True
    return False
print(fun(int(input('Enter a number: '))))
#problem 10 Longest Commom SubString
def fun2(s1,s2):
    lis=[]
    for i in range(len(s1)):
        for j in range(len(s1)):
            if i<=j:
                lis.append(s1[i:j+1])
    #print(lis)
    m,st=0,''
    for i in range(len(lis)):
        if lis[i] in s2 and len(lis[i])>m:
            m=len(lis[i])
            st=lis[i]
    return st
s11=input('Enter a string: ')
s22=input('Enter a string: ')
print(fun2(s11,s22))
