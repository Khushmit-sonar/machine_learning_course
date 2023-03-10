

##numpy: its most commonly used libraries for data science
## it is mostly used by scientific computing and data analysis
# basic numpy object :- ndarray

import numpy as np

##array in numpy its just like a list but in numpy its array
np.array([1,5,7,8])

a= np.array([1,2,3,4])
print(a)
print(a.shape)

##nd array (multidimention array)
b= np.array([[1,2,3],[4,5,6]])
print(b)

print("### To check the dimention of array")

print(b.shape)

print("### To check which type of elements are presen in array we use -> dtype")
print(b.dtype)


print("## to check total number of rows present in array")
print(b.ndim)

## if we want value for 0 to -- then we use arange fun
c = np.arange(50)
print(c)

# Commented out IPython magic to ensure Python compatibility.
##to check how much time an operation is taking to execute in python

c_pyton = range(1000)
# %timeit [i ** 3 for i in c_pyton]

# Commented out IPython magic to ensure Python compatibility.
##to check how much time an operation is taking to execute in python
c_numpy = np.arange(1000)

# %timeit c_numpy**3

print("## to print from what to what")## for eg u want element in ur array from 2 to 12

m = np.arange(2,12)
print(m)


print("## print element in arrar from to what with some interval")
## for eg u want element from 2 to 12 but they should have an interval of 2 in them

n = np.arange(2,12,2)
print(n)

## if u want a nd array which contain only zeros in it

np.zeros([3,2])##three rows and 2 col

## if u want a nd array which contain only ones in it

np.ones([3,4])##3 rows and  4 col

###we can create identity matrix
## in identity matrix all the diagnals will 1 and all values will be 0

np.eye(3)

## to fill value in matrix 

np.full((3,3),4)## we are filling 4 in 3 by 3 matrix

x=np.full((3,3),4.4 )
print(x)

print("##but we don't want floating value we want int values ")
y = np.full((3,3),4.4 ,dtype= np.int)
print(y)

##if u want diagonals of your choice

a = np.diag([1,5,9,6])
print(a)

## if i want to tile the matrix
## like for example i have 123 of array and i want to make it as ([1,2,3],[1,2,3],[1,2,3])

v =np.array([1,2,3])


print(np.tile(v,(3,1)))
print(np.tile(v,(3,2)))

## random value in numpy

50*np.random.random() +2

## when we want a random value of matrix

np.random.random([3,3])

##linspace mean for eg we want value from 1 to 50 but it should be distributed equally
##In 100 sub parts
a = np.linspace(1,50,100)
print(a)

print("## how to identify how much memory is used by this operation in term of bites")
print(a.itemsize)

b = np.arange(18).reshape(2,3,3)
print(b)

a = np.array([2,5,8,3,5,8,6,4])
print(a[0])
print(a[3])
print(a[[2,3,4]])##retriving multiple elements from array
print(a[2:])## when we want element from 2 index
print(a[2:5])## when we want element from 2 index to 5
print(a[0::2])## get element from 0 to end with 2 interval init

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
##if we want 9 from it
print(a[2,2])

#we want value which is grater than 2 from this array
print(a>2)
b =a[(a>2)&(a<5)]
print(b)

a = np.arange(10)
print(a)
b = a

print(b)

b[0]=14 ## if we are changing b,, a arrary will also change because the both are 
## same memory location
print(b)
print(a)

np.shares_memory(a,b)## to check if the memory location is some or not

## but when we want to change the second array so we will need make a copy 
## 

a = np.arange(10)
print(a)
b = a.copy()## now we had created a seprated object 
b[0]=14
print(a)
print(b)
np.shares_memory(a,b)

##matrix transform
a= np.array([[1,2,3],[4,5,6]])
print(a)## before transform
print("-----------------------------------")
print(a.T)## after transform

b= np.array([[11,41,13],[4,5,6]])
print("-----------------------------------")
#if we want to compare two arrays
print(a == b)

print("-----------------------------------")
## if we want to stack element virtacally
print(np.vstack((a,b)))

print("-----------------------------------")
## if we want to stack element horizentaly
print(np.hstack((a,b)))

a =np.arange(1,10)

print(np.sin(a))##if we want the sin of each element
print("-----------------------------------")
print(np.cos(a))##if we want the cos of each element
print("-----------------------------------")
print("exponintial",np.exp(a))## if we want the exponential of each element
print("-----------------------------------")
print("sum",np.sum(a))## sum of all element in the array
print("-----------------------------------")
print("median",np.median(a))
print("-----------------------------------")
print("mean",np.mean(a))
print("-----------------------------------")
print("standard deviation",a.std())

a = np.arange(1,10).reshape(3,3)
a

print("-----------------------------------")
print("to find the diterminant", np.linalg.det(a))

a = np.arange(1,10).reshape(3,3)
b = a.T
print(a)
print("-----------------------------------")
print(b)

print("-----------------------------------")
# dot product
print(np.dot(a,b))

##logical operation on array
a = np.array([1,1,0] ,dtype = bool)
b = np.array([1,0,1], dtype = bool)
print(np.logical_or(a,b))
print("-----------------------------------")
print(np.logical_and(a,b))
print("-----------------------------------")
print(np.all( a == a))
