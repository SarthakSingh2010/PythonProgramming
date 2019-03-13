from itertools import permutations 
perm = permutations([1, 2, 3], 2) 
for i in list(perm): 
    print(i) 
  
# Answer->(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)
    
def allPermute(s): #str 
    k=[]
    l=list(permutations(s)) 
    strl = [''.join(item) for item in l]
    for i in strl:
        k.append(int(i))
    return k
print(allPermute('123'))

def remove_duplicates(s):
    p=''
    lis=list(map(str,s))
    lis.sort()
    for i in range(len(s)-1):
        if s[i]!=s[i+1] and s[i] not in p:
            p+=s[i]
    if s[len(s)-1] not in p:
        p+=s[len(s)-1]
    return p
print(remove_duplicates(input('Enter a String: ')))


def check_anagrams(s1,s2):
    lis_s1=list(map(str,s1))
    lis_s2=list(map(str,s2))
    lis_s1.sort()
    lis_s2.sort()
    if len(set(lis_s1) & set(lis_s2))==len(lis_s1):
        return True
    else:
        return False
s11=input('Enter String: ')
s12=input('Enter String: ')
print(check_anagrams(s11,s12))

def perfect(n):
    s=0
    for i in range(1,n):
        if n%i==0:
           s+=i     
    if s==n:
        return True
    else:
        return False
def perfect_extend(lis):
    k=[]
    for i in range(len(lis)):
        if perfect(lis[i])==True:
           k.append(lis[i])
    return k
print(perfect_extend(list(map(int,input('Enter a list: ').split()))))

#circular Prime
def prime(n):
    if n<2:
        return False
    if n==2 or n==3:
        return True
    if n%2==0 or n%3==0:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def circular(n):
    m=str(n)
    return int(m[-1]+m[:len(m)-1])

nk=int(input('Enter a limit: '))

for i in range(1,nk):
    if prime(i):
        flag=True
        p=circular(i)
        while(p!=i):
            if prime(p)==False:
                flag=False
                break
            p=circular(p)
        if flag==True:
            print(i,end=' ')
            
#Longest common substring
def fun2(s1,s2):
    lis=[]
    for i in range(len(s1)):
        for j in range(len(s1)):
            if i<=j:
                lis.append(s1[i:j+1])
    print(lis)
    m,st=0,''
    for i in range(len(lis)):
        if lis[i] in s2 and len(lis[i])>m:
            m=len(lis[i])
            st=lis[i]
    return st
s11=input('Enter a string: ')
s22=input('Enter a string: ')
print(fun2(s11,s22))

#all subset of a list
def fun3(lis):
    k=[]
    for i in range(len(lis)):
        for j in range(len(lis)):
            if i<=j:
                k.append(lis[i:j+1])
    return k
kp=list(map(int,input('Enter a list: ').split()))
print(fun3(kp))

#all consecutive counts
k=[1,0,0,0,1,1,0,0,0,2,2,2,1,1,1,0,0]
def consecutiveCount(k):
    p,c=[],1
    k.append('$')
    for i in range(len(k)-1):
       if k[i]==k[i+1]:
           c+=1
       else:
           p.append((k[i],c))
           c=1
    return p
print(consecutiveCount(k))