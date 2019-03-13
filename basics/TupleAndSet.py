'''
list : value can be changed (the original list is modified) mutable
tuple : value can't be changed (non mutable)
list, tuple : collection of homogenous or heterogenous element
list is denoted by sqaure bracket []
tuple is denoted by round bracket ()
'''
tup=(44,7,8,65,21,90,5,22,7,11,55,7)
print(tup)#we cannot append or change value at index 
#iteration is faster in tuple than in list
print('first element ',tup[0])
print('slicing from index 2 to 5',tup[2:6])
print('count occurance of 7 in tuple ',tup.count(7))
print('index of 7 in tuple ',tup.index(7))#1st index


#set : denoted by curly brackets (like in maths)
#set : doesnot follow insert sequence at the time of display
#set uses hashing concept and also doesnot allow duplicates
#In set indexing is not allowed like p[2] is not allowed
p={22,25,14,21,5}
q={1,5,22,67,89}
n=q.copy()
print('copy of q and changes made to q will not affect n ',n)
print(p) #not always sorted order 
print(len(p))
for i in p:
    print(i,end=' ')
print()
'''
The only difference between the two is that, while using discard() 
if the item does not exist in the set, it remains unchanged. 
But remove() will raise an error in such condition.
Similarly, we can remove and return an item using the pop() method.
'''
print('remove 21 in p')
p.discard(21)
print(p)
print('add more than 1 element in set say [45,33] as list')
p.update([45,33])
print(p)
print('union')
a=p|q
print(a)
print('intersect ',p&q)
print('difference ',p-q)#elements in p not in q {25,14,21}
print('add 79 in set p ')
p.add(79)
print(p)
print('clear set a')
a.clear()
print(a)