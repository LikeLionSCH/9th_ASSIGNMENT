from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.utils import timezone
# Create your views here.
def home(request):
    cats = Cat.objects.all()
    return render (request, 'home.html', {'cats':cats})

def detail(request, id):
    cat = get_object_or_404(Cat, pk=id)
    return render(request, "detail.html", {"cat":cat})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_cat = Cat()
    new_cat.title = request.POST['title']
    new_cat.author = request.POST['author']
    new_cat.image = request.FILES['image']
    new_cat.body = request.POST['body']
    new_cat.pub_date = timezone.now()
    new_cat.save()
    return redirect('home')

def edit(request, id):
    cat = Cat.objects.get(id=id)
    return render(request, 'edit.html', {'cat':cat})

def update(request, id):
    update_cat = Cat.objects.get(id=id)
    update_cat.title = request.POST['title']
    update_cat.author = request.POST['author']
    update_cat.body = request.POST['body']
    update_cat.save()
    return redirect('detail', update_cat.id)

def delete(request, id):
    delete_cat = Cat.objects.get(id=id)
    delete_cat.delete()
    return redirect('home')
