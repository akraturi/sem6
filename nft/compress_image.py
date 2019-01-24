import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def blockshaped(arr, nrows, ncols):
    """
    Return an array of shape (n, nrows, ncols) where
    n * nrows * ncols = arr.size

    If arr is a 2D array, the returned array should look like n subblocks with
    each subblock preserving the "physical" layout of arr.
    """
    h, w = arr.shape
    return (arr.reshape(h//nrows, nrows, -1, ncols)
               .swapaxes(1,2)
               .reshape(-1, nrows, ncols))

img = cv.imread("charly_greyscale.jpg",cv.COLOR_BGR2GRAY)


print(img)
print(img.shape)
height,width = img.shape
print("Height:",height)
print("Widht:",width)
filter_height = height/2
filter_width = width/2
block=blockshaped(img,filter_height,filter_width)
#plt.imshow(block)
print(block)
print(block.shape)
#print(img.size/1024)
#print(img.dtype)


