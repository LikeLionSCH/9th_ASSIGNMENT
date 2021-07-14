from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone

class Board(models.Model):
    title = models.CharField(max_length=100)
    body=models.TextField()
    pub_date=models.DateTimeField()
    author=models.ForeignKey('account.User', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    content=models.TextField()
    writer=models.ForeignKey('account.User', on_delete=models.CASCADE)
    board=models.ForeignKey(Board, on_delete=CASCADE)
    created_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.content