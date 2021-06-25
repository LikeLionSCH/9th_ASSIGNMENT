from django.shortcuts import render, get_object_or_404

from .models import *

from django.utils import timezone

# Create your views here.
def home (request):
    blogs = Blog.objects.all()

    return render(request, 'home.html', {'blogs':blogs})

def cat (request):
    porsches = Porsche.objects.all()

    return render (request, 'cat.html', {'porsches':porsches})

def detail(request, id):
    blog = get_object_or_404(Blog, pk=id)
    return render(request, 'detail.html', {'blog':blog})

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


