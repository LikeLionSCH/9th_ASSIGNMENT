from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('choco/', views.choco, name='choco'),
    path('<str:id>', views.detail, name='detail'),
    path('new/', views.new, name='new'), 
    path('create/', views.create, name='create'), 
    path('edit/<str:id>', views.edit, name='edit'), 
    path('update/<str:id>', views.update, name='update'), 
    path('delete/<str:id>', views.delete, name='delete'), 
]