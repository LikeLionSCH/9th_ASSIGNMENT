from django.shortcuts import render

from .models import *

# Create your views here.

def home (request):
    blogs = Blog.objects.all()
    return render(request,'home.html',{'blogs':blogs})

def cat (request):
    cats = Cat.objects.all()
    return render(request, 'cat.html', {'cats': cats})