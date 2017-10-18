'''
Created on Aug 12, 2017

@author: erickhdez, bermudezarii, xbolanos, nicolmorice
'''

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
    return facade.train_system(request)
