from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="followers", blank=True)
    # 어떤 모델과 연결시킬지('self' or settings.AUTH_USER_MODEL), related_name(역참조), blank(이 칸은 비워도 됨)
    introduce = models.TextField()
    profile_image = ProcessedImageField(
                upload_to = 'accounts/images', # 저장위치
                processors = [ResizeToFill(150,150)], # 크기지정
                format = 'JPEG',
                options = {'quality':90},
                blank = True
        )
    def __str__(self):
        return self.username