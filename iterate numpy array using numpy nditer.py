import numpy as np
a = np.arange(12).reshape(3,4)
print(a)

for x in np.nditer(a,order='c'):#for c order iteration
    print(x)

for x in np.nditer(a,order='F'):#for Fortan order iteration
    print(x)

for x in np.nditer(a,order='F', flags = ['external_loop']):#want to go in fortan order and print entire column at a time
    print(x)

for x in np.nditer(a,op_flags=['readwrite']):
                   print(x[...]==x*x)
