"""blogproject URL Configuration

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

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dog', views.dog, name='dog'),
    path('<str:id>', views.detail, name='detail'),
    path('post/', views.make_post, name='post'),
    path('update/<str:id>', views.update, name='update'),
    path('delete/<str:id>', views.delete, name='delete'),

    #comment
    path('create_comment/<int:blog_id>', views.create_comment, name="create_comment"),
    path('delete_comment/<int:blog_id>/<int:comment_id>/', views.delete_comment, name="delete_comment"),
    path('update_comment/<int:blog_id>/<int:comment_id>/', views.update_comment, name="update_comment"),

]