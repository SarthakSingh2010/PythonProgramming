kp=list(range(10))#make a list of 0-9 using range data type
print(kp)
nums = [25,12,16,95,43]
print(nums)
print('make a copy of nums')
mp=nums.copy()
print(mp)
print('1st value ',nums[0])
print('from index 2 till last index')
print(nums[2:])
print('last 3 element')
print(nums[-3:])
print('negative indexing')
print(nums[-5])#1st element.
names=['apple','mango','orange']
print(names)
values=[6.5,'sarthak',24]
print(values)
mil=[names,values]
print(mil)
print('accessing the mil elements:')
print('1st row:')
print(mil[0])
print('2nd row')
print(mil[1])
print('1st row 2nd element')
print(mil[0][1])
#list are mutable
print('append 25 at end')
nums.append(25) #append at end
nums=nums+[25] #another way to append
print(nums)
print('count all occurances of 25')
print(nums.count(25))# count occurances of 25 in list 
print('sort ascending')
nums.sort() #ascending order
nums.sort(reverse=True) #descending order
print(nums)
print('get reverse of list')
nums.reverse() #reverse the entire list
print(nums)
print('remove a element by its value')
nums.remove(16)#remove element 16
print(nums)
print('remove the last element')
nums.pop() #removes last element
print(nums)
print('remove element by index')
nums.pop(2)#remove element at index 2
print(nums)
print('Delete all element from index 2 till last "multiple deletion"')
del nums[2:]
print(nums)
print('append more than 1 element in list')
nums.extend([44,55,66,77,88,99])
print(nums)
print('index of 55')
print(nums.index(55))#error if not in list else index start from 0
print('insert 69 at index 2 in nums list')
nums.insert(2,69)
print(nums)
print('minimum ',min(nums))
print('maximum ',max(nums))
print('sumtotal ',sum(nums))
print('remove all element making it empty')
nums.clear() #clear entire list
print(nums)

#check if element is there in list or not reply as True or False
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
  
#List are mutable values can be changed
thislist[1]="mango"
print(thislist)

#get a 2d matrix code
print("enter content for 2d matrix")
arr=[]
for i in range(3):
    k=list(map(int,input().split()))
    arr.append(k)
print(arr) # thats a matrix with 3 rows

u=[1,2,3]
v=[1,2,3]
#set(u) & set(v) give intersection of 2 list as list
if len(set(u) & set (v))==len(u):
    print('Lists are same')
else:
    print('List are different')
    
    
print('List to string using join func')
k=['A','P','P','L','E']
print('.'.join(k))#only works for a list having str type elem

print('valid list builts')
k1=[1,2,3,4]
k2=[[1,2,3],[4,5,6],[7,8,9]]
k3=['A'+'PP','$'*3,7+4,3]
print(k1)
print(k2)
print(k3)

#convert 123 into [1,2,3]
lis=list(map(int,str(123)))
print(lis)