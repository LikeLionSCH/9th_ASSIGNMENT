from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User
from .models import User
from django.contrib import auth
# Create your views here.

# def home(request):
#     return render(request, 'home.html')

def user_login(request):
    # POST 방식으로 들어오면 
    if request.method == "POST" : 
        username = request.POST["username"]
        password = request.POST["password"]
        # 해당 계정 정보가 있는지 확인 
        user = authenticate(username = username, password = password)
        print(username)
        print(password)
        # user 가 존재하면 
        if user is not None : 
            # 로그인
            login(request, user)
            print("성공")
            # home 으로 이동 
            return redirect('home')
        # user 가 존재하지 않으면 
        else : 
            # 에러문구를 리턴한다. 
            print("실패")
            return render(request, 'login.html', {'error' : '아이디와 비밀번호가 맞지 않습니다. '})
    # POST 방식이 아닐 경우 login 에서 유지 
    else : 
        return render(request, 'login.html')

def user_signup(request):
    # POST 방식으로 들어오면 아래의 과정 실행 
    if request.method == "POST":
        # 비밀번호 확인해서 같으면 user create 실행 
        if request.POST["password"] == request.POST["password2"]:
            user = User.objects.create_user(
                # 장고 기본 유저 필드
                username = request.POST["username"],
                password = request.POST["password"], 
                # 확장 유저 필드 
                nickname = request.POST["nickname"],
                university = request.POST["university"],
            )
            # password 확인까지 마쳤을 때 login 되면서 home 으로 이동. 
            user.save()
            auth.login(request, user)
            return redirect('home')
        # password 비교 시 틀렸으면 signup 페이지에 머무름 
        else: 
            return render(request, 'signup.html')
    # 메소드 방식이 post 가 아닐경우 signup 에 머무름 . 
    else: 
        return render(request, 'signup.html')

def user_logout(request): 
    logout(request)
    return redirect('home')

def mypage(request):
    return render(request, 'mypage.html')