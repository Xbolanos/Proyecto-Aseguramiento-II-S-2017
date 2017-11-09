'''
Created on Nov 3, 2017
@author: erickhdez, bermudezarii, xbolanos, nicolmorice
@version: version 1.0 beta
'''

from abc import ABC, abstractmethod
import numpy as np
from WebServer.settings import STATICFILES_DIRS
from networkx.classes.function import neighbors
from controller.ErrorHandler import ErrorHandler
np.set_printoptions(threshold=np.nan)


class FacesManager(ABC):
    """
    @summary: class for handling all the images processing as well as
    guiding the system through learning and recognition.

    Variables
    ---------
    @var images_paths: contains all the paths to the images currently being
    used in the system.
    @var images: contains the processed images matrix.
    @var path_saved: contains the path of saved stuff
    """
    def __init__(self):
        self.path_saved = STATICFILES_DIRS[0] + '/saved/'


    # le da vuelta a image, que ya volveria cada muestra en columna (:
    @staticmethod
    def transpose(images):
        """
        @summary: This function transforms the matrix of images, puts each row
        as a column because each sample is as a row, but for the matrix of
        covariance.

        Parameters
        ----------
        @param images: an array with the images transformed in a vector.

        Returns
        ----------
        @return: the matrix of images transposed.

        Reference: page 1 document: Eigen Faces.pdf
        """
        try:
            if images is not None:
                a = isinstance(images, list)
                if (a or isinstance(images, np.ndarray)):
                    return np.array(images).transpose()
                else:
                    s = "images of transpose doesn't correspond in type: list"
                    raise Exception(s)
            else:
                raise Exception("images of transpose is null")
        except Exception as msg:
            e = ErrorHandler()
            e.error(msg)

    @staticmethod
    def average_face(images):
        """
        @summary: This function calculates the mean from the
        columns of the matrix images which is the average face.

        Parameters
        ----------
        @param images: an array (matrix) with the images, each sample
        is a column.

        Returns
        ----------
        @return: the mean of the columns in a single column.

        Reference: page 2 document: Eigen Faces.pdf Step 3.
        """
        try:
            if images is not None:
                if (isinstance(images, list) or isinstance(images, np.ndarray)):
                    a = np.array(images)
                    b = np.mean(a, axis=1)[np.newaxis]
                    return b.T
                else:
                    raise Exception("images of avface is not list")
            else:
                raise Exception("images of avface is null")
        except Exception as msg:
            e = ErrorHandler()
            e.error(msg)

    @staticmethod
    def matrix_of_differences(images_n, av_face):
        """
        @summary: This function calculates the matrix of Differences, which
        is the each column of the images matrix minus the average face.

        Parameters
        ----------
        @para images_n: an array (matrix) with the images, each sample
        is a column.
        @param av_face: the mean between all the samples of the matrix
        images.

        Returns
        ----------
        @return: the matrix of difference.

        Reference: page 3 document: Eigen Faces.pdf Step 4.
        """
        try:
            if ((images_n is not None and av_face is not None)):
                a = isinstance(av_face, np.ndarray)
                if(isinstance(images_n, np.ndarray) and a):
                    return images_n - av_face
                else:
                    raise Exception("1+ param of matrix is not np.array")
            else:
                raise Exception("1+ param of matrix is null")
        except Exception as msg:
            e = ErrorHandler()
            e.error(msg)


    @staticmethod
    def calculate_cov_matrix_ev(m_dif):
        """
        @summary: This function calculates the covariance
        matrix multiplying the matrix of Differences with
        its transposed, this is the efficient covariance
        matrix.

        Parameters
        ----------
        @param m_dif: matrix of Differences.

        Returns
        ----------
        @return: the efficent covariance matrix.

        Reference: page 2 document: Eigen Faces.pdf Step 5.
        """
        try:
            if (m_dif is not None):
                if(isinstance(m_dif, np.ndarray)):
                    DT = np.matrix(np.transpose(m_dif))
                    D = np.matrix(m_dif)
                    return DT*D
                else:
                    raise Exception("mDif of ev has wrong type")
            else:
                raise Exception("mDif of ev is null")
        except Exception as msg:
            e = ErrorHandler()
            e.error(msg)

    @staticmethod
    def eigen_vectors_of_matrix(matrix, n):
        """
        @summary: This function calculates with the help of
        the library NUMPY, the eigen vectors from a matrix.

        Parameters
        ----------
        @param matrix: matrix which needs the eigen vectors.
        @param n: how many eigen vectors do you want to work with.

        Returns
        ----------
        @return: an array of eigen vectors.

        Reference: page 3 document: Eigen Faces.pdf Step 6.
        """
        try:
            if (matrix is not None and n is not None):
                if (isinstance(matrix, np.ndarray) and isinstance(n, int)): 
                    matrix_vectors = np.linalg.eigh(matrix)[1]
                    matrix_reduced = np.array(matrix_vectors)[:, 0:n]
                    return matrix_reduced
                else:
                    raise Exception("Matrix or n doesn't correspond in type")
            else:
                raise Exception("Matrix or n in eigvectors is NULL")
        except Exception as msg:
            e = ErrorHandler()
            e.error(msg)

    @staticmethod
    def calculate_w(m_dif, n):
        """
        @summary: This function calculates W that is the N-k eigenvectors.

        Parameters
        ----------
        @param m_dif: matrix of Differences
        @param n: how many eigen vectors do you want to work with

        Returns
        ----------
        @return: W = the N-k eigenvalues of the efficent matrix
        of covariance.
        Reference: page 5 document: Eigen Faces.pdf Step 2 (getting the w).
        """
        try:
            if (m_dif is not None and n is not None):
                if (isinstance(m_dif, np.ndarray) and isinstance(n, int)):
                    ev = FacesManager.calculate_cov_matrix_ev(m_dif)
                    eigen = FacesManager.eigen_vectors_of_matrix(ev, n)
                    w = np.dot(np.matrix(m_dif), eigen)
                    return w
                else:
                    raise Exception("mDif or n in w doesn't match")
            else:
                raise Exception("mDif or n in w is null")
        except Exception as msg:
            e = ErrorHandler()
            e.error(msg)


    @staticmethod
    def project_images(m_dif, w):
        """
        @summary: This function transforms the columns into a projected space.

        Parameters
        ----------
        @param m_dif: matrix of Differences.
        @param w: the matrix of difference multiplied eigen values.

        Returns
        ----------
        @return: a matrix of the matrix of difference projected.
        Reference: page 5 document: Eigen Faces.pdf Step 2.
        """
        try:
            if (m_dif is not None and w is not None):
                if(isinstance(m_dif, np.ndarray) and isinstance(w, np.ndarray)):
                    wt = np.transpose(np.matrix(w))
                    m_dif_projected = wt * np.matrix(m_dif)
                    return m_dif_projected
                else:
                    raise Exception("some params of project images doesn't match")
            else:
                raise Exception("some params of project images are null")
        except Exception as msg:
            e = ErrorHandler()
            e.error(msg)

    @staticmethod
    def classify_nearest_centroid(new_image, projected_images):
        """
        @summary: This function search the face of the new image.

        Parameters
        ----------
        @param new_image: the image that you need the face of, it has
        come processed.
        @param projected_images: the images of training already projected
        into the space.

        Returns
        ----------
        @return: the value that correspond to the person detected
        in the image.
        Reference: page 6 document: Eigen Faces.pdf Step 3.
        """
        try:
            if(new_image is not None and projected_images is not None):
                a1 = isinstance(new_image, np.ndarray)
                a2 = isinstance(projected_images, np.ndarray)
                if(a1 and a2):
                    a = projected_images-new_image
                    distance_norm = np.linalg.norm(a, axis=0)
                    n = np.argmin(distance_norm)
                    final = int(n/8)
                    return final + 1
                else:
                    raise Exception("some params of centroid doesn't match")
            else:
                raise Exception("some params of centroid are null")
        except Exception as msg:
            e = ErrorHandler()
            e.error(msg)

    @staticmethod
    def get_min(distance):
        """
        @summary: gets the minimun value of the array and sets the
        selected one into a big value so it doesn't take it anymore

        Parameters
        ----------
        @param distance: is the euclidean distance of each
        eigenvectors

        Returns
        ----------
        @return: return the index of the minimun and
        the new distance.
        """
        try:
            if(distance is not None):
                if(isinstance(distance, np.ndarray)):
                    n = np.argmin(distance)
                    final = int(n/8)
                    distance[n] = 50000000000
                    return final + 1, distance
                else:
                    raise Exception("distance of get_min doesn't match")
            else:
                raise Exception("distance of get_min is null")
        except Exception as msg:
            e = ErrorHandler()
            e.error(msg)

    @staticmethod
    def k_neighbors(k, new_image, projected_images):
        """
        @summary: This function search the face of the new image.

        Parameters
        ----------
        @param k: how many faces you want to get 
        @param new_image: the image that you need the face of, it has
        come processed.
        @param projected_images: the images of training already projected
        into the space.

        Returns
        ----------
        @return: the value that correspond to the person detected
        in the image.
        Reference: uses the principles of page 6 document:
        Eigen Faces.pdf Step 3.
        """
        try:
            if(k is not None and new_image is not None
               and projected_images is not None):
                if(isinstance(k, int) and isinstance(new_image, np.ndarray)
                   and isinstance(projected_images, np.ndarray)):
                    a = projected_images-new_image
                    distance_norm = np.linalg.norm(a, axis=0)
                    neighbors = []
                    for i in range(k):
                        neighbors.append(FacesManager.get_min(distance_norm)[0])
                        new_distance_norm = FacesManager.get_min(distance_norm)[1]
                        distance_norm = new_distance_norm
                    unique, counts = np.unique(neighbors, return_counts=True)
                    j = np.argmax(counts)
                    return unique[j]
                else:
                    raise Exception("some params of k-neighborhs")
            else:
                raise Exception("some params of k neighbors are null")
        except Exception as msg:
            e = ErrorHandler()
            e.error(msg)


    @abstractmethod
    def process(self, image_manager):
        """
        Abstract method, implement it in child classes.
        """
        pass
