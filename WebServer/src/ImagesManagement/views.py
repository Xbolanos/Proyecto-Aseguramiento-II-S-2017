from django.shortcuts import render
from django import forms
from django.core.files.storage import FileSystemStorage

class UploadFileForm(forms.Form):
     """
        @summary: This function is in charge of upload files form.
        
        Parameters
        ----------
        @param form.Form= is the form that going to be the upload file.
        
        Returns
        ----------
        @return: void
     """
     title = forms.CharField(max_length=100)
     file = forms.ImageField()

     

def index(request):
     """
        @summary: This function is in charge of get the html.
        
        Parameters
        ----------
        @param request: is the state from the system 
        
        Returns
        ----------
        @return: HttpResponse
     """
     return render(request, 'html/inicio.html')

def upload_image(request):
     """
        @summary: This function is in charge of get the html.
        
        Parameters
        ----------
        @param request: is the state from the system 
        
        Returns
        ----------
        @return: HttpResponse
     """
     if request.method == 'POST':
        proccess_files(request.FILES.getlist('files'))
        
     return render(request, 'html/inicio.html')

def proccess_files(files):
     """
        @summary: This function is in charge of get all files that was sending in the front end.
        
        Parameters
        ----------
        @param files: array of files 
        
        Returns
        ----------
        @return: void
     """
     fs = FileSystemStorage()
    
     for file in files:
        filename = fs.save(file.name, file)
        fileurl = fs.url(filename)
        print(filename)
        print(fileurl)