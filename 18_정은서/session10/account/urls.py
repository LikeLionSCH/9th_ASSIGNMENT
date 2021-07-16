from django.urls import path
from . import views as A
urlpatterns = [
    path('account/signup', A.user_signup, name="signup"),
    path('account/login', A.user_login, name="login"),
    path('account/logout', A.user_logout, name="logout"),
    path('account/mypage', A.mypage, name="mypage"),
]
