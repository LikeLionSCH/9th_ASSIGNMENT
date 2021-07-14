from django.urls import path
from . import views

urlpatterns=[
    path('test/', views.test, name='test'),
    path('signup/', views.signup, name='signup'),
    path('accountCreate/', views.accountCreate, name='accountCreate'),
    path('accountHome/', views.accountHome, name='accountHome'),
]