'''
Created on Aug 12, 2017

@author: erickhdez, bermudezarii
'''

import cv2
import numpy as np 
from _cffi_backend import string
np.set_printoptions(threshold=np.nan)



# las imagenes estan ya en vector pero falta trasponerlas 
#como necesitamos las muestras en las columnas y no en las filas como esta
images = []
A = []
G = 0

def addImage(path):
    """
    @summary: This function reads the image 
    
    Parameters
    ----------
    @param path: is the address of the file that needs to be read  
    
    Returns
    ----------
    @return: the matrix of the image selected by the parameter path
    """

    return cv2.imread(path,0)

def calculateCovarianceMatrix(samples):
    """
    @summary: This function calculates the covariance matrix of a given matrix containing
    the samples of the same image; where every column represents a sample and every row
    represents the different values for the same pixel. 
    
    Parameters
    ----------
    @param samples: the matrix with all the samples of a given image. Which should have
    every sample as a column.
    
    Returns
    ----------
    @return: the covariance matrix for the samples matrix of the image.
    """
    
    return np.cov(samples)
     

def matrix2vector(matrix):        
    """
    @summary: This function transforms a matrix that comes from an image to a 
    vector ; every row goes consecutive in the vector, in the same order.
    
    Parameters
    ----------
    @param matrix: is the matrix of a given image. 
    
    Returns
    ----------
    @return: the same matrix in an array format
    """
    global G
    aimg = np.asarray(matrix).reshape(-1)
    np.savetxt(str(G), aimg)
    G = G + 1
    return aimg


def add2images(vector):
    """
    @summary: This function adds the vector that receives to a "general" array that will contain
    all the samples. 
    
    Parameters
    ----------
    @param vector: receives a vector (the image matrix transformed in a vector) 
    
    Returns
    ----------
    @return: void 
    """

    images.append(vector)

#le da vuelta a image, que ya volveria cada muestra en columna (: 
def transpose():
    """
    @summary: This function transforms the matrix of images, puts each row as a column
    because each sample is as a row, but for the matrix of covariance 
    
    Parameters
    ----------
    @param :  there are no parameters 
    
    Returns
    ----------
    @return: the matrix of images transposed 
    """

    return np.array(images).transpose()

#esto eventualmente cambiara para cuando tengamos lo web 
def process():
    """
    @summary: This function is like a main, puts together all the functions that 
    have to be called 
    
    Parameters
    ----------
    @param :  there are no parameters 
    
    Returns
    ----------
    @return: void
    """
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
    A = transpose() #aqui se crea la matriz de muestras
    print(A)
    print("Matriz de covarianza:\n")
    print(calculateCovarianceMatrix(A))


#---------------------------------------------------------------------
#plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
#plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
#plt.show()

process()


