'''
Created on Aug 12, 2017
@author: erickhdez, bermudezarii, xbolanos, nicolmorice
'''

import cv2
import numpy as np
from WebServer.settings import STATICFILES_DIRS


class ImagesManager:
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

    images_paths = []
    images = []
    path_saved = STATICFILES_DIRS[0] + '/saved/'

    def read_image(self, path):
        """
        @summary: This function reads the image.

        Parameters
        ----------
        @param path: is the address of the file that needs to be read.

        Returns
        ----------
        @return: the matrix of the image selected by the parameter path.
        """

        return cv2.imread(path, 0)

    def calculate_covariance_matrix(self, samples):
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

    def matrix_2_vector(self, matrix):
        """
        @summary: This function transforms a matrix that comes from an image to
        a vector; every row goes consecutive in the vector, in the same order.

        Parameters
        ----------
        @param matrix: is the matrix of a given image.

        Returns
        ----------
        @return: the same matrix in an array format.
        """

        return np.asarray(matrix).reshape(-1)

    def add_2_images(self, vector):
        """
        @summary: This function adds the vector that receives to a "general"
        array that will contain all the samples.

        Parameters
        ----------
        @param vector: receives a vector (the image matrix transformed in a
        vector).

        Returns
        ----------
        @return: void.
        """

        self.images.append(vector)

    # le da vuelta a image, que ya volveria cada muestra en columna (:
    def transpose(self, images):
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

    def average_face(self, images):
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
        b = np.mean(a, axis=1)[np.newaxis]
        return b.T

    def matrix_of_differences(self, images_n, av_face):
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

    def calculate_cov_matrix_ev(self, m_dif):
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

    def eigen_vectors_of_matrix(self, matrix, n):
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

    def calculate_w(self, m_dif, n):
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
        ev = self.calculate_cov_matrix_ev(m_dif)
        eigen = self.eigen_vectors_of_matrix(ev, n)
        w = np.dot(np.matrix(m_dif), eigen)
        #matmul
        return w

    def project_images(self, m_dif, w):
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

    def classify_nearest_centroid(self, new_image, projected_images):
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

    def load_images(self):
        """
        @summary: loads all the images from the given parameter list and add
        them to the images list.

        Parameters
        ----------
        @param images_paths: a list containing all the paths of the images to
        be loaded.

        Returns
        -------
        @return: void.
        """
        del self.images[:]

        for path in self.images_paths:
            greys_image = self.read_image(path)
            column_vector = self.matrix_2_vector(greys_image)
            self.add_2_images(column_vector)

    def training(self, n_eigen_vectors, paths, n_training):
        """
        @summary: This function trains the system with faces
        calling different functions.

        Parameters
        ----------
        @param n_eigen_vectors: how many eigen vectors
        would you like to work with
        @param paths: a list of paths containing the address to the new images
        to be added to the system.
        @param n_training: number of faces/images per subject

        Returns
        -------
        @return: void.
        """

        self.images_paths.extend(paths)
        self.load_images()
        normalized = self.transpose(self.images)
        av_face = self.average_face(normalized)
        print("a")
        np.savetxt(self.path_saved+'AverageFace.out', av_face, delimiter=',')
        print("a")
        m_dif = self.matrix_of_differences(normalized, av_face)
        print(m_dif)
        w = self.calculate_w(m_dif, n_eigen_vectors)
        print(w)
        np.savetxt(self.path_saved+'W.out', w, delimiter=',')
        all_projected = self.project_images(m_dif, w)
        all_p = self.path_saved+'projectedFaces.out'
        np.savetxt(all_p, all_projected, delimiter=',')
        print(all_projected)
        n_train = np.matrix(n_training)
        np.savetxt(self.path_saved+'n_training.out', n_train)

    def recognize(self, path):
        """
        @summary: This function search the face of the new image.

        Parameters
        ----------
        @param path: address of the image.

        Returns
        ----------
        @return: the value that correspond to the person detected
        in the image.
        """
        av = self.path_saved+'AverageFace.out'
        av_face = np.loadtxt(av, delimiter=',')[np.newaxis]
        w = np.loadtxt(self.path_saved+'W.out', delimiter=',')
        all_p = self.path_saved+'projectedFaces.out'
        all_projected = np.loadtxt(all_p, delimiter=',')
        e_image = self.matrix_2_vector(self.read_image(path))[np.newaxis]
        t_image = self.transpose(e_image)
        image = self.matrix_of_differences(t_image, av_face.T)
        processed = self.project_images(image, w) #esto multiplica la imagen x por autovectores transpuestos 
        result = self.classify_nearest_centroid(processed, all_projected)
        print("pls result ")
        print(result)
        return (result)
