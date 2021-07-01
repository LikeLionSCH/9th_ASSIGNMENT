from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:id>', views.detail, name='detail'), # <str:id> - 가변적인 값 처리 가능
    path('cat/', views.cat, name='cat'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('edit/<str:id>', views.edit, name='edit'),
    path('update/<str:id>', views.update, name='update'),
    path('delete/<str:id>', views.delete, name='delete'),
]