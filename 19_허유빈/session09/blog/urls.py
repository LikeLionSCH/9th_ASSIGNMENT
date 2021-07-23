from django.urls import path
from blog import views as b

urlpatterns = [
    path('', b.home, name="home"),
    path('dog/', b.dog, name="dog"),
    path('<str:id>', b.detail, name="detail"),
    # path('new/', b.new, name="new"),
    # path('create/', b.create, name="create"),
    path('post/', b.post, name="post"),
    # path('edit/<str:id>/', b.edit, name="edit"),
    path('update/<str:id>/', b.update, name="update"),
    path('delete/<str:id>/', b.delete, name="delete"),

    path('create_comment/<int:blog_id>/', b.create_comment, name="create_comment"),
    path('update_comment/<int:blog_id>/<int:comment_id>/', b.update_comment, name="update_comment"),
    path('delete_comment/<int:blog_id>/<int:comment_id>/', b.delete_comment, name="delete_comment"),
    
]
