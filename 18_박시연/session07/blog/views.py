from django.shortcuts import render
from .models import *

# Create your views here.

# home 추가
def home (request) :
    # 블로그의 모든 객체를 가져온다.
    blogs = Blog.objects.all()
    # 딕셔너리 형식으로 home.html에 보내주기 (이름 blogs로.)
    return render (request, 'home.html', {'blogs' : blogs})

def cat (request) :
    cats = Cat.objects.all()
    return render (request, 'cat.html', {'cats' : cats})