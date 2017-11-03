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
'''


from WebServer.settings import STATICFILES_DIRS
from controller.images_manager import ImagesManager
from django.http.response import JsonResponse
from filestack import Filelink

IM = ImagesManager()
EIGEN_VECTORS = 1000
IMAGES_PER_SUBJECT = 8


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


def train_system(data):
    """
    @summary: gets the images handlers and use the FileStack API to download
    them into the local file system to use them into the training of the
    system.

    Parameters
    ----------
    @param data: the data from the client's http request.

    Returns
    -------
    @return: a json response containing the type, title and message fields to
    describe what happen within the server.
    """
    path = STATICFILES_DIRS[0]  # The static path for de subjects images.
    images_paths = []

    for handler in data['handlers']:
        # Creates a new object to connect to FileStack with the given API.
        filelink = Filelink(handler, apikey='AFWdiEhaQUP00SdiMZPugz')
        extension = filelink.get_metadata()['filename'][-4:]
        fullpath = path + '/subjects/' + handler + extension
        filelink.download(fullpath)
        images_paths.append(fullpath)

    IM.training(EIGEN_VECTORS, images_paths, IMAGES_PER_SUBJECT)

    return {'type': 'success',
            'title': '¡Registrado!',
            'message': 'Se ha agregado al nuevo sujeto al sistema.'}
