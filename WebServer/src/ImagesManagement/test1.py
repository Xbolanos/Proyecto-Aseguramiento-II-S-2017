import unittest
import numpy as np
from imagesmanager import ImagesManager
from ImagesManagement import imagesmanager
from numpy import newaxis

imagesm = ImagesManager()
#resulta q esa es la cara promedio
A = np.array([[1,2,5], [4,10,5], [3,5,5]])
#print("a looks like")
#print(A)
B = imagesm.averageFace(A)
#print("bueno la media es: ")
#print(B)
#print("la C es:")
C = imagesm.matrixOfDifferences(A, B) 
#print (C.transpose())
D= imagesm.calculateCovMatrixEv(C)
E = imagesm.calculateCovMatrixEw(C)
#print("la nueva cov")

#print(D)
#print("cov no eficiente")
#print(E)
#print("eigen")

#print(autovalores)
#print("wat")
#print(autovectores)

# a ver si es cierto 
















autovalores, autovectores = np.linalg.eig(np.matrix(D))
autovaloresw, autovectoresw = np.linalg.eig(np.matrix(E))
print("a")
print(np.matrix(D))
print("b")
print(np.matrix(autovectores))


print(np.matrix(D) * autovectores)

print("quak")

print(np.matrix(autovalores) * np.matrix(autovectores))

print("W")
W = np.matrix(C) * autovectores
print(W) 
print("NANI")
Wi = imagesm.calculateW(C)

print(Wi)
pro = imagesm.projectImages(C, Wi)
print("wao y ya")
print(pro)