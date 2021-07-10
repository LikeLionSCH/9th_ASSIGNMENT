from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.utils import timezone
# Create your views here.

def home_1 (request) :

    notices = Blog_1.objects.all()

    return render (request, 'home_1.html', {'notices':notices})

def detail_1 (request, id) :

    notice = get_object_or_404(Blog_1, pk=id)

    return render(request, 'detail_1.html', {'notice':notice})

def create_1 (request) :
    new_blog = Blog_1()
    new_blog.title = request.POST['title']
    new_blog.author = request.POST['author']
    new_blog.image = request.FILES['image']
    new_blog.body = request.POST['body']
    new_blog.pub_date = timezone.now()
    new_blog.save()
    return redirect('home_1')

def new_1 (request) :
    return render(request, 'new_1.html')

def edit_1 (request, id) :
    notice = Blog_1.objects.get(id = id)
    return render(request, 'edit_1.html', {'notice':notice})

def update_1 (request, id) :
    update_blog = Blog_1.objects.get(id = id)
    update_blog.title = request.POST['title']
    update_blog.author = request.POST['author']
    update_blog.body = request.POST['body']
    update_blog.save()
    return redirect('detail_1', update_blog.id)

def delete_1 (request, id) :
    delete_blog = Blog_1.objects.get(id = id)
    delete_blog.delete()
    return redirect('home_1')


