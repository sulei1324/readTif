__author__ = 'Su Lei'

import cv2 as cv
import numpy as np
import tifffile

a = cv.imread('Stack.tif', -1)
b = np.array([1, 2, 3])
print a.dtype, a.shape

c = tifffile.imread('Stack3.tif')
print c.dtype, c.shape
tifffile.imsave('223.tif', c)