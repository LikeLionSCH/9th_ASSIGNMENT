from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cat', views.cat, name='cat'),
    path('<str:id>', views.detail, name='detail'),
    path('delete/<str:id>', views.delete, name='delete'),
    path('post/', views.make_post, name='post'),
    path('update/<str:id>', views.update, name='update'),

    # comment
    path('create_comment/<int:blog_id>', views.create_comment, name="create_comment"),
    path('delete_comment/<int:blog_id>/<int:comment_id>/', views.delete_comment, name="delete_comment"),
    path('update_comment/<int:blog_id>/<int:comment_id>/', views.update_comment, name="update_comment"),
]