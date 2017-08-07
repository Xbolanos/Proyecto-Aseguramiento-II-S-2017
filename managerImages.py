import numpy as np 
import cv2
from matplotlib import pyplot as plt
print cv2.__version__
img = cv2.imread('1.jpg',0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()