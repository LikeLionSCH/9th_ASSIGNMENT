from django.shortcuts import render, redirect
from .models import *


# Create your views here.
def test(requset):
    print("정상 작동합니다.")

def todo(request, id):
    return render(request, 'todo.html')