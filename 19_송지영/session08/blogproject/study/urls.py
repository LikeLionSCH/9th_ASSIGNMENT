from django.contrib import admin
from django.urls import path
from study import views as s

urlpatterns = [
    path('study/', s.study, name='study'),
    path('study/<str:id>', s.study_detail, name='study_detail'),
    path('study_post/', s.study_post, name='study_post'),
    path('study_update/<str:id>', s.study_update, name='study_update'),
    path('study_delete/<str:id>', s.study_delete, name='study_delete'),
]