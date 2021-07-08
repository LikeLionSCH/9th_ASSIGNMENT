from django.db import models

# 회원가입 signup 시 필요한 Account 정보
# 이름, 닉네임, 이메일주소, 비밀번호, 프로필이미지, 회원 생성날짜, 
class User(models.Model): # models 모듈 안에 있는 Model 클래스 상태
    user_name=models.CharField(max_length=20)
    user_id=models.CharField(max_length=30)
    user_password=models.CharField(max_length=20)
    user_profileImg=models.ImageField(upload_to = "account/", blank=True, null=True)
    user_createdDate=models.DateTimeField()
    
    def __str__(self):
        return self.user_name