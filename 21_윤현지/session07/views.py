from django.shortcuts import render
from .models import *

# Create your views here.
def home (request) :
    blogs = Blog.objects.all()
    return render (request, 'home.html', {'blogs': blogs})

def haha (request) :
    ncts = NCT.objects.all()
    return render (request, 'haha.html', {'ncts': ncts})
    