import numpy as np
a = np.array([[1,2],[3,4],[5,6]])#2D array
print(a.sum(axis=0))#columns sum as axis=0 means columns
print(a.sum(axis=1))#columns sum as axis=1 means rows
print(np.sqrt(a))#prints sqrt of each each element in the array
print(np.std(a))#prints standard deviation of array

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
print(a.dot(b))#print dot product of a and b
