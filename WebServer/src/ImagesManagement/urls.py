
from django.conf.urls import url
from ImagesManagement import views
urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^index$', views.index,name='index'),
    url(r'^uploadimage$', views.upload_image,name='uploadimage'),
]