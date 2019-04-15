from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="followers", blank=True)
    # 어떤 모델과 연결시킬지('self' or settings.AUTH_USER_MODEL), related_name(역참조), blank(이 칸은 비워도 됨)

    def __str__(self):
        return self.username