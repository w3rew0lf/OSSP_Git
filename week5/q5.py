import sys
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import numpy as np
n =1000
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)
plt.scatter(X,Y)
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
