from django.urls import path
from blog import views as b

urlpatterns = [
    path('', b.home, name="home"),
    path('dog/', b.dog, name="dog"),
    path('<str:id>', b.detail, name="detail"),
    path('new/', b.new, name="new"),
    path('create/', b.create, name="create"),
    path('edit/<str:id>/', b.edit, name="edit"),
    path('update/<str:id>/', b.update, name="update"),
    path('delete/<str:id>/', b.delete, name="delete"),
]
