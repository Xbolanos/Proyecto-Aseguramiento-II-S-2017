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
        "Muestras/s10/10.pgm",
        "Muestras/s11/1.pgm",
        "Muestras/s11/2.pgm", 
        "Muestras/s11/3.pgm",
        "Muestras/s11/4.pgm",
        "Muestras/s11/5.pgm",
        "Muestras/s11/6.pgm",
        "Muestras/s11/7.pgm",
        "Muestras/s11/8.pgm",
        "Muestras/s11/9.pgm",
        "Muestras/s11/10.pgm", 
        "Muestras/s12/1.pgm",
        "Muestras/s12/2.pgm", 
        "Muestras/s12/3.pgm",
        "Muestras/s12/4.pgm",
        "Muestras/s12/5.pgm",
        "Muestras/s12/6.pgm",
        "Muestras/s12/7.pgm",
        "Muestras/s12/8.pgm",
        "Muestras/s12/9.pgm",
        "Muestras/s12/10.pgm", 
        "Muestras/s13/1.pgm",
        "Muestras/s13/2.pgm", 
        "Muestras/s13/3.pgm",
        "Muestras/s13/4.pgm",
        "Muestras/s13/5.pgm",
        "Muestras/s13/6.pgm",
        "Muestras/s13/7.pgm",
        "Muestras/s13/8.pgm",
        "Muestras/s13/9.pgm",
        "Muestras/s13/10.pgm",
        "Muestras/s14/1.pgm",
        "Muestras/s14/2.pgm", 
        "Muestras/s14/3.pgm",
        "Muestras/s14/4.pgm",
        "Muestras/s14/5.pgm",
        "Muestras/s14/6.pgm",
        "Muestras/s14/7.pgm",
        "Muestras/s14/8.pgm",
        "Muestras/s14/9.pgm",
        "Muestras/s14/10.pgm",
        "Muestras/s15/1.pgm",
        "Muestras/s15/2.pgm", 
        "Muestras/s15/3.pgm",
        "Muestras/s15/4.pgm",
        "Muestras/s15/5.pgm",
        "Muestras/s15/6.pgm",
        "Muestras/s15/7.pgm",
        "Muestras/s15/8.pgm",
        "Muestras/s15/9.pgm",
        "Muestras/s15/10.pgm",
        "Muestras/s16/1.pgm",
        "Muestras/s16/2.pgm", 
        "Muestras/s16/3.pgm",
        "Muestras/s16/4.pgm",
        "Muestras/s16/5.pgm",
        "Muestras/s16/6.pgm",
        "Muestras/s16/7.pgm",
        "Muestras/s16/8.pgm",
        "Muestras/s16/9.pgm",
        "Muestras/s16/10.pgm",
        "Muestras/s17/1.pgm",
        "Muestras/s17/2.pgm", 
        "Muestras/s17/3.pgm",
        "Muestras/s17/4.pgm",
        "Muestras/s17/5.pgm",
        "Muestras/s17/6.pgm",
        "Muestras/s17/7.pgm",
        "Muestras/s17/8.pgm",
        "Muestras/s17/9.pgm",
        "Muestras/s17/10.pgm", 
        "Muestras/s18/1.pgm",
        "Muestras/s18/2.pgm", 
        "Muestras/s18/3.pgm",
        "Muestras/s18/4.pgm",
        "Muestras/s18/5.pgm",
        "Muestras/s18/6.pgm",
        "Muestras/s18/7.pgm",
        "Muestras/s18/8.pgm",
        "Muestras/s18/9.pgm",
        "Muestras/s18/10.pgm",
        "Muestras/s19/1.pgm",
        "Muestras/s19/2.pgm", 
        "Muestras/s19/3.pgm",
        "Muestras/s19/4.pgm",
        "Muestras/s19/5.pgm",
        "Muestras/s19/6.pgm",
        "Muestras/s19/7.pgm",
        "Muestras/s19/8.pgm",
        "Muestras/s19/9.pgm",
        "Muestras/s19/10.pgm", 
        "Muestras/s20/1.pgm",
        "Muestras/s20/2.pgm", 
        "Muestras/s20/3.pgm",
        "Muestras/s20/4.pgm",
        "Muestras/s20/5.pgm",
        "Muestras/s20/6.pgm",
        "Muestras/s20/7.pgm",
        "Muestras/s20/8.pgm",
        "Muestras/s20/9.pgm",
        "Muestras/s20/10.pgm",
        "Muestras/s21/1.pgm",
        "Muestras/s21/2.pgm", 
        "Muestras/s21/3.pgm",
        "Muestras/s21/4.pgm",
        "Muestras/s21/5.pgm",
        "Muestras/s21/6.pgm",
        "Muestras/s21/7.pgm",
        "Muestras/s21/8.pgm",
        "Muestras/s21/9.pgm",
        "Muestras/s21/10.pgm", 
        "Muestras/s22/1.pgm",
        "Muestras/s22/2.pgm", 
        "Muestras/s22/3.pgm",
        "Muestras/s22/4.pgm",
        "Muestras/s22/5.pgm",
        "Muestras/s22/6.pgm",
        "Muestras/s22/7.pgm",
        "Muestras/s22/8.pgm",
        "Muestras/s22/9.pgm",
        "Muestras/s22/10.pgm", 
        "Muestras/s23/1.pgm",
        "Muestras/s23/2.pgm", 
        "Muestras/s23/3.pgm",
        "Muestras/s23/4.pgm",
        "Muestras/s23/5.pgm",
        "Muestras/s23/6.pgm",
        "Muestras/s23/7.pgm",
        "Muestras/s23/8.pgm",
        "Muestras/s23/9.pgm",
        "Muestras/s23/10.pgm",
        "Muestras/s24/1.pgm",
        "Muestras/s24/2.pgm", 
        "Muestras/s24/3.pgm",
        "Muestras/s24/4.pgm",
        "Muestras/s24/5.pgm",
        "Muestras/s24/6.pgm",
        "Muestras/s24/7.pgm",
        "Muestras/s24/8.pgm",
        "Muestras/s24/9.pgm",
        "Muestras/s24/10.pgm",
        "Muestras/s25/1.pgm",
        "Muestras/s25/2.pgm", 
        "Muestras/s25/3.pgm",
        "Muestras/s25/4.pgm",
        "Muestras/s25/5.pgm",
        "Muestras/s25/6.pgm",
        "Muestras/s25/7.pgm",
        "Muestras/s25/8.pgm",
        "Muestras/s25/9.pgm",
        "Muestras/s25/10.pgm",
        "Muestras/s26/1.pgm",
        "Muestras/s26/2.pgm", 
        "Muestras/s26/3.pgm",
        "Muestras/s26/4.pgm",
        "Muestras/s26/5.pgm",
        "Muestras/s26/6.pgm",
        "Muestras/s26/7.pgm",
        "Muestras/s26/8.pgm",
        "Muestras/s26/9.pgm",
        "Muestras/s26/10.pgm",
        "Muestras/s27/1.pgm",
        "Muestras/s27/2.pgm", 
        "Muestras/s27/3.pgm",
        "Muestras/s27/4.pgm",
        "Muestras/s27/5.pgm",
        "Muestras/s27/6.pgm",
        "Muestras/s27/7.pgm",
        "Muestras/s27/8.pgm",
        "Muestras/s27/9.pgm",
        "Muestras/s27/10.pgm", 
        "Muestras/s28/1.pgm",
        "Muestras/s28/2.pgm", 
        "Muestras/s28/3.pgm",
        "Muestras/s28/4.pgm",
        "Muestras/s28/5.pgm",
        "Muestras/s28/6.pgm",
        "Muestras/s28/7.pgm",
        "Muestras/s28/8.pgm",
        "Muestras/s28/9.pgm",
        "Muestras/s28/10.pgm",
        "Muestras/s29/1.pgm",
        "Muestras/s29/2.pgm", 
        "Muestras/s29/3.pgm",
        "Muestras/s29/4.pgm",
        "Muestras/s29/5.pgm",
        "Muestras/s29/6.pgm",
        "Muestras/s29/7.pgm",
        "Muestras/s29/8.pgm",
        "Muestras/s29/9.pgm",
        "Muestras/s29/10.pgm", 
        "Muestras/s30/1.pgm",
        "Muestras/s30/2.pgm", 
        "Muestras/s30/3.pgm",
        "Muestras/s30/4.pgm",
        "Muestras/s30/5.pgm",
        "Muestras/s30/6.pgm",
        "Muestras/s30/7.pgm",
        "Muestras/s30/8.pgm",
        "Muestras/s30/9.pgm",
        "Muestras/s30/10.pgm",
        "Muestras/s31/1.pgm",
        "Muestras/s31/2.pgm", 
        "Muestras/s31/3.pgm",
        "Muestras/s31/4.pgm",
        "Muestras/s31/5.pgm",
        "Muestras/s31/6.pgm",
        "Muestras/s31/7.pgm",
        "Muestras/s31/8.pgm",
        "Muestras/s31/9.pgm",
        "Muestras/s31/10.pgm", 
        "Muestras/s32/1.pgm",
        "Muestras/s32/2.pgm", 
        "Muestras/s32/3.pgm",
        "Muestras/s32/4.pgm",
        "Muestras/s32/5.pgm",
        "Muestras/s32/6.pgm",
        "Muestras/s32/7.pgm",
        "Muestras/s32/8.pgm",
        "Muestras/s32/9.pgm",
        "Muestras/s32/10.pgm", 
        "Muestras/s33/1.pgm",
        "Muestras/s33/2.pgm", 
        "Muestras/s33/3.pgm",
        "Muestras/s33/4.pgm",
        "Muestras/s33/5.pgm",
        "Muestras/s33/6.pgm",
        "Muestras/s33/7.pgm",
        "Muestras/s33/8.pgm",
        "Muestras/s33/9.pgm",
        "Muestras/s33/10.pgm",
        "Muestras/s34/1.pgm",
        "Muestras/s34/2.pgm", 
        "Muestras/s34/3.pgm",
        "Muestras/s34/4.pgm",
        "Muestras/s34/5.pgm",
        "Muestras/s34/6.pgm",
        "Muestras/s34/7.pgm",
        "Muestras/s34/8.pgm",
        "Muestras/s34/9.pgm",
        "Muestras/s34/10.pgm",
        "Muestras/s35/1.pgm",
        "Muestras/s35/2.pgm", 
        "Muestras/s35/3.pgm",
        "Muestras/s35/4.pgm",
        "Muestras/s35/5.pgm",
        "Muestras/s35/6.pgm",
        "Muestras/s35/7.pgm",
        "Muestras/s35/8.pgm",
        "Muestras/s35/9.pgm",
        "Muestras/s35/10.pgm",
        "Muestras/s36/1.pgm",
        "Muestras/s36/2.pgm", 
        "Muestras/s36/3.pgm",
        "Muestras/s36/4.pgm",
        "Muestras/s36/5.pgm",
        "Muestras/s36/6.pgm",
        "Muestras/s36/7.pgm",
        "Muestras/s36/8.pgm",
        "Muestras/s36/9.pgm",
        "Muestras/s36/10.pgm",
        "Muestras/s37/1.pgm",
        "Muestras/s37/2.pgm", 
        "Muestras/s37/3.pgm",
        "Muestras/s37/4.pgm",
        "Muestras/s37/5.pgm",
        "Muestras/s37/6.pgm",
        "Muestras/s37/7.pgm",
        "Muestras/s37/8.pgm",
        "Muestras/s37/9.pgm",
        "Muestras/s37/10.pgm", 
        "Muestras/s38/1.pgm",
        "Muestras/s38/2.pgm", 
        "Muestras/s38/3.pgm",
        "Muestras/s38/4.pgm",
        "Muestras/s38/5.pgm",
        "Muestras/s38/6.pgm",
        "Muestras/s38/7.pgm",
        "Muestras/s38/8.pgm",
        "Muestras/s38/9.pgm",
        "Muestras/s38/10.pgm",
        "Muestras/s39/1.pgm",
        "Muestras/s39/2.pgm", 
        "Muestras/s39/3.pgm",
        "Muestras/s39/4.pgm",
        "Muestras/s39/5.pgm",
        "Muestras/s39/6.pgm",
        "Muestras/s39/7.pgm",
        "Muestras/s39/8.pgm",
        "Muestras/s39/9.pgm",
        "Muestras/s39/10.pgm", 
        "Muestras/s40/1.pgm",
        "Muestras/s40/2.pgm", 
        "Muestras/s40/3.pgm",
        "Muestras/s40/4.pgm",
        "Muestras/s40/5.pgm",
        "Muestras/s40/6.pgm",
        "Muestras/s40/7.pgm",
        "Muestras/s40/8.pgm",
        "Muestras/s40/9.pgm",
        "Muestras/s40/10.pgm",
        "Muestras/s41/1.pgm",
        "Muestras/s41/2.pgm", 
        "Muestras/s41/3.pgm",
        "Muestras/s41/4.pgm",
        "Muestras/s41/5.pgm",
        "Muestras/s41/6.pgm",
        "Muestras/s41/7.pgm",
        "Muestras/s41/8.pgm",
        "Muestras/s41/9.pgm",
        "Muestras/s41/10.pgm", 
    ]



#resulta q esa es la cara promedio
for path in path_list:    
            imagesm.add2images(imagesm.matrix2vector(imagesm.addImage(path)))
normalized =  imagesm.transpose(imagesm.images)

#print(imagesm.images)

AverageFace = imagesm.averageFace(normalized)

lista = np.array(imagesm.images)

mDif = imagesm.matrixOfDifferences(normalized, AverageFace)


Ev = imagesm.calculateCovMatrixEv(mDif)

i = imagesm.eigenVectorsofMatrix(Ev)

W = imagesm.calculateW(mDif)

allProjected = imagesm.projectImages(mDif, W)
print("print all projected")
print(allProjected)
print("okay all projected")
timage =  imagesm.transpose(imagesm.matrix2vector(imagesm.addImage(path_list[8])))[np.newaxis]
print("timage")
print(timage)
image = imagesm.matrixOfDifferences(timage.T, AverageFace) 
print("the image in 1 col ")
print(image)
print("okay -3")
processed = imagesm.projectImages(image, W)
print("okay")
result = imagesm.classifyNearestCentroid(processed, W, allProjected)
print("pls result ")
print(result)