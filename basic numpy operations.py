import numpy as np

b = np.array([5,6,9]) #1D array
a = np.array([[1,2],[3,4],[5,6]])#2D array

print(a.ndim)#prints the dimension of array a
print(b.ndim)#prints the dimension of array b
print(a.itemsize)#prints byte size of each of these elements
print(a.dtype)#prints the data type

a = np.array([[1,2],[3,4],[5,6]], dtype = np.float64)#converting to float datatype
print(a.dtype)#prints the data type
a = np.array([[1,2],[3,4],[5,6]], dtype = complex)#converting to complex datatype
print(a.dtype)#prints the data type
a = np.array([[1,2],[3,4],[5,6]], dtype = np.int32)#converting to int datatype
print(a.dtype)#prints the data type
print(a)
print(a.size)#prints total no.of elements
print(a.shape)#prints shape of array
print(a.reshape(2,3))
print(a.ravel())#flatten to 1D
z=np.zeros((3,4))#to get a array with all zeros of shape (3,4) i.e.; 3 rows and 4 columns
print(z)
o=np.ones((3,4))#to get a array with all ones of shape (3,4) i.e.; 3 rows and 4 columns
print(o)
range_from_1_to_4 = np.arange(1,5)#1 is included and 5 is excluded
print(range_from_1_to_4)
range_from_1_to_4_in_2_steps = np.arange(1,5,2)#1 is included and 5 is excluded and 2 steps
print(range_from_1_to_4_in_2_steps)
linearspaced = np.linspace(1,5,10)#this will generate 10 numbers b/w 1 &5 which are linearly spaced
print(linearspaced)
print(a.min())
print(a.max())
print(a.sum())
