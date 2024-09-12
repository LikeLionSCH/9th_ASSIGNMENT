from django.contrib import admin
from .models import Board
from .models import Comment

# Register your models here.
admin.site.register(Board)
admin.site.register(Comment)