from django.urls import path
from restaurant import views

urlpatterns = [
    path('', views.re_list, name='re_list'),
    path('<str:id>', views.re_detail, name='re_detail'),
    path('new/', views.re_new, name='re_new'), 
    path('create/', views.re_create, name='re_create'), 
    path('edit/<str:id>', views.re_edit, name='re_edit'), 
    path('update/<str:id>', views.re_update, name='re_update'), 
    path('delete/<str:id>', views.re_delete, name='re_delete'), 
]