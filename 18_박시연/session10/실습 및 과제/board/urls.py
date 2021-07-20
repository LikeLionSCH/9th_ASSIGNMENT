from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('create', views.create, name="create"),
    path('detail/<str:id>', views.detail, name="detail"),
    path('edit/<str:id>', views.edit, name="edit"),
    path('delete/<str:id>', views.delete, name="delete"),
    path('create_comment/<int:board_id>', views.create_comment, name="create_comment"),
    path('delete_comment/<int:board_id>/<int:comment_id>', views.delete_comment, name="delete_comment"),

]