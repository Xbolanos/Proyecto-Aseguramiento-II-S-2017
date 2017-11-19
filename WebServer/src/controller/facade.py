'''
Created on Oct 10, 2017

@author: epikhdez
@version: version 1.0 beta
'''
from controller import system


def get_index_page():
    """
    @summary: asks the core system for the home page of the website.

    Return
    ------
    @return: the website's main page.
    """
    return system.get_index_page()


def train_system(files, filesData, autovectors, images_per_subject):
    """
    @summary: pass the request to the system so it can get the uploaded images
    and process them.

    Parameters
    ----------
    @param files: a dictionary of the files to be added into the system.
    @param filesData: a dictionary with the files data, ej: subjects names.
    @param autovectors: the number of autovectores to be used in the training.
    @param images_per_subject: the number os given images per subject.

    Return
    ------
    @return: the system's response to the request.
    """
    return system.train_system(files,
                               filesData,
                               autovectors,
                               images_per_subject)


def recognize_subject(subject, mode=1):
    """
    @summary: pass the subject to recognize and the requested method to it
    into the system.

    Parameters
    ----------
    @param subject: the subject file to be identified
    @param mode: the method you want to use (0 - centroid, 1 - k neighbors)

    Return
    ------
    @return: a list with the name of the identified subject and messages for
    the user.
    """
    return system.recognize_subject(subject, mode)


def signin(user):
    """
    @summary: attempts to login a user with the given credentials.

    Parameters
    ----------
    @param user: the user's credential packed in an object

    Return
    ------
    @return: true if the login is accepted, false otherwise.
    """
    return system.signin(user)


def logout():
    """
    @summary: attempts to logout the session of the user.

    Return
    ------
    @return: true if the logout was successful, false otherwise.
    """
    return system.logout()
