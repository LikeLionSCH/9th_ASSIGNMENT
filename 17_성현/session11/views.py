from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, authenticate
from .models import *
from django.core.paginator import Paginator
from django.utils import timezone
# Create your views here.

def home(request):
    diaryList = Diary.objects.all()
    paginator = Paginator(diaryList, 3)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    search_word = request.POST.get('search_word')
    if search_word:
        diarys = diaryList.filter(title__icontains = search_word)
        return render(request, 'search.html', {'diary':diarys, 'search_word':search_word})
    return render(request, 'home.html', {'diary':page})

def user_logout(request):
    logout(request)
    return redirect('home')

def detail(request, id):
    diarys = get_object_or_404(Diary, pk=id)
    return render(request, 'detail.html', {'diary':diarys})

def goAdd(request):
    return render(request, 'add.html')

def add(request):
    new_Diary = Diary()
    new_Diary.title = request.POST['title']
    new_Diary.body = request.POST['body']
    new_Diary.weather = request.POST['weather']
    new_Diary.photo = request.FILES['photo']
    new_Diary.time = timezone.now()
    new_Diary.save()
    return redirect('home')

def delete(request, id):
    delete_Diary = Diary.objects.get(id = id)
    delete_Diary.delete()
    return redirect('home')

def gallery(request):
    diaryList = Diary.objects.all()
    paginator = Paginator(diaryList, 3)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'gallery.html', {'diary':page})

def search(request):
    diarys = Diary.objects.all()
    search_word = request.POST.get('search_word')
    if search_word:
        diarys = diarys.filter(title__icontains = search_word)
        return render(request, 'search.html', {'diary':diarys, 'search_word':search_word})
    return render(request, 'search.html', {'diary':diarys, 'search_word':search_word})