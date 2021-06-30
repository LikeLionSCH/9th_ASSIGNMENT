from django.shortcuts import render

from .models import *
# Create your views here.
def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs':blogs})

def dog(request):
    rabbits = Rabbit.objects.all()
    return render(request, 'dog.html', {'rabbits':rabbits})

