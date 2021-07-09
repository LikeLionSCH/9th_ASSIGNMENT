from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.utils import timezone


def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs': blogs})

def choco(request):
    chocos = Choco.objects.all()
    return render(request, 'choco.html', {'chocos': chocos})

def detail(request, id):
    blog = get_object_or_404(Blog, pk=id)
    return render(request, 'detail.html', {'blog': blog})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.author = request.POST['author']
    new_blog.image = request.FILES['image']
    new_blog.body = request.POST['body']
    new_blog.pub_date = timezone.now()
    new_blog.save()
    return redirect('home')

def edit(request, id):
    blog = Blog.objects.get(id=id)
    return render(request, 'edit.html', {'blog': blog})

def update(request, id):
    update_blog = Blog.objects.get(id=id)
    update_blog.title = request.POST['title']
    update_blog.author = request.POST['author']
    update_blog.body = request.POST['body']
    update_blog.save()
    return redirect('detail', update_blog.id)

def delete(request, id):
    delete_blog = Blog.objects.get(id=id)
    delete_blog.delete()
    return redirect('home')