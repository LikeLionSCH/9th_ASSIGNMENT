from django.shortcuts import render
from .models import *

def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs':blogs});

def cat(request):
    cat = Cat.objects.all()
    return render(request, 'cat.html', {'cat': cat})