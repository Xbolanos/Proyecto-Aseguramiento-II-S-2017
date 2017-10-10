'''
Created on Oct 10, 2017

@author: epikhdez
'''
from controller import system


def show_index_page(request):
    """
    @summary: asks the core system for the home page of the website.

    Parameters
    ----------
    @param request: the http request from the client.

    Return
    ------
    @return: the system response.
    """
    return system.show_index_page(request)


def train_system(request):
    """
    @summary: pass the request to the system so it can get the uploaded images
    and process them.

    Parameters
    ----------
    @param request: the http request from the client.

    Return
    ------
    @return: the system response.
    """
    return system.train_system(request)
