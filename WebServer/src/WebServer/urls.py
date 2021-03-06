"""WebServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
    @version: version 1.0 beta
"""
from django.conf.urls import url
from controller import ui


"""
This variable calls the correct route from view module
"""
urlpatterns = [
    url(r'^$', ui.show_index_page),
    url(r'^index$', ui.show_index_page),
    url(r'^learn$', ui.learn),
    url(r'^recognize$', ui.recognize),
    url(r'^signin$', ui.signin),
    url(r'^logout$', ui.logout)
]
