from django.shortcuts import render, HttpResponse
from.models import Photo

# Create your views here.

def home( request):

    quiryset = Photo.objects.all()
    content = {
        'photos' : quiryset
    }
    return render (request,'index.html',content)