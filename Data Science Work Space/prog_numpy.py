import numpy as np
import matplotlib.pyplot as plt
lis1=list(range(1,5))
arr=np.array(lis1)#make list into numpy arrays
print(arr)
lis2=[11,22,33,44]
lis3=[lis1,lis2]
arr2=np.array(lis3)
print(arr2)
print(arr2.shape)#(rows,columns)
print(arr2.dtype)#obj type it stores
print('array of zeros')
arr3=np.zeros(5)
print(arr3)#dtype: float64
print('array of ones')
arr4=np.ones([5,5])#5 rows ,5 colms
print(arr4)#dtype: float64
print('identity array')
arr5=np.eye(5)#square matrix (5,5)
print(arr5)#dtpye: float64
print('use of arange func')
arr6=np.arange(2,51,2)#range(start,stop+1,step)
print(arr6)
'''arrays and scalars'''
arr7=np.array([[1,2,3,4],[8,9,10,11]])
print(arr7)
print(arr7*arr7)#arr[i][j]*=arr[i][j]
#can also do things like (+,*,/,-,**)
print(1/arr7)
'''indexing array'''
arr8=np.arange(0,11)
print(arr8)
print(arr8[3])#at index 3
print(arr8[1:5])#slicing
arr8[0:5]=100#mutable
print(arr8)
arr8[:]=0#make all elem = 0
print(arr8)
'''
In numpy data is not copied so any changes made to slice 
of array effect the original array too , done to preserve memory
'''
#to make a copy
arr9=arr8.copy()
print(arr9)
#index 2D matrix
arr10=np.array([[5,10,15],[20,25,30],[35,40,45]])
print(arr10)
print(arr10[1])#print row
print(arr10[1][0])#print elem
#2D array slicing
#[[10,15],[25,30]]
print(arr10[0:2,1:3])
#fancy indexing
arr11=np.zeros((10,10))
for i in range(arr11.shape[0]):
    arr11[i]=i
print(arr11[[0,4,5,3]])#fancy: we can get them in any order
'''Array Transposition'''
arr12=np.arange(50).reshape((10,5))
print(arr12)# 10rows,5 colms
print(arr12.T)#transpose matrix
print(np.dot(arr12.T,arr12))#dot product of arrays
'''universal Func in Array'''
arr13=np.arange(11)
print(arr13)
print(np.sqrt(arr13))
print(np.square(arr13))
A=np.random.randn(10)
print(A)
B=np.random.randn(10)
print(B)
#Binary Func(use 2 matrix)
print(np.add(A,B))
print(np.maximum(A,B))
'''Array processing'''
points=np.arange(-5,5,0.01)
dx,dy=np.meshgrid(points,points)
print(dx)
print('------------------')
print(dy)
print('------------------')
z=np.sin(dx)+np.sin(dy)
print(z)
print('------------------')
plt.imshow(z)
plt.colorbar()
plt.title('Plot for sin(x)+sin(y)')

M=np.array([1,2,3,4])
N=np.array([100,200,300,400])
condition=np.array([True,True,False,False])
#if conditiont true choose M else N
answer=[(M_val if cond else N_val)for M_val,N_val,cond in zip(M,N,condition)]
print(answer)
#where(condtion,true,false)
answer2=np.where(condition,M,N)
print(answer2)
#making a 5x5 normal distribution array
mk=np.random.randn(5,5)
print(mk)
mkp=mk<0
print(mkp)
print(np.where(mk<0,0,mk))
pp=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(pp)
print(pp.sum())
print('sum up columnwise')
print(pp.sum(0))
print(pp.mean())#avg
print(pp.std())#standard deviation
print(pp.var())#variance

bool_arr=np.array([True,False,True])
print(bool_arr.any())#returns true if any elem in arr is true
print(bool_arr.all())#return true if all elem in arr is true
#sort
arrp=np.random.randn(5)
print(arrp)
arrp.sort()
print('sorted ',arrp)
#unique
countries=np.array(['France','Germany','Russia','USA','Mexico','Germany'])
print(countries)
print(np.unique(countries))#unique set
#compare more than 1 elem
print(np.in1d(['France','Sweden'],countries))

#input output in array
kp=np.arange(5)
print(kp)
np.save('myarray',kp)#kp saved as myarray.npy
kp=np.arange(10)
print(kp)
print(np.load('myarray.npy'))
kp1=np.load('myarray.npy')
kp2=kp
np.savez('ziparray.npz',x=kp1,y=kp2)#to save multiple array
archive_array=np.load('ziparray.npz')
print(archive_array['x'])
print(archive_array['y'])

#save as txt not as array
arrp=np.array([[1,2,3],[4,5,6]])
np.savetxt('myTextArray.txt',arrp,delimiter=',')
#load txt file
arrq=np.loadtxt('myTextArray.txt',delimiter=',')
print(arrq)
