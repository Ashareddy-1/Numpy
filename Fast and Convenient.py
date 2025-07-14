#python vs numpy in terms of fast and convenient

import time
import numpy as np

#python
size=10000000000
l1 = range(size)
l2 = range(size)

start = time.time()
result = [(x+y) for x,y in zip(l1,l2)]
print('python list took:',(time.time()-start)*1000)

#numpy size
a1 = np.arange(size)
a2 = np.arange(size)

start = time.time()
result = a1+a2
print('numpy took:',(time.time()-start)*1000)
