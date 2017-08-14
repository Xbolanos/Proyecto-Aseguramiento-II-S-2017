
from django.conf.urls import url
from ImagesManagement import views
urlpatterns = [
    url(r'^$', views.index,name='index'),
    

    
]