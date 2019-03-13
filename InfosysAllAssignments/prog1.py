#Assignment 7: Mandatory Level 1 2 string check for equality
s1=input('Enter a string: ')
s2=input('Enter a string: ')
if s1.lower()==s2.lower():
    print('Yes')
else:
    print('No')
def validate_employee(d,un,en): #dict usage
    if en in d.keys() and len(un)>=4:
        if un[:3]==d[en][:3] or un[-3:]==d[en][:3]:
            return True
    return False
emp_dict={1111:'Sim',1234:'Jomes',9999:'Amy',5555:'Jessica'}
print(validate_employee(emp_dict,'Jome',1234))
#Assignment 9: Mandatory Level 2 count unique occurances in sorted str
s3=input('Enter a string: ')
s3+='#'
c=1
for i in range(len(s3)-1):
    if s3[i]==s3[i+1]:
        c+=1
    else:
        print(str(c)+s3[i],end='')
        c=1
#Assignment 10 Level 2 Display All common characters between 2 String
s4=input('Enter a String: ')
s5=input('Enter a String: ')
if len(s4)<len(s5):
    for i in range(len(s4)):
        if s4[i] in s5 and s4[i]!=' ':
            print(s4[i],end='')
else:
    for i in range(len(s5)):
        if s5[i] in s4 and s5[i]!=' ':
            print(s5[i],end='')
#Assignment 11 Level 2 for a range find no. whose sumofdigit divisible by 3 
#len(no.)==2 and no. divisible by 5
num1=int(input('Enter a number: '))
num2=int(input('Enter a number: '))
if num2<num1:
    print(-1)
else:
    lis=[]
    for i in range(num1,num2+1):
        if sum(map(int,str(i)))%3==0 and len(str(i))==2 and i%5==0:
            lis.append(i)
    if len(lis)!=0:
        print(max(lis))
    else:
        print(-1)
#Assignment 12  level 2 anagram(num)==anagram(num*2)
def check_double(num):
    lis1=list(str(num))
    lis2=list(str(num*2))
    lis1.sort()
    lis2.sort()
    if len(set(lis1)& set(lis2))==len(lis1) and len(lis1)==len(lis2):
        return True
    return False
print(check_double(int(input('Enter a number: '))))
#Assignment 13 Level 1 Duplicate remove
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
#Assignment 14 Level 2 Anagrams
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
#Assignment 15 Level 1 Perfect Number
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
#Assignment 16 Level 2 Circular Prime
def prime(n):
    if n<2:
        return False
    if n==2:
        return True
    if n%2==0:
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
#Assignment 17 Level 2 User validation
def validate_name(s):
    if s!='' and len(s)<=15 and s.isalpha()==True:
        return True
    return False

def validate_phone_no(n):
    if len(n)==10 and n.isdigit()==True and n.count(n[0])!=len(n):
        return True
    return False

def validate_email_id(d):
    if '.com' in d and d.count('@')==1:
        if d[d.index('@')+1:d.index('.com')] in ['gmail','yahoo','hotmail']:
            return True
    return False

def validate_all(n,p,e):
    if validate_name(n) and validate_phone_no(p) and validate_email_id(e):
        return True
    return False

n=input('Enter a name: ')
p=input('Enter a phone number: ')
e=input('Enter a email id: ')
print(validate_all(n,p,e))
