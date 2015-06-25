__author__ = 'Su Lei'

import numpy as np


a = np.array([[[0, 1], [3, 4]], [[7, 8], [6, 7]]])
b = np.array([[[6, 7], [4, 5]], [[5, 4], [1, 2]]])
c = np.concatenate((a, b), axis=1)
print a[0, 0]
print c[1, 0]
print c