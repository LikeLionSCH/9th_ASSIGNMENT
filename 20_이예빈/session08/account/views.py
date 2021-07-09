from django.shortcuts import render, redirect
from .models import *
from django.utils import timezone

def test(request):
    return render(request, 'test.html')

def accountHome(request):
    accounts = User.objects.all()
    return render(request, 'accountHome.html', {'accounts':accounts});

def accountCreate(request):
    new_account=User()
    new_account.user_name=request.POST['name']
    new_account.user_id=request.POST['id']

    new_account.user_password=request.POST['pw']
    new_account.user_profileImg=request.FILES['profImg']
    new_account.user_createdDate=timezone.now()
    new_account.save()
    return redirect('accountHome')

def signup(request):
    return render(request, 'signupPage.html')