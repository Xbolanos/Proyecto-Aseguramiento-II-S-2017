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
from controller.recognizing_manager import Recognize
from filestack import Filelink
from django.core.files.storage import FileSystemStorage
from WebServer.settings import MEDIA_ROOT


im = ImagesManager()


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


def train_system(files, filesData, autovectors, images_per_subject):
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
    fs = FileSystemStorage(location=MEDIA_ROOT)
    basePath = fs.location
    paths = []
    subjects_names = []
    for key in files.keys():
        file = files[key]
        fileData = filesData[key + 'data']
        if fileData not in subjects_names:
            subjects_names.append(fileData)

        fs.location = basePath + '/' + fileData

        fileName = fs.save(file.name, file)
        fileUrl = fs.location + '/' + fileName
        paths.append(fileUrl)

    im.add_images_paths(paths, subjects_names)
    im.load_images()

    training = Training()
    training.process(im, autovectors, images_per_subject)

    return {'type': 'success',
            'title': '¡Registrado!',
            'message': 'Se ha(n) registrado con exito al sistema.'}


def recognize_subject(handler):
    path = STATICFILES_DIRS[0]  # The static path for de subjects images.

    # Creates a new object to connect to FileStack with the given API.
    filelink = Filelink(handler, apikey='AhZpdzSRTdW9nhvd946LAz')
    extension = filelink.get_metadata()['filename'][-4:]
    fullpath = path + '/subjects/' + handler + extension
    filelink.download(fullpath)

    tempIM = ImagesManager()
    tempIM.add_images_paths([fullpath])
    tempIM.load_images()

    rm = Recognize()
    index = rm.process(tempIM, mode=1)
    result = im.get_subject_name(index - 1)
    return {'type': 'success',
            'title': 'Se ha reconocido al sujeto',
            'message': 'El rostro pertenece al sujeto: ' + str(result)}


def signin(user):
    admin = {
        'email': 'admin@reconoceme.com',
        'password': '123Queso'
    }

    if(user['email'] == admin['email']):
        if(user['password'] == user['password']):
            return True
        else:
            False
    else:
        False
