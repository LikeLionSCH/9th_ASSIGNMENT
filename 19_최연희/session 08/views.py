from diary.models import Diary, Rabbit
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.utils import timezone

# Create your views here.

def home(request):
    # 작성한 객체 다 출력
    diarys = Diary.objects.all()
    return render(request, 'home.html', {'diarys':diarys})

def rabbit(request):
    rabbits = Rabbit.objects.all()
    return render(request, 'rabbit.html', {'rabbits':rabbits})

def detail(request, id):
    diary = get_object_or_404(Diary, pk=id)
    return render(request, 'detail.html', {'diary':diary})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_diary = Diary()
    new_diary.title = request.POST['title']
    new_diary.author = request.POST['author']
    new_diary.image = request.FILES['image']
    new_diary.body = request.POST['body']
    new_diary.todolist = request.POST['todolist']
    new_diary.pub_date = timezone.now()
    new_diary.save()
    return redirect('home')

def edit(request, id):
    diary = Diary.objects.get(id = id)
    return render(request, 'edit.html', {'diary':diary})


def update(request, id):
    update_diary = Diary.objects.get(id = id)
    update_diary.title = request.POST['title']
    update_diary.author = request.POST['author']
    update_diary.body = request.POST['body']
    update_diary.todolist = request.POST['todolist']
    update_diary.save()
    return redirect('detail', update_diary.id)

def delete(request, id):
    delete_diary = Diary.objects.get(id = id)
    delete_diary.delete()
    return redirect('home')