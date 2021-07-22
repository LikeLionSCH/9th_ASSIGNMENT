from django.db import models

class Diary(models.Model):
    title=models.CharField(max_length=100) # 일기 제목
    pub_date=models.DateTimeField() # 일기 날짜
    mood=models.CharField(max_length=100) # 오늘의 기분
    weather=models.CharField(max_length=20) # 오늘의 날씨
    body=models.TextField() # 일기 내용
    image=models.ImageField(upload_to="diary/", blank=True, null=True) # 첨부 사진
    
    def __str__(self):
        return self.title