from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User
from .models import User
from django.contrib import auth
# Create your views here.

# def home(request):
#     return render(request, 'home.html')

def user_login(request):
    if request.method == "POST" : 
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username = username, password = password)
        print(username)
        print(password)
        if user is not None : 
            login(request, user)
            print("성공")
            return redirect('home')
        else : 
            print("실패")
            return render(request, 'login.html', {'error' : '아이디와 비밀번호가 맞지 않습니다. '})
    else : 
        return render(request, 'login.html')

def user_signup(request):
    if request.method == "POST":
        if request.POST["password"] == request.POST["password2"]:
            user = User.objects.create_user(
                username = request.POST["username"],
                password = request.POST["password"], 
                nickname = request.POST["nickname"],
                university = request.POST["university"],
            ) 
            user.save()
            auth.login(request, user)
            return redirect('home')
        else : 
            return render(request, 'signup.html')
    else: 
        return render(request, 'signup.html')

def user_logout(request) : 
    logout(request)
    return redirect('home')

def mypage(request) :
    return render(request, 'mypage.html')