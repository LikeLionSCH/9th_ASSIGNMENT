from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    date = models.DateTimeField()
    body = models.TextField(null=True)
    
    # 이름 설정
    def __str__(self):
        return self.name