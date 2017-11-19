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

from controller.images_manager import ImagesManager
from controller.training_manager import Training
from controller.recognizing_manager import Recognize
from django.core.files.storage import FileSystemStorage
from WebServer.settings import MEDIA_ROOT
from django.core.files.uploadedfile import UploadedFile


im = ImagesManager()
im.loadLists()


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

    return True


def recognize_subject(subject, mode):
    """
        @summary: This function search the face of the new image.

        Parameters
        ----------
        @param subject: the image of the person

        Returns
        ----------
        @return: the name that correspond to the person detected
        in the image.
    """

    if subject is None:
        return ('error', 'No se ha proveido un sujeto.', '', '')

    if not isinstance(subject, UploadedFile):
        return ('error', 'Parametro incorrecto', 'Verifique el parametro e' +
                'intentelo de nuevo.', '')

    fs = FileSystemStorage(location=MEDIA_ROOT)

    fileName = fs.save(subject.name, subject)
    fileUrl = fs.location + '/' + fileName
    path = [fileUrl]

    tempIM = ImagesManager()
    tempIM.add_images_paths(path)
    tempIM.load_images()

    rm = Recognize()
    index = rm.process(tempIM, mode)
    result = im.get_subject_name(index - 1)

    return ('success', '¡Se ha reconocido!', 'El rostro pertenece al sujeto ',
            str(result))


def signin(user):
    """
        @summary: This function helps to log in.

        Parameters
        ----------
        @param user: the person who tries to log in.

        Returns
        ----------
        @return: a boolean indicating if is correct 
        or not.
    """
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

def logout():
    return True