from __future__ import print_function
import cv2 as cv
import numpy as np
import sys

args = sys.argv[1]
image = cv.imread(str(arg))

if image is None:
    print('Could not open or find the image: ', args.input)
    exit(0)

contrastControl = float(input('* Enter Contrast modifier value (Typically 1.0-3.0): '))
brightnessControl = int(input('* Enter Brightness modifier value (Typically 0-100): '))

output = cv.addWeighted(image,contrastControl, np.zeros(image.shape, image.dtype), 0, brightnessControl)

# Alternate Method: Apply Multiplier and Translation to all Pixels g(i,j)=(contrast control)⋅f(i,j)+(brightness control):
# i = 1
# for y in range(image.shape[0]):
#    for x in range(image.shape[1]):
#        for c in range(image.shape[2]):
#            output[y,x,c] = np.clip(contrastControl*image[y,x,c] + brightnessControl, 0, 255) 
#            print('iteration: '+str(i))
#            i = i + 1

cv.imshow('Original Image', image)
cv.imshow('New Image', output)

cv.waitKey();

