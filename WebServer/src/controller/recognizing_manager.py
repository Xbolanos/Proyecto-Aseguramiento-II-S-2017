'''
Created on Nov 3, 2017
@author: erickhdez, bermudezarii, xbolanos, nicolmorice
@version: version 1.0 beta
'''

from controller.faces_manager import FacesManager
import numpy as np
from controller.images_manager import ImagesManager
from controller.ErrorHandler import ErrorHandler


class Recognize(FacesManager):
    """
    Class to handle the recognition of subjects within the system.
    """
    def __init__(self):
        super(Recognize, self).__init__()

    def process(self, image_manager, mode=0):
        """
        @summary: This function search the face of the new image.

        Parameters
        ----------
        @param

        Returns
        ----------
        @return: the value that correspond to the person detected
        in the image.
        """
        try:
            if image_manager is not None and mode is not None:
                if isinstance(image_manager, ImagesManager) and isinstance(mode, int):
                    subject = image_manager.images_matrix[0]
                    av = self.path_saved+'AverageFace.out'
                    av_face = np.loadtxt(av, delimiter=',')[np.newaxis]
                    w = np.loadtxt(self.path_saved+'W.out', delimiter=',')
                    all_p = self.path_saved+'projectedFaces.out'
                    all_projected = np.loadtxt(all_p, delimiter=',')
                    e_image = subject[np.newaxis]
                    t_image = super(Recognize, Recognize).transpose(e_image)
                    image = super(Recognize, Recognize).matrix_of_differences(
                        t_image, av_face.T)
                    processed = super(Recognize, Recognize).project_images(
                        image, w)
                    result = 0
                    if mode == 0:
                        result = super(Recognize,
                                       Recognize).classify_nearest_centroid(
                                       processed, all_projected)
                    elif mode == 1:
                        result = super(Recognize,
                                       Recognize).k_neighbors(
                                       3, processed, all_projected)
                    print(result)
                    return result
                else:
                    raise Exception("rProcess: some params type doesn't match")
            else:
                raise Exception("rProcess: some params are null")
        except Exception as msg:
            e = ErrorHandler()
            e.error(msg)
