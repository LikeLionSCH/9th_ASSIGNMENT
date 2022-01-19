from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('create', views.create, name="create"),
    path('detail/<str:id>', views.detail, name="detail"),
    path('edit/<str:id>', views.edit, name="edit"),
    path('delete/<str:id>', views.delete, name="delete"),

    # comment
    path('create-comment/<str:id>/', views.create_comment, name="create-comment"),
    path('delete-comment/<str:board_id>/<str:comment_id>/', views.delete_comment, name="delete_comment")
]