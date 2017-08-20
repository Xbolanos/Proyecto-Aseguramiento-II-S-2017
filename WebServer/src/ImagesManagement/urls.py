'''
Created on Aug 12, 2017

@author: erickhdez, bermudezarii, xbolanos, nicolmorice
'''

from django.conf.urls import url
from ImagesManagement import views

"""
This variable represents the routes from the view the frontend can access.
"""

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^index$', views.index,name='index'),
    url(r'^uploadimage$', views.upload_image,name='uploadimage'),
]