from django.db import models
from django.utils import timezone

# Create your models here.
class Board(models.Model) :
    title = models.CharField(max_length=100)
    body = models.TextField()
    pub_date = models.DateTimeField()
    author = models.ForeignKey('account.User', on_delete=models.CASCADE)

    def __str__(self) :
        return self.title

class Comment(models.Model):
    author = models.CharField(max_length=50)
    date = models.DateTimeField()
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.title