'''
Created on Oct 10, 2017

@author: erickhdez, bermudezarii, xbolanos, nicolmorice
'''


from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from WebServer.settings import MEDIA_ROOT
from controller import images_manager
from controller.images_manager import ImagesManager


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
    return render(request, 'html/index.html')


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
    if request.method != 'post':
        # No other method are allowed for this function than post.
        return render(request, 'html/index.html')

    result, images_paths = get_request_images(request)

    if not result:
        return render(request, 'html/index.html')

    im = ImagesManager()
    im.load_images(images_paths)

    return render(request, 'html/index.html')


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
