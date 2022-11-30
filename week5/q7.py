import sys
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import numpy as np
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S, P, Q = np.tan(X), 1/(np.tan(X)), 1/(np.cos(X)), 1/(np.sin(X))
plt.plot(X, C)
plt.plot(X, S)
plt.plot(X, P)
plt.plot(X, Q)
plt.show()
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
