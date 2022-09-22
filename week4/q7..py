import numpy as np
arr1 = np.arange(1,10).reshape(3,3)
arr2 = np.arange(10,19).reshape(3,3)
arr1
arr2

np.concatenate((arr1,arr2),axis=1)