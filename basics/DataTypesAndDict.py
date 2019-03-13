'''
DataTypes:
    None(NULL)
    Numeric(int,float,complex(a+bj),bool)
    Sequence(List,tuple,set,string,range)
    mapping(dictionary)
'''
num=None
print(type(num))
num=5
print(type(num))
num=5.4
print(type(num))
num=3+4j
print(type(num))
num=True
print(type(num))
#Type Casting
num=4.5
print(int(num))
num=4
print(float(num))
a=3
b=5
print(complex(a,b))
print(complex(a))
print(a.imag,a.real)
k=True
print(int(k))
lis=[1,2,3,4]
print(type(lis))
tup=(1,2,3,4)
print(type(tup))
se={1,2,3,4}
print(type(se))
k='abc'
print(type(k))
m=range(10)
print(m)
print(type(m))

'''Dictionary (every element has a key which is unique)'''

dp={'A':'Apple','B':'Banana','C':'Banana','D':'Donkey'}
print(dp)
print(type(dp))
dp_keys=dp.keys()
print(dp_keys)
print(type(dp_keys))
print(dp.values())
print(dp['A']) #get element
print(dp.get('A')) #get element
dp['E']='Ema' #add new element
print(dp)
#remove a dictionary
del dp['E'] #or del [dp['E']]
print(dp)
#convert a dictionary to list
lis_dp=[]
for x,y in dp.items():
    lis_dp.append([x,y])
print(lis_dp)
print('individual access :: ',lis_dp[0],lis_dp[0][0],lis_dp[0][1]) 

#aeiou in string
dp={'a':0,'e':0,'i':0,'o':0,'u':0}
s=input('Enter a string :: ')
s=s.lower()
for i in range(len(s)):
    if s[i] in dp.keys():
        dp[s[i]]+=1
        
dpk=[]
for x,y in dp.items():
    dpk.append([x,y])
print('len: ',len(dpk))
for i in range(len(dpk)):
    print(dpk[i][0],dpk[i][1])