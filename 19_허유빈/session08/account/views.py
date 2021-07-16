from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.utils import timezone


# Create your views here.
def home(request) :
    cats = Cat.objects.all()
    return render(request, 'home_cat.html', {'cats':cats})

def detail(request, id) :
    cat = get_object_or_404(Cat, pk = id)
    return render(request, 'detail_cat.html', {'cat':cat})


def new(request) :
    return render(request, 'new_cat.html')

def create(request) :
    new_cat = Cat()
    new_cat.title = request.POST['title']
    new_cat.author = request.POST['author']
    new_cat.image = request.FILES['image']
    new_cat.body = request.POST['body']
    new_cat.pub_date = timezone.now()
    new_cat.save()
    return redirect('home_cat')