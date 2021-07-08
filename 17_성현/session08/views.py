from django.shortcuts import render, get_object_or_404, redirect
from .models import *
# Create your views here.

def home (request) :
    blogs = Blog.objects.all()
    return render (request, 'quiz_nonjQ.html', {'blogs':blogs})

def update (request, id) :
    update_blog = Blog.objects.get(id =id)
    update_blog.comment = request.POST['comment']
    update_blog.save()
    blogs = Blog.objects.all()
    return render (request, 'quiz_nonjQ.html', {'blogs':blogs})
