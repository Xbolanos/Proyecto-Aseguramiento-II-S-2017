'''
Created on Aug 12, 2017
@author: erickhdez, bermudezarii, xbolanos, nicolmorice
'''

import cv2 as cv
import numpy as np


class ImagesManager(object):
    """
    Class to handle the images to be used in the system.
    """

    def __init__(self):
        self.images_paths = []
        self.images_matrix = []

    def add_images_paths(self, paths):
        """
        Adds a lists of paths to the already known paths of the class.

        Parameters
        ----------
        paths: the list of paths to be added.

        Returns
        -------
        Nothing is returned.
        """
        self.images_paths.extend(paths)

    @staticmethod
    def read_image(path):
        """
        This function reads an image in gray scale.

        Parameters
        ----------
        path: is the address of the file that will be read.

        Returns
        ----------
        The image as a matrix of values between 0 and 255.
        """
        return cv.imread(path, 0)

    @staticmethod
    def matrix_to_vector(matrix):
        """
        This function transforms a image matrix that to a vector
        image; every row goes consecutive in the vector, in the same order.

        Parameters
        ----------
        matrix: is the matrix of a given image.

        Returns
        ----------
        The matrix transformed as a vector.
        """
        return np.asarray(matrix).reshape(-1)

    def add_to_images(self, vector):
        """
        This function adds the vector that receives to a "general" array that
        will contain all the samples.

        Parameters
        ----------
        vector: the image like vector to be added to the matrix of images.

        Return
        ------
        Nothing is returned.
        """
        self.images_matrix.append(vector)

    def load_images(self):
        """
        Loads all the images from the images_paths static attribute and add
        them to the images_matrix attibute.

        Parameters
        ----------
        There are no parameters

        Returns
        -------
        Nothing is returned.
        """
        del self.images_matrix[:]

        for path in self.images_paths:
            greys_image = ImagesManager.read_image(path)
            column_vector = ImagesManager.matrix_to_vector(greys_image)
            self.add_to_images(column_vector)
