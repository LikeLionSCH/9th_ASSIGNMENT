from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    # 블로그의 모든 객체를 가져옴
    blogs = Blog.objects.all()
    # 딕셔너리로 home.html에 보내주기
    return render (request, 'home.html', {'blogs':blogs})

def dog(request):
    # 블로그의 모든 객체를 가져옴
    dogs = Dog.objects.all()
    # 딕셔너리로 home.html에 보내주기
    return render (request, 'dog.html', {'dogs':dogs})