'''
Created on Nov 3, 2017
@author: erickhdez, bermudezarii, xbolanos, nicolmorice
'''

from controller.faces_manager import FacesManager
from controller.images_manager import ImagesManager
import numpy as np


class Training(FacesManager):
    """
    Class incharge of training the system with the subjects faces.
    """
    EIGEN_VECTORS = 1000
    IMAGES_PER_SUBJECT = 8

    def __init__(self):
        super(Training, self).__init__()

    def process(self, image_manager):
        """
        @summary: This function trains the system with faces
        calling different functions.

        Parameters
        ----------
        @param EIGEN_VECTORS: how many eigen vectors
        would you like to work with
        @param paths: a list of paths containing the address to the new images
        to be added to the system.
        @param IMAGES_PER_SUBJECT: number of faces/images per subject

        Returns
        -------
        @return: void.
        """
        images_matrix = image_manager.images_matrix
        normalized = super(Training, Training).transpose(images_matrix)
        av_face = super(Training, Training).average_face(normalized)
        print("a")
        np.savetxt(self.path_saved+'AverageFace.out', av_face, delimiter=',')
        print("a")
        m_dif = super(Training, Training).matrix_of_differences(normalized, 
                                                                av_face)
        print(m_dif)
        w = super(Training, Training).calculate_w(m_dif, 
                                                  Training.EIGEN_VECTORS)
        print(w)
        np.savetxt(self.path_saved+'W.out', w, delimiter=',')
        all_projected = super(Training, Training).project_images(m_dif, w)
        all_p = self.path_saved+'projectedFaces.out'
        np.savetxt(all_p, all_projected, delimiter=',')
        print(all_projected)
        n_train = np.matrix(Training.IMAGES_PER_SUBJECT)
        np.savetxt(self.path_saved+'IMAGES_PER_SUBJECT.out', n_train)
