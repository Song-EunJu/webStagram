from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser): # 상속받고 확장하고 싶은 column들을 추가하면 된다.
    nickname = models.CharField(max_length=20, default="")  # 닉네임
    profileImg = models.ImageField(upload_to = "profile/", blank = True, null = True) # 프로필 사진
    profileMsg = models.CharField(max_length=100, default="") # 소개 