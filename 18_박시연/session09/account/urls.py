from os import stat
from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test, name='test'),
]