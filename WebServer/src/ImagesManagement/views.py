from django.shortcuts import render
from django import forms
from django.core.files.storage import FileSystemStorage

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=100)
    file = forms.ImageField()

def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "holii"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'html/inicio.html', context_dict)

def upload_image(request):
    if request.method == 'POST':
        proccess_files(request.FILES.getlist('files'))
        
    return render(request, 'html/inicio.html')

def proccess_files(files):
    fs = FileSystemStorage()
    
    for file in files:
        filename = fs.save(file.name, file)
        fileurl = fs.url(filename)
        print(filename)
        print(fileurl)