from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="blog/", blank=True, null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

class Dog(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="blog/", blank=True, null=True)

    def __str__(self):
        return self.title