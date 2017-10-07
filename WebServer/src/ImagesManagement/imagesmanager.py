'''
Created on Aug 12, 2017
@author: erickhdez, bermudezarii, xbolanos, nicolmorice
'''

import cv2
import numpy as np


class ImagesManager:

    images = []
    A = []
    G = 0

    def addImage(self, path):
        """
        @summary: This function reads the image

        Parameters
        ----------
        @param self: part of OOP syntax
        @param path: is the address of the file that needs to be read

        Returns
        ----------
        @return: the matrix of the image selected by the parameter path
        """

        return cv2.imread(path, 0)

    def calculateCovarianceMatrix(self, samples):
        """
        @summary: This function calculates the covariance matrix of a given
        matrix containing the samples of the same image; where every column
        represents a sample and every row represents the different values for
        the same pixel.

        Parameters
        ----------
        @param self: part of OOP syntax
        @param samples: the matrix with all the samples of a given image. Which
        should have every sample as a column.

        Returns
        ----------
        @return: the covariance matrix for the samples matrix of the image.
        """

        return np.cov(samples)

    def matrix2vector(self, matrix):
        """
        @summary: This function transforms a matrix that comes from an image to
        a vector; every row goes consecutive in the vector, in the same order.

        Parameters
        ----------
        @param self: part of OOP syntax
        @param matrix: is the matrix of a given image.

        Returns
        ----------
        @return: the same matrix in an array format
        """

        return np.asarray(matrix).reshape(-1)

    def add2images(self, vector):
        """
        @summary: This function adds the vector that receives to a "general"
        array that will contain all the samples.

        Parameters
        ----------
        @param self: part of OOP syntax
        vector: receives a vector (the image matrix transformed in a vector)

        Returns
        ----------
        @return: void
        """

        self.images.append(vector)

    

    # le da vuelta a image, que ya volveria cada muestra en columna (:
    def transpose(self, images):
        """
        @summary: This function transforms the matrix of images, puts each row
        as a column because each sample is as a row, but for the matrix of
        covariance

        Parameters
        ----------
        @param self: part of OOP syntax
        images: an array with the images transformed in a vector


        Returns
        ----------
        @return: the matrix of images transposed
        """
        print (np.array(images).transpose())
        return np.array(images).transpose()


    def averageFace(self, images):
        """
        @summary: This function calculates the mean from the columns of the matrix images
        which is the average face

        Parameters
        ----------
        @param self: part of OOP syntax
        images: an array (matrix) with the images, each sample 
        is a column

        Returns
        ----------
        @return: the mean of the columns 
        """
        a = np.array(images)
        b = np.mean(a, axis=1)[np.newaxis]
        return b.T
        
    def matrixOfDifferences(self, images, avface):
        """
        @summary: This function calculates the matrix
        of Differences, which is the each column of 
        the images matrix minus the average face 

        Parameters
        ----------
        @param self: part of OOP syntax
        images: an array (matrix) with the images, each sample 
        is a column
        avface: the mean between al the samples of the matrix
        images

        Returns
        ----------
        @return: the matrix of differences 
        """
        return images - avface
    
    def calculateNewCovMatrix(self, mDif):
        """
        @summary: This function calculates the covariance
        matrix multiplying the matrix of Differences with 
        its transposed 

        Parameters
        ----------
        @param self: part of OOP syntax
        mDif: matrix of Differences 
        
        Returns
        ----------
        @return: the covariance matrix
        """   
        return  mDif.transpose()  * mDif 
        
    # esto eventualmente cambiara para cuando tengamos lo web
    def process(self):
        """
        @summary: This function is like a main, puts together all the functions
        that have to be called

        Parameters
        ----------
        @param self: part of OOP syntax

        Returns
        ----------
        @return: void
        """

        print (cv2.__version__)
        self.add2images(self.matrix2vector(self.addImage('Muestras/s1/1.pgm')))
        self.add2images(self.matrix2vector(self.addImage('Muestras/s1/2.pgm')))
        self.add2images(self.matrix2vector(self.addImage('Muestras/s1/3.pgm')))
        self.add2images(self.matrix2vector(self.addImage('Muestras/s1/4.pgm')))
        self.add2images(self.matrix2vector(self.addImage('Muestras/s1/5.pgm')))
        self.add2images(self.matrix2vector(self.addImage('Muestras/s1/6.pgm')))
        self.add2images(self.matrix2vector(self.addImage('Muestras/s1/7.pgm')))
        self.add2images(self.matrix2vector(self.addImage('Muestras/s1/8.pgm')))
        self.add2images(self.matrix2vector(self.addImage('Muestras/s1/9.pgm')))
        A = self.transpose(self.images)  # aqui se crea la matriz de muestras
        print(A)
        print("Matriz de covarianza:\n")
        #print(self.calculateCovarianceMatrix(A))
        return A

    # ---------------------------------------------------------------------
    # plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
    # plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    # plt.show()


