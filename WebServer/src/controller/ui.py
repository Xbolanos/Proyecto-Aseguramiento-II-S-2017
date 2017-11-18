'''
Created on Aug 12, 2017

@author: erickhdez, bermudezarii, xbolanos, nicolmorice
@version: version 1.0 beta
'''

from controller import facade
from django.shortcuts import render
from django.http import JsonResponse


def show_index_page(request):
    """
    @summary: forwards the request into the inner components to process it and
    determine the correct response.

    Parameters
    ----------
    @param request: the http request from the client.

    Return
    ------
    @return: the system's response to the request.
    """
    page = facade.get_index_page()
    return render(request, page)


def learn(request):
    """
    @summary: forwards the request into the inner components to process it and
    determine the correct response.

    Parameters
    ----------
    @param request: the http request from the client.

    Return
    ------
    @return: the system's response to the request.
    """
    if request.method != 'POST':
        # No other method are allowed for this function than post.
        return JsonResponse({'type': 'error',
                             'title': 'Metodo invalido',
                             'message': 'No se permiten otros metodos además' +
                                        'de post.'})

    files = request.FILES
    filesData = request.POST
    autovectors = int(filesData['autovectors'])
    images_per_subject = int(filesData['imagesPerSubject'])

    response = facade.train_system(files,
                                   filesData,
                                   autovectors,
                                   images_per_subject)

    if(response):
        return JsonResponse({'type': 'success',
                             'title': '¡Registrado!',
                             'message': 'Se ha(n) registrado con exito al' +
                             'sistema.'})
    else:
        return JsonResponse({'type': 'error',
                             'title': 'No registrado',
                             'message': 'No se ha(n) podido registrar'})


def recognize(request):
    """
        @summary: related to the function that recognize.

        Parameters
        ----------
        @param request: a method of web

        Returns
        ----------
        @return: a Json answer if it fails, or the answer in terms of html
    """
    if request.method != 'POST':
        # No other method are allowed for this function than post.
        return JsonResponse({'type': 'error',
                             'title': 'Metodo invalido',
                             'message': 'No se permiten otros metodos además' +
                                        'de post.'})

    files = request.FILES
    response = facade.recognize_subject(files['subject'])

    return JsonResponse({'type': 'success',
                         'title': 'Se ha reconocido al sujeto',
                         'message': 'El rostro pertenece al sujeto: '
                         + response})


def signin(request):
    """
        @summary: related to the function helps to log in.

        Parameters
        ----------
        @param request: a method of web

        Returns
        ----------
        @return: a Json answer if it fails, or the answer in terms of html
    """
    if request.method != 'POST':
        # No other method are allowed for this function than post.
        return JsonResponse({'type': 'error',
                             'title': 'Metodo invalido',
                             'message': 'No se permiten otros metodos además' +
                                        'de post.'})

    user = {
        'email': request.POST['email'],
        'password': request.POST['password']
    }

    if(facade.signin(user)):
        return render(request, 'index.html', {'userEmail': user['email']})

    return render(request, 'index.html')


def logout(request):
    """
        @summary: related to the function helps to log in.

        Parameters
        ----------
        @param request: a method of web

        Returns
        ----------
        @return: a Json answer if it fails, or the answer in terms of json too.
    """
    if request.method != 'POST':
        # No other method are allowed for this function than post.
        return JsonResponse({'type': 'error',
                             'title': 'Metodo invalido',
                             'message': 'No se permiten otros metodos además' +
                                        'de post.'})

    return JsonResponse({'type': 'success',
                         'title': 'Se ha cerrado sesión',
                         'message': ''})
