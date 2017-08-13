import numpy as np 
import cv2
from matplotlib import pyplot as plt


# las imagenes estan ya en vector pero falta trasponerlas 
#como necesitamos las muestras en las columnas y no en las filas como esta
images = []
A = []

def addImage(path):
    return cv2.imread(path,0)

def calculateCovarianceMatrix(samples):
    """
    @summary: This function calculates de covariance matrix of a given matrix of samples of the same image.
    
    Parameters
    ----------
    @param samples: the matrix with all the samples of a given image.
    
    Returns
    ----------
    @return: the covariance matrix for the samples matrix of the image.
    """
    
    return np.cov(samples)
     
#sacamos el vector de la imagen
def matrix2vector(matrix):        
    return np.asarray(matrix).reshape(-1)

#vamos a meter cada vector en image, image es casi la matriz
# A que vimos en clase, que tiene todas las muestras
def add2images(vector):
    images.append(vector)

#le da vuelta a image, que ya volveria cada muestra en columna (: 
def analysis():
    return np.array(images).transpose()

#esto eventualmente cambiara para cuando tengamos lo web 
def process():
    print (cv2.__version__)
    add2images(matrix2vector(addImage('Muestras/s1/1.pgm')))
    add2images(matrix2vector(addImage('Muestras/s1/2.pgm')))
    add2images(matrix2vector(addImage('Muestras/s1/3.pgm')))
    add2images(matrix2vector(addImage('Muestras/s1/4.pgm')))
    add2images(matrix2vector(addImage('Muestras/s1/5.pgm')))
    add2images(matrix2vector(addImage('Muestras/s1/6.pgm')))
    add2images(matrix2vector(addImage('Muestras/s1/7.pgm')))
    add2images(matrix2vector(addImage('Muestras/s1/8.pgm')))
    add2images(matrix2vector(addImage('Muestras/s1/9.pgm')))
    add2images(matrix2vector(addImage('Muestras/s1/10.pgm')))
    A = analysis() #aqui se crea la matriz de muestras
    print(A)
    print("Matriz de covarianza:\n")
    calculateCovarianceMatrix(A)

print(np.cov(np.array([1, 2, 3])))
process()







#---------------------------------------------------------------------
#plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
#plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
#plt.show()






