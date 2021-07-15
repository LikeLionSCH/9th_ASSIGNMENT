from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.contrib import auth

# Create your views here.
# def home(request):
#     return render(request, 'home.html')


def user_login(request):
    # POST 방식이라면, 
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        # 해당 계정에 정보가 있는지 확인
        user = authenticate(username = username, password = password)
        print(username)
        print(password)

        # user가 존재한다면,
        if user is not None:
            login(request,user)
            print("성공")
            # 로그인 성공 후, home으로 돌아가기
            return redirect('home')
        # 로그인 실패 시,
        else:
            print("실패")
            return render(request, 'login.html', {'error' : '아이디와 비밀번호가 맞지 않습니다. '})
    # POST가 아닐 경우, login에서 유지
    else:
        return render(request, 'login.html')

def user_signup(request):
    # POST 방식이라면, 
    if request.method == "POST":
        # 비밀번호가 일치한지 확인
        if request.POST["password"] == request.POST["password2"]:
            user = User.objects.create_user(
                # 장고 기본 유저 필드
                username = request.POST["username"],
                password = request.POST["password"],
                # 확장 유저 필드
                nickname = request.POST["nickname"],
                university = request.POST["university"],
            )
            # LOGIN이 완료되면 home으로 이동
            user.save()
            auth.login(request, user)
            return redirect('home')
        # password가 불일치라면 signup 페이지에 머무르기 
        else:
            return render(request, 'signup.html')
    # POST 방식이 아닐 경우 signup 페이지에 머무르기
    else:
        return render(request, 'signup.html')


def user_logout(request):
    logout(request)
    return redirect('home')

def mypage(request):
    return render(request, 'mypage.html')