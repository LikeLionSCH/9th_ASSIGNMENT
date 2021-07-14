from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:id>', views.detail, name='detail'), # <str:id> - 가변적인 값 처리 가능
    path('cat/', views.cat, name='cat'),
    path('post/', views.make_post, name='post'),
    path('update/<str:id>', views.update, name='update'),
    path('delete/<str:id>', views.delete, name='delete'),
    path('create_comment/<int:blog_id>', views.create_comment, name="create_comment"),
    path('update_comment/<int:blog_id>/<int:comment_id>', views.update_comment, name="update_comment"),
    path('delete_comment/<int:blog_id>/<int:comment_id>', views.delete_comment, name="delete_comment"),
]