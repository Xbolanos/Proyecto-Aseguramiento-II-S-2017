import unittest
import numpy as np
from controller.images_manager import ImagesManager


class Test(unittest.TestCase):
    samplesTranposed = [
        np.loadtxt("Pruebas/MuestrtasTranspuestas/little_test"),
        np.loadtxt("Pruebas/MuestrtasTranspuestas/s1"),
        np.loadtxt("Pruebas/MuestrtasTranspuestas/s2"),
        np.loadtxt("Pruebas/MuestrtasTranspuestas/s3"),
        np.loadtxt("Pruebas/MuestrtasTranspuestas/s4"),
        np.loadtxt("Pruebas/MuestrtasTranspuestas/s5"),
        np.loadtxt("Pruebas/MuestrtasTranspuestas/s6"),
        np.loadtxt("Pruebas/MuestrtasTranspuestas/s7"),
        np.loadtxt("Pruebas/MuestrtasTranspuestas/s8"),
        np.loadtxt("Pruebas/MuestrtasTranspuestas/s9"),
        np.loadtxt("Pruebas/MuestrtasTranspuestas/s10")
    ]
    expected_av_faces = [
        np.loadtxt("Pruebas/Average Faces/little_test"),
        np.loadtxt("Pruebas/Average Faces/s1"),
        np.loadtxt("Pruebas/Average Faces/s2"),
        np.loadtxt("Pruebas/Average Faces/s3"),
        np.loadtxt("Pruebas/Average Faces/s4"),
        np.loadtxt("Pruebas/Average Faces/s5"),
        np.loadtxt("Pruebas/Average Faces/s6"),
        np.loadtxt("Pruebas/Average Faces/s7"),
        np.loadtxt("Pruebas/Average Faces/s8"),
        np.loadtxt("Pruebas/Average Faces/s9"),
        np.loadtxt("Pruebas/Average Faces/s10")
    ]
    expected_mat_dif = [
        np.loadtxt("Pruebas/Matrix of dif/little_test"),
        np.loadtxt("Pruebas/Matrix of dif/s1"),
        np.loadtxt("Pruebas/Matrix of dif/s2"),
        np.loadtxt("Pruebas/Matrix of dif/s3"),
        np.loadtxt("Pruebas/Matrix of dif/s4"),
        np.loadtxt("Pruebas/Matrix of dif/s5"),
        np.loadtxt("Pruebas/Matrix of dif/s6"),
        np.loadtxt("Pruebas/Matrix of dif/s7"),
        np.loadtxt("Pruebas/Matrix of dif/s8"),
        np.loadtxt("Pruebas/Matrix of dif/s9"),
        np.loadtxt("Pruebas/Matrix of dif/s10")
    ]
    expected_Ev = [
        np.loadtxt("Pruebas/Ev/little_test"),
        np.loadtxt("Pruebas/Ev/s1"),
        np.loadtxt("Pruebas/Ev/s2"),
        np.loadtxt("Pruebas/Ev/s3"),
        np.loadtxt("Pruebas/Ev/s4"),
        np.loadtxt("Pruebas/Ev/s5"),
        np.loadtxt("Pruebas/Ev/s6"),
        np.loadtxt("Pruebas/Ev/s7"),
        np.loadtxt("Pruebas/Ev/s8"),
        np.loadtxt("Pruebas/Ev/s9"),
        np.loadtxt("Pruebas/Ev/s10")
    ]

    expected_eigen_vectors = [
        np.loadtxt("Pruebas/Eigen vectors/little_test"),
        np.loadtxt("Pruebas/Eigen vectors/s1"),
        np.loadtxt("Pruebas/Eigen vectors/s2"),
        np.loadtxt("Pruebas/Eigen vectors/s3"),
        np.loadtxt("Pruebas/Eigen vectors/s4"),
        np.loadtxt("Pruebas/Eigen vectors/s5"),
        np.loadtxt("Pruebas/Eigen vectors/s6"),
        np.loadtxt("Pruebas/Eigen vectors/s7"),
        np.loadtxt("Pruebas/Eigen vectors/s8"),
        np.loadtxt("Pruebas/Eigen vectors/s9"),
        np.loadtxt("Pruebas/Eigen vectors/s10")
    ]

    def test_average_face(self):
        G = 0
        imagesm = ImagesManager()
        for matrix in self.samplesTranposed:
            result = ImagesManager.average_face(imagesm, matrix)
            result = result.astype('float')
            expected = self.expected_av_faces[G]
            err = "Mismatch of average faces"
            self.assertEqual(result.all(), expected.all(), err)
            print("Average Face unittest:" + str(G))
            G = G + 1

    def test_mat_of_difference(self):
        G = 0
        imagesm = ImagesManager()
        sizeSamples = len(self.samplesTranposed)
        while(G < sizeSamples):
            av_face = self.expected_av_faces[G][np.newaxis]
            matrix = self.samplesTranposed[G]
            result = imagesm.matrix_of_differences(matrix, av_face.T)
            result = result.astype('float')
            expected = self.expected_mat_dif[G]
            err = "Mismatch of matrix of difference"
            self.assertEqual(result.all(), expected.all(), err)
            print("Matrix of dif. unittest:" + str(G))
            G = G + 1

    def test_Ev(self):
        G = 0
        imagesm = ImagesManager()
        for matrix in self.expected_mat_dif:
            result = imagesm.calculate_cov_matrix_ev(matrix)
            result = result.astype('float')
            expected = self.expected_Ev[G]
            err = "Mismatch of Ev"
            self.assertEqual(result.all(), expected.all(), err)
            print("Ev unittest:" + str(G))
            G = G + 1

    def test_eigen_vectors(self):
        G = 0
        imagesm = ImagesManager()
        for matrix in self.expected_Ev:
            result = imagesm.eigen_vectors_of_matrix(matrix, 200)
            result = result.astype('float')
            expected = self.expected_eigen_vectors[G]
            err = "Mismatch of matrix of eigen vectors"
            self.assertEqual(result.all(), expected.all(), err)
            print("Eigen vectors unittest:" + str(G))
            G = G + 1
