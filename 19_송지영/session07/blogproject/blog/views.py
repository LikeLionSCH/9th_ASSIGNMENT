from django.shortcuts import render

from .models import *

# Create your views here.
def home(request):

    blogs = Blog.objects.all()

    return render (request, 'home.html',{'blogs':blogs})

def dog(request):
    dogs = Dog.objects.all()

    return render (request, 'dog.html',{'dogs':dogs})