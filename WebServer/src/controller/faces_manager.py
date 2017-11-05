'''
Created on Nov 3, 2017
@author: erickhdez, bermudezarii, xbolanos, nicolmorice
'''

from abc import ABC, abstractmethod
import numpy as np
from WebServer.settings import STATICFILES_DIRS
from networkx.classes.function import neighbors
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

    @staticmethod
    def calculate_covariance_matrix(samples):
        """
        @summary: This function calculates the covariance matrix of a given
        matrix containing the samples of the same image; where every column
        represents a sample and every row represents the different values for
        the same pixel.

        Parameters
        ----------
        @param samples: the matrix with all the samples of a given image. Which
        should have every sample as a column.

        Returns
        ----------
        @return: the covariance matrix for the samples matrix of the image.
        """
        return np.cov(samples)

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
        """
        return np.array(images).transpose()

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
        """
        a = np.array(images)
        print("a es: " + str(a))
        b = np.mean(a, axis=1)[np.newaxis]
        return b.T

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
        """
        return images_n - av_face

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
        """
        DT = np.matrix(np.transpose(m_dif))
        D = np.matrix(m_dif)
        return DT*D

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
        """
        matrix_vectors = np.linalg.eigh(matrix)[1]
        matrix_reduced = np.array(matrix_vectors)[:, 0:n]
        return matrix_reduced

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
        """
        ev = FacesManager.calculate_cov_matrix_ev(m_dif)
        eigen = FacesManager.eigen_vectors_of_matrix(ev, n)
        w = np.dot(np.matrix(m_dif), eigen)
        return w

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
        """
        wt = np.transpose(np.matrix(w))
        m_dif_projected = wt * np.matrix(m_dif)
        return m_dif_projected

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
        """
        a = projected_images-new_image
        distance_norm = np.linalg.norm(a, axis=0)
        n = np.argmin(distance_norm)
        final = int(n/8)
        print("resultado " + str(final))
        return final + 1

    @staticmethod
    def getMin(distance):
        n = np.argmin(distance)
        print("disntace: " + str(distance))
        final = int(n/8)
        print("tama;o; " + str(np.size(distance)))
        distance[n] = 50000000000
        print("cambio: " + str(distance[n]))
        return final + 1, distance

    @staticmethod
    def k_neighbors(k, new_image, projected_images):
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
        """
        a = projected_images-new_image
        distance_norm = np.linalg.norm(a, axis=0)
        neighbors = []
        for i in range(k): 
            #//consigue el numero del sujetoy lo agrega
            #tambien devuelve el nuevo distance norm 
            neighbors.append(FacesManager.getMin(distance_norm)[0])
            new_distance_norm = FacesManager.getMin(distance_norm)[1]
            distance_norm = new_distance_norm
        unique, counts = np.unique(neighbors, return_counts=True)
        print("unique: " + str(unique)) 
        print("counts: " + str(counts))
        j = np.argmax(counts)
        print(neighbors)
        return unique[j]



    @abstractmethod
    def process(self, image_manager):
        """
        Abstract method, implement it in child classes.
        """
        pass
