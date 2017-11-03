'''
Created on Nov 3, 2017
@author: erickhdez, bermudezarii, xbolanos, nicolmorice
'''

from controller.faces_manager import FacesManager
import numpy as np


class Recognize(FacesManager):
    """
    Class to handle the recognition of subjects within the system.
    """
    def __init__(self):
        super(Recognize, self).__init__()

    def process(self, image_manager):
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
        subject = image_manager.images_matrix[0]
        av = self.path_saved+'AverageFace.out'
        av_face = np.loadtxt(av, delimiter=',')[np.newaxis]
        w = np.loadtxt(self.path_saved+'W.out', delimiter=',')
        all_p = self.path_saved+'projectedFaces.out'
        all_projected = np.loadtxt(all_p, delimiter=',')
        e_image = subject[np.newaxis]
        t_image = super(Recognize, Recognize).transpose(e_image)
        image = super(Recognize, Recognize).matrix_of_differences(t_image, 
                                                                  av_face.T)
        # Esto multiplica la imagen x por autovectores transpuestos 
        processed = super(Recognize, Recognize).project_images(image, w)
        result = super(Recognize, Recognize).classify_nearest_centroid(
                                                processed, all_projected)
        print("pls result ")
        print(result)
        return (result)