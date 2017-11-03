'''
Created on Aug 12, 2017

@author: erickhdez, bermudezarii, xbolanos, nicolmorice
'''

from controller import facade
from django.shortcuts import render


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

    data = request.body.decode('UTF-8')  # Turns bytes body into a string.
    data = eval(data)  # Turns the string into a working list.

    reponse = facade.train_system(date)
    return JsonResponse(response)
