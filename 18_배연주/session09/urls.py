from django.urls import path
from blog import views

urlpatterns = [
    path('', views.home, name='home'),
    path('choco/', views.choco, name='choco'),
    path('<str:id>', views.detail, name='detail'),
    path('post/', views.make_post, name='post'),
    # path('edit/<str:id>', views.edit, name='edit'), 
    path('update/<str:id>', views.update, name='update'), 
    path('delete/<str:id>', views.delete, name='delete'),

    # comment
    path('create_comment/<int:blog_id>', views.create_comment, name="create_comment"), 
    path('update_comment/<int:blog_id>/<int:comment_id>/', views.update_comment, name="update_comment"), 
    path('delete_comment/<int:blog_id>/<int:comment_id>/', views.delete_comment, name="delete_comment"),
]