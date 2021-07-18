from django.urls import path
from account import views as t

urlpatterns = [
    path('', t.home, name="home_cat"),
    path('new/', t.new, name="new_cat"),
    path('create/', t.create, name="create_cat"),
    path('<str:id>/', t.detail, name="detail_cat"),
    
]
