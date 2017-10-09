import unittest
import numpy as np
from imagesmanager import ImagesManager
from ImagesManagement import imagesmanager
from numpy import newaxis

imagesm = ImagesManager()

path_list = [
        "Muestras/s1/1.pgm",
        "Muestras/s1/2.pgm", 
        "Muestras/s1/3.pgm",
        "Muestras/s1/4.pgm",
        "Muestras/s1/5.pgm",
        "Muestras/s1/6.pgm",
        "Muestras/s1/7.pgm",
        "Muestras/s1/8.pgm",
        "Muestras/s1/9.pgm",
        "Muestras/s1/10.pgm",
        "Muestras/s2/1.pgm",
        "Muestras/s2/2.pgm", 
        "Muestras/s2/3.pgm",
        "Muestras/s2/4.pgm",
        "Muestras/s2/5.pgm",
        "Muestras/s2/6.pgm",
        "Muestras/s2/7.pgm",
        "Muestras/s2/8.pgm",
        "Muestras/s2/9.pgm",
        "Muestras/s2/10.pgm", 
        "Muestras/s3/1.pgm",
        "Muestras/s3/2.pgm", 
        "Muestras/s3/3.pgm",
        "Muestras/s3/4.pgm",
        "Muestras/s3/5.pgm",
        "Muestras/s3/6.pgm",
        "Muestras/s3/7.pgm",
        "Muestras/s3/8.pgm",
        "Muestras/s3/9.pgm",
        "Muestras/s3/10.pgm", 
        "Muestras/s4/1.pgm",
        "Muestras/s4/2.pgm", 
        "Muestras/s4/3.pgm",
        "Muestras/s4/4.pgm",
        "Muestras/s4/5.pgm",
        "Muestras/s4/6.pgm",
        "Muestras/s4/7.pgm",
        "Muestras/s4/8.pgm",
        "Muestras/s4/9.pgm",
        "Muestras/s4/10.pgm",
        "Muestras/s5/1.pgm",
        "Muestras/s5/2.pgm", 
        "Muestras/s5/3.pgm",
        "Muestras/s5/4.pgm",
        "Muestras/s5/5.pgm",
        "Muestras/s5/6.pgm",
        "Muestras/s5/7.pgm",
        "Muestras/s5/8.pgm",
        "Muestras/s5/9.pgm",
        "Muestras/s5/10.pgm",
        "Muestras/s6/1.pgm",
        "Muestras/s6/2.pgm", 
        "Muestras/s6/3.pgm",
        "Muestras/s6/4.pgm",
        "Muestras/s6/5.pgm",
        "Muestras/s6/6.pgm",
        "Muestras/s6/7.pgm",
        "Muestras/s6/8.pgm",
        "Muestras/s6/9.pgm",
        "Muestras/s6/10.pgm",
        "Muestras/s7/1.pgm",
        "Muestras/s7/2.pgm", 
        "Muestras/s7/3.pgm",
        "Muestras/s7/4.pgm",
        "Muestras/s7/5.pgm",
        "Muestras/s7/6.pgm",
        "Muestras/s7/7.pgm",
        "Muestras/s7/8.pgm",
        "Muestras/s7/9.pgm",
        "Muestras/s7/10.pgm", 
        "Muestras/s8/1.pgm",
        "Muestras/s8/2.pgm", 
        "Muestras/s8/3.pgm",
        "Muestras/s8/4.pgm",
        "Muestras/s8/5.pgm",
        "Muestras/s8/6.pgm",
        "Muestras/s8/7.pgm",
        "Muestras/s8/8.pgm",
        "Muestras/s8/9.pgm",
        "Muestras/s8/10.pgm",
        "Muestras/s9/1.pgm",
        "Muestras/s9/2.pgm", 
        "Muestras/s9/3.pgm",
        "Muestras/s9/4.pgm",
        "Muestras/s9/5.pgm",
        "Muestras/s9/6.pgm",
        "Muestras/s9/7.pgm",
        "Muestras/s9/8.pgm",
        "Muestras/s9/9.pgm",
        "Muestras/s9/10.pgm", 
        "Muestras/s10/1.pgm",
        "Muestras/s10/2.pgm", 
        "Muestras/s10/3.pgm",
        "Muestras/s10/4.pgm",
        "Muestras/s10/5.pgm",
        "Muestras/s10/6.pgm",
        "Muestras/s10/7.pgm",
        "Muestras/s10/8.pgm",
        "Muestras/s10/9.pgm",
        "Muestras/s10/10.pgm"
    ]
#resulta q esa es la cara promedio
for path in path_list:    
            imagesm.add2images(imagesm.matrix2vector(imagesm.addImage(path)))
normalized =  imagesm.transpose(imagesm.images)
#print(imagesm.images)

AverageFace = imagesm.averageFace(normalized)
print("average face")
print(AverageFace)
lista = np.array(imagesm.images)
print(lista.shape[0])
print(lista.shape[1])
print(AverageFace.shape[0])
print(AverageFace.shape[1])
mDif = imagesm.matrixOfDifferences(normalized, AverageFace)
print("mDiff")
print(mDif)
Ev = imagesm.calculateCovMatrixEv(mDif)
print("EV y EW")
print(Ev)
W = imagesm.calculateW(mDif)
print("entonces W")
print(W)
allProjected = imagesm.projectImages(mDif, W)
print("print all projected")
print(allProjected)
print("okay -2")
image =  imagesm.matrixOfDifferences(imagesm.transpose(imagesm.matrix2vector(imagesm.addImage(path_list[98]))), AverageFace)
print("okay -3")
processed = imagesm.projectImages(image, W)
print("okay")
result = imagesm.classifyNearestCentroid(processed, W, allProjected)
print("pls result ")
print(result)