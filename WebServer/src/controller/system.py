'''
Created on Oct 10, 2017

@summary: the main controller of the system, will handle request, control the
image processing module and responding to the clients.

Variables
---------
@var IM: instance of the ImagesManager class.
@var EIGEN_VECTORS: The quantity of eigen vectors to be used in the training.
@var IMAGES_PER_SUBJECT: The quantity of images to be used by subject in the
training.

@author: erickhdez, bermudezarii, xbolanos, nicolmorice
@version: version 1.0 beta
'''

from WebServer.settings import STATICFILES_DIRS
from controller.images_manager import ImagesManager
from controller.training_manager import Training
from filestack import Filelink


def get_index_page():
    """
    @summary: a basic function to retrieve the home page of the website and
    returns it to the client.

    Parameters
    ----------
    @param request: the http request from the client.

    Return
    ------
    @return: the home page of the web site.
    """
    return 'index.html'


def train_system(paths):
    """
    @summary: gets the images handlers and use the FileStack API to download
    them into the local file system to use them into the training of the
    system.

    Parameters
    ----------
    @param paths: the paths of the new added images.

    Returns
    -------
    @return: a json response containing the type, title and message fields to
    describe what happen within the server.
    """

    im = ImagesManager()
    im.add_images_paths(paths)
    im.load_images()

    training = Training()
    training.process(im)

    return {'type': 'success',
            'title': '¡Registrado!',
            'message': 'Se ha agregado al nuevo sujeto al sistema.'}
