'''
Created on Oct 10, 2017

@author: erickhdez, bermudezarii, xbolanos, nicolmorice
'''


from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from WebServer.settings import MEDIA_ROOT
from WebServer.settings import STATICFILES_DIRS
from controller import images_manager
from controller.images_manager import ImagesManager
from django.http.response import JsonResponse
from filestack import Filelink


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
                             'message': 'No se permiten otros metodos además \
de post.'})

    handlers = request.body.decode('UTF-8')
    handlers = eval(handlers)
    path = STATICFILES_DIRS[0]
    images_paths = []

    for handle in handlers:
        filelink = Filelink(handle, apikey='ABeQAmZTIQ8ygf76s90Bnz')
        extension = filelink.get_metadata()['filename'][-4:]
        fullpath = path + '/subjects/' + handle + extension
        filelink.download(fullpath)
        images_paths.append(fullpath)

    im = ImagesManager()
    im.load_images(images_paths)
    return JsonResponse({'type': 'success',
                         'title': '¡Registrado!',
                         'message': 'Se ha agregado al nuevo sujeto al \
sistema.'})


def get_request_images(request):
    """
    @summary: extracts only the image like files from the given uploaded set.

    Parameters
    ----------
    @param request: the http request from the client.

    Returns
    -------
    @return: True and a filled list if valid images were found, False and an
    empty list otherwise.
    """
    files = request.FILES.getlist('files')
    images_paths = []

    for file in files:
        if(is_image(file)):
            images_paths += save_image(file)

    if len(images_paths) == 0:
        return False, []

    return True, images_paths


def is_image(file):
    """
    @summary: checks if a given file is a valid image format for the system.

    Parameters
    ----------
    @param file: the file to be tested.

    Returns
    -------
    @return: true if the file is a valid image., false otherwise.
    """
    extensions = ('.jpg', '.jpeg', '.png', '.pgm')

    return file.name.endswith(extensions)


def save_image(image):
    """
    @summary: saves a image into the static folder of the project, for later
    use.

    Parameters
    ----------
    @param image: the image file to be saved.

    Returns
    -------
    @return: the full path of the saved image.
    """
    fs = FileSystemStorage()
    file_name = fs.save(image.name, image)
    file_path = MEDIA_ROOT + '/' + file_name

    return file_path
