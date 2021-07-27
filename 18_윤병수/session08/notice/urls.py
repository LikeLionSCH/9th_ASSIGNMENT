from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_1, name='home_1'),
    path('<str:id>', views.detail_1, name='detail_1'),
    path('new_1/', views.new_1, name='new_1'),
    path('create_1/', views.create_1, name='create_1'),
    path('edit_1/<str:id>', views.edit_1, name='edit_1'),
    path('update_1/<str:id>', views.update_1, name='update_1'),
    path('delete_1/<str:id>', views.delete_1, name='delete_1'),
]