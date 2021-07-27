from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),   
    path('detail/<str:id>', views.detail, name='detail'), 
    path('edit/<str:id>', views.edit, name='edit'),
    path('delete/<str:id>', views.delete, name='delete'),
]