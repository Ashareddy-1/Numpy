#python vs numpy in terms of less memory

import sys
import numpy as np

#python size
l=range(1000)
size_in_python = sys.getsizeof(999)*len(l)
print(size_in_python)

#numpy size
array = np.arange(1000)
size_in_numpy = array.size*array.itemsize
print(size_in_numpy)     

