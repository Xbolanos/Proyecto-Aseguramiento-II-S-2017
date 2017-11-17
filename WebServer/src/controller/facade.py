'''
Created on Oct 10, 2017

@author: epikhdez
@version: version 1.0 beta
'''
from controller import system


def get_index_page():
    """
    @summary: asks the core system for the home page of the website.

    Parameters
    ----------
    @param request: the http request from the client.

    Return
    ------
    @return: the system's response to the request.
    """
    return system.get_index_page()


def train_system(files, filesData, autovectors, images_per_subject):
    """
    @summary: pass the request to the system so it can get the uploaded images
    and process them.

    Parameters
    ----------
    @param data: the data from the client's http request.

    Return
    ------
    @return: the system's response to the request.
    """
    return system.train_system(files, filesData, autovectors, images_per_subject)
    
def recognize_subject(handler):
    return system.recognize_subject(handler)

def signin(user):
    return system.signin(user)
