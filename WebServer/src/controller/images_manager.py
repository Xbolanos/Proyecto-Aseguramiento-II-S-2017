'''
Created on Aug 12, 2017
@author: erickhdez, bermudezarii, xbolanos, nicolmorice
@version: version 1.0 beta
'''

import cv2 as cv
import numpy as np
from controller.ErrorHandler import ErrorHandler
from WebServer.settings import STATICFILES_DIRS


class ImagesManager(object):
    """
    Class to handle the images to be used in the system.
    """

    def __init__(self):
        self.images_paths = []
        self.subjects_names = []
        self.images_matrix = []
        self.path_saved = STATICFILES_DIRS[0] + '/saved/'

    def add_images_paths(self, paths, subjects_names=None):
        """
        @sumary: Adds a lists of paths to the already known paths of the class.

        Parameters
        ----------
        @param: paths: the list of paths to be added.

        Returns
        -------
        Nothing is returned.
        """
        if(paths is not None):
            if(isinstance(paths, list)):
                self.images_paths = np.append(self.images_paths, paths)

                if(subjects_names is not None):
                    self.subjects_names = np.append(self.subjects_names,
                                                    subjects_names)
                    self.orderLists()
                    self.saveLists()
                print(self.images_paths)
                print(self.subjects_names)
            else:
                raise Exception("add images: paths type doesn't match")
        else:
            raise Exception("add images: paths type is null")
        
    def orderLists(self):
        """
        @sumary: Takes paths and the subjects and sort them 

        Parameters
        ----------
        @param: none

        Returns
        -------
        @return: none
        """
        np.sort(self.images_paths)
        np.sort(self.subjects_names)
        
    def saveLists(self):
        """
        @sumary: Takes paths and the subjects and saves them in 
        text files 

        Parameters
        ----------
        @param: none

        Returns
        -------
        @return: none
        """
        np.savetxt(self.path_saved + 'imagespaths.data', self.images_paths, delimiter=',', fmt="%s")
        np.savetxt(self.path_saved + 'subjectsnames.data', self.subjects_names, delimiter=',', fmt="%s")
        
    def loadLists(self):
        """
        @sumary: Takes text files from paths and the subjects and
        loads them to the system  

        Parameters
        ----------
        @param: none

        Returns
        -------
        @return: none
        """
        try:
            self.images_paths = np.loadtxt(self.path_saved + 'imagespaths.data', delimiter=',', dtype='str')
            self.subjects_names = np.loadtxt(self.path_saved + 'subjectsnames.data', delimiter=',', dtype='str')
        except Exception:
            pass
        
        
    def get_subject_name(self, index):
        """
        @sumary: this function with a index gets the name 
        of the subject because its sorted in the list of 
        names  

        Parameters
        ----------
        @param: index: the position of the list 

        Returns
        -------
        @return: returns the subject name
        """
        return self.subjects_names.item(index)

    @staticmethod
    def read_image(path):
        """
        @summary: This function reads an image in gray scale.

        Parameters
        ----------
        @param:  path: is the address of the file that will be read.

        Returns
        ----------
        @return: The image as a matrix of values between 0 and 255.
        """
        if(path is not None):
            if(isinstance(path, str)):
                return cv.imread(path, 0)
            else:
                raise Exception("read images: path type doesn't match")
        else:
            raise Exception("read images: path type is null")

    @staticmethod
    def matrix_to_vector(matrix):
        """
        @summary: This function transforms a image matrix that to a vector
        image; every row goes consecutive in the vector, in the same order.

        Parameters
        ----------
        @param: matrix: is the matrix of a given image.

        Returns
        ----------
        @return: The matrix transformed as a vector.
        """
        if(matrix is not None):
            if(isinstance(matrix, list) or isinstance(matrix, np.ndarray)):
                return np.asarray(matrix).reshape(-1)
            else:
                raise Exception("mtx2vct: matrix type doesn't match")
        else:
            raise Exception("mtx2vct: matrix type is null")

    def add_to_images(self, vector):
        """
        @sumary: This function adds the vector that receives to a "general" array that
        will contain all the samples.

        Parameters
        ----------
        @param: vector: the image like vector to be added to the matrix of images.

        Return
        ------
        @return: Nothing is returned.
        """
        if(vector is not None):
            if(isinstance(vector, list) or isinstance(vector, np.ndarray)):
                self.images_matrix.append(vector)
            else:
                raise Exception("add2img: vector type doesn't match")
        else:
            raise Exception("add2img: vector type is null")

    def load_images(self):
        """
        @sumary: Loads all the images from the images_paths static attribute and add
        them to the images_matrix attibute.

        Parameters
        ----------
        @param: There are no parameters

        Returns
        -------
        @return: Nothing is returned.
        """
        del self.images_matrix[:]

        for path in self.images_paths:
            greys_image = ImagesManager.read_image(path)
            column_vector = ImagesManager.matrix_to_vector(greys_image)
            self.add_to_images(column_vector)
