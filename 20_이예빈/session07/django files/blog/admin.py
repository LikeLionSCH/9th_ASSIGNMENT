from django.contrib import admin

# .models - 현재 경로에서 models 지정, Blog 불러오기
from .models import Blog
from .models import Cat

# Blog 모델 admin 사이트에 등록
admin.site.register(Blog)
admin.site.register(Cat)