'''
Created on Aug 12, 2017

@author: erickhdez, bermudezarii, xbolanos, nicolmorice
@version: version 1.0 beta
'''

from controller import facade
from django.shortcuts import render
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from WebServer.settings import MEDIA_ROOT
import os


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
    fs = FileSystemStorage(location=MEDIA_ROOT)
    basePath = fs.location
    paths = []
    
    for key in files.keys():
        file = files[key]
        fileData = filesData[key + 'data']
        
        try:
            
            if(len(fileData) == 2):
                fileData = fileData[:1] + '0' + fileData[1:]
            
            os.makedirs(fileData)
        except Exception:
            pass
        
        fs.location = basePath + '/' + fileData
        
        fileName = fs.save(file.name, file)
        fileUrl = fs.location + '/' + fileName
        paths.append(fileUrl)

    response = facade.train_system(paths)
    return JsonResponse(response)

def recognize(request):
    if request.method != 'POST':
        # No other method are allowed for this function than post.
        return JsonResponse({'type': 'error',
                             'title': 'Metodo invalido',
                             'message': 'No se permiten otros metodos además' +
                                        'de post.'})
        
    data = request.body.decode('UTF-8')  # Turns bytes body into a string.

    response = facade.recognize_subject(data)
    return JsonResponse(response)

def signin(request):
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
    if request.method != 'POST':
        # No other method are allowed for this function than post.
        return JsonResponse({'type': 'error',
                             'title': 'Metodo invalido',
                             'message': 'No se permiten otros metodos además' +
                                        'de post.'})
        
    return JsonResponse({'type': 'success',
            'title': 'Se ha cerrado sesión',
            'message': ''})
    
