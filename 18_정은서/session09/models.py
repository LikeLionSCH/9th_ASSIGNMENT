from django.db import models
from django.db.models.fields import AutoField

# Create your models here.
class Cat(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image=models.ImageField(upload_to = "cat/", blank=True, null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.content