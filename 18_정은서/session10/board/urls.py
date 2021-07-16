from django.urls import path
from . import views as B
urlpatterns = [
    path('', B.home, name="home"),
    path('create', B.create, name="create"),
    path('detail/<str:id>', B.detail, name="detail"),
    path('edit/<str:id>', B.edit, name="edit"),
    path('delete/<str:id>', B.delete, name="delete"),
    ## comment ##
    path('create_comment/<int:board_id>', B.c_comment, name="c_comment"),
    path('delete_comment/<int:board_id>/<int:comment_id>', B.d_comment, name="d_comment"),
]