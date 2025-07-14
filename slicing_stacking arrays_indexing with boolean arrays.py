import numpy as np
#slicing
a = np.array([6,7,8])
print(a[0:2])#slicing 0 is included and 2 is excluded
print(a[-1])#numpy supports reverse index also

a = np.array([[6,7,8], [1,2,3], [9,3,2]])#3 rows(0,1,2) and 3 columns(0,1,2) 3D array
print(a)
print(a[1,2])#1 row and 2 column element so 3 is o/p
print(a[0:2,2])#0:2 means 0,1 rows and 2 column so [8,3] is o/p
print(a[-1,0:2])#-1 row i.e; 2 row and 0,1 column so [9,3] is o/p
print(a[:,1:3])#all rows and 1 and 2 columns so [[7,8],[2,3],[3,2]]

#iteration
a = np.array([[6,7,8], [1,2,3], [9,3,2]])
for row in a:
    print(row)

for cell in a.flat:
    print(cell)#flatten the list and print every cell

#stacking together two array
a = np.arange(6).reshape(3,2)
b = np.arange(6,12).reshape(3,2)
print(a)
print(b)
print(np.vstack((a,b)))#to vertically stack a and b
print(np.hstack((a,b)))#to horizontally stack a and b


#splitting two array
a = np.arange(30).reshape(2,15)
print(a)
result = np.hsplit(a,3)#splits horizontally to 3 parts
print(result)
print(result[0])
print(result[1])
print(result[2])
result = np.vsplit(a,2)#splits vertically to 2 parts
print((result))

#Indexing with Boolean array
a = np.arange(12).reshape(3,4)
print(a)
b=a>4
print(b)
print(a[b])#prints only elements where b=a>4
a[b]=-1
print(a)
