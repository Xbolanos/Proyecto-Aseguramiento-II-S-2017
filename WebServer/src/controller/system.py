'''
Created on Oct 10, 2017

@author: erickhdez, bermudezarii, xbolanos, nicolmorice
'''


from django.shortcuts import render
from WebServer.settings import STATICFILES_DIRS
from controller.images_manager import ImagesManager
from django.http.response import JsonResponse
from filestack import Filelink

IM = ImagesManager()
EIGEN_VECTORS = 300
IMAGES_PER_SUBJECT = 8


def show_index_page(request):
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
    return render(request, 'index.html')


def train_system(request):
    """
    @summary: look up for images in the request as well if it is a post
    request, in case this fails a the system will not be trained. Otherwise,
    the images are processed and used to train the system. The result of the
    function is always sent to the client.

    Parameters
    ----------
    @param request: the http request from the client.

    Returns
    -------
    @return: a success page if the processing and training went well. a failure
    page otherwise.
    """
    if request.method != 'POST':
        # No other method are allowed for this function than post.
        return JsonResponse({'type': 'error',
                             'title': 'Metodo invalido',
                             'message': 'No se permiten otros metodos además' +
                                        'de post.'})

    data = request.body.decode('UTF-8')
    data = eval(data)
    path = STATICFILES_DIRS[0]
    images_paths = []

    for handler in data['handlers']:
        filelink = Filelink(handler, apikey='AFWdiEhaQUP00SdiMZPugz')
        extension = filelink.get_metadata()['filename'][-4:]
        fullpath = path + '/subjects/' + handler + extension
        filelink.download(fullpath)
        images_paths.append(fullpath)

    IM.training(EIGEN_VECTORS, images_paths, IMAGES_PER_SUBJECT)

    return JsonResponse({'type': 'success',
                         'title': '¡Registrado!',
                         'message': 'Se ha agregado al nuevo sujeto al' +
                                    'sistema.'})
