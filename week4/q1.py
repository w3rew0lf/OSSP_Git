import numpy as np
print(np.version.version)

a = input().split(" ")
print(a)
b = np.array(a)
unique, counts = np.unique(b, return_counts=True)
print(np.asarray((unique, counts)).T)
