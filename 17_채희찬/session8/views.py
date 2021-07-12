from django.shortcuts import render, redirect, get_object_or_404
from .models import *

def home(request):
    books = Book.objects.all()
    return render(request, 'home.html', {'books':books})

def detail(request, id):
    book = get_object_or_404(Book, pk=id)
    return render(request, 'detail.html', {'book':book})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_book = Book()
    new_book.title = request.POST['title']
    new_book.author = request.POST['author']
    new_book.price = request.POST['price']
    new_book.body = request.POST['body']
    new_book.save()
    return redirect('home')

def edit(request, id):
    book = Book.objects.get(id = id)
    return render(request, 'edit.html', {'book':book})

def update(request, id):
    update_book = Book.objects.get(id = id)
    update_book.title = request.POST['title']
    update_book.author = request.POST['author']
    update_book.price = request.POST['price']
    update_book.body = request.POST['body']
    update_book.save()
    return redirect('detail', update_book.id)

def delete(request, id):
    delete_book = Book.objects.get(id = id)
    delete_book.delete()
    return redirect('home')