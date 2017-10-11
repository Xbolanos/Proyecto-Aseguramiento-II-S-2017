'''
Created on Aug 12, 2017

@author: erickhdez, bermudezarii, xbolanos, nicolmorice
'''

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import controller.images_manager as im
from WebServer.settings import MEDIA_ROOT
from controller import facade


def show_index_page(request):
    """
    @summary: forwards the request into the inner components to process it and
    determine the correct response.

    Parameters
    ----------
    @param request: the http request from the client.

    Return
    ------
    @return: the facade response.
    """
    return facade.show_index_page(request)


def learn(request):
    """
    @summary: forwards the request into the inner components to process it and
    determine the correct response.

    Parameters
    ----------
    @param request: the http request from the client.

    Return
    ------
    @return: the facade response.
    """
    if request.method == 'POST':
        # In case is a post request this method will handle the request.
        return proccess_files(request)

    # Otherwise the response is the same page.
    return render(request, 'html/inicio.html')


def proccess_files(request):
    """
    @summary: This function is in charge of get all files that was sending in
    the front end.

    Parameters
    ----------
    @param request: the original request from the front end.

    Returns
    ----------
    @return: HttpResponse
    """
    files = request.FILES.getlist('files')
    fs = FileSystemStorage()
    imageManager = im.ImagesManager()

    if(len(files) == 0):
        # No files to process, start page is shown.
        return render(request, 'html/inicio.html')

    for file in files:
        filename = fs.save(file.name, file)
        filepath = MEDIA_ROOT + '/' + filename
        matrix = imageManager.addImage(filepath)

        return render(request, 'html/result.html', {'matrix': matrix})
