from django.contrib import admin
from .models import Board
from .models import Comment

admin.site.register(Board)
admin.site.register(Comment)