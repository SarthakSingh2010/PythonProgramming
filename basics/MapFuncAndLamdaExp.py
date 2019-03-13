# Python program to demonstrate working 
# of map. 
  
# Return double of n 
def addition(n): 
    return n + n 
  
# We double all numbers using map() 
numbers = (1, 2, 3, 4) 
result = map(addition, numbers) 
print(list(result)) 


# Double all numbers using map and lambda 
numbers = (1, 2, 3, 4) 
result = map(lambda x: x + x, numbers) 
print(list(result)) 

# Add two lists using map and lambda 
numbers1 = [1, 2, 3] 
numbers2 = [4, 5, 6] 
result = map(lambda x, y: x + y, numbers1, numbers2) 
print(list(result)) 

# List of strings 
l = ['sat', 'bat', 'cat', 'mat'] 
# map() can listify the list of strings individually 
test = list(map(list, l)) 
print(test) 

#sum of digits or how to convert 123 into [1,2,3]
print(list(map(int,str(123))))
print(sum(map(int,str(123))))

#lambda func : small anonymous func
#A lambda func can take any #args, but one expression 

x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))



