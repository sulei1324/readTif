__author__ = 'Su Lei'

from libtiff import TIFF
import cv2 as cv
import numpy
import libtiff
import tifffile
import tiffany
import PIL

tif = tifffile.imread('3.tif')
print tif
t = cv.imread('3.tif', cv.CV_LOAD_IMAGE_UNCHANGED)
print t

