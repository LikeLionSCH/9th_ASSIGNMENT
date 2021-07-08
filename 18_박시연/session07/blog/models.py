from django.db import models

# Create your models here.

# models 모듈 안에 있는 Model 클래스를 상속받습니다.
class Blog(models.Model) :
    # title은 글자를 입력 받고, 최대 입력 수는 100자이다.
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = "blog/", blank=True, null=True)

def __str__(self):
    return self.title

# models 모듈 안에 있는 Model 클래스를 상속받습니다.
class Cat(models.Model) :
    # title은 글자를 입력 받고, 최대 입력 수는 100자이다.
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = "cat/", blank=True, null=True)

# 제목 설정
