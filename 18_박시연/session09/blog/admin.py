from django.contrib import admin
# .models는 현재 경로에서 models를 지정한다. Blog 불러오기
from .models import Blog

# Register your models here.

# Blog 모델을 admin 사이트에 등록
admin.site.register(Blog)