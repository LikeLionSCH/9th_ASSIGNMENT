from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="blog/", blank=True, null=True)

    # 제목 설정
    def __str__(self):
        return self.title


class Choco(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="blog/", blank=True, null=True)

    # 제목 설정
    def __str__(self):
        return self.title


