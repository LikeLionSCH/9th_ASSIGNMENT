from django.db import models

# Create your models here.

class Diary(models.Model) :
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = "diary/", blank=True, null=True)

    def __str__(self):
        return self.title