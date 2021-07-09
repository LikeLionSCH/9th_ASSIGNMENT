"""BoardProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from board import views

urlpatterns = [
    path('', views.home, name="home"),
    path('create', views.create, name="create"),
    path('detail/<str:id>/<str:user>', views.detail, name="detail"),
    path('edit/<str:id>', views.edit, name="edit"),
    path('delete/<str:id>', views.delete, name="delete"),
    path('create_comment/<str:id>/<str:user>', views.create_comment, name="create_comment"),
    path('delete_comment/<str:id>/<str:user>', views.delete_comment, name="delete_comment"),
]
