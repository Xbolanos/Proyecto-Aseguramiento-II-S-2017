import unittest
import numpy as np
from imagesmanager import ImagesManager
from ImagesManagement import imagesmanager
from numpy import newaxis

imagesm = ImagesManager()
#resulta q esa es la cara promedio
A = np.array([[1,2], [4,10]])
print("a looks like")
print(A)
B = imagesm.averageFace(A)
print("bueno la media es: ")
print(B)
print("la D es:")
C = imagesm.matrixOfDifferences(A, B)[np.newaxis]
print (C)

print("la nueva cov")
print(imagesm.calculateNewCovMatrix(C))


