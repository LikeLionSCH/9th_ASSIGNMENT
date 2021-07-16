from django.contrib.admin import autodiscover
from django.db import models
# Create your models here.

class Board(models.Model) : 
    title = models.CharField(max_length=100)
    body = models.TextField()
    pub_date = models.DateTimeField()
    author = models.ForeignKey('account.User', on_delete= models.CASCADE) 

    def __str__(self) : 
        return self.title

class Comment(models.Model) : 
    board = models.ForeignKey(Board, on_delete = models.CASCADE)
    writer = models.ForeignKey('account.User', on_delete = models.CASCADE)
    date = models.DateTimeField()
    content = models.TextField()

    def __str__(self) : 
        return self.content
    