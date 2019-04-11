from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings

# Create your models here.
class Post(models.Model):
    content = models.CharField(max_length=100)
    # image = models.ImageField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE) # 상위 파일이 지워지면 같이 지워지게 만듦, on_delete=models.CASCADE
    file = ProcessedImageField(
                upload_to = 'posts/images', # 저장위치
                processors = [ResizeToFill(600,600)], # 크기지정
                format = 'JPEG',
                options = {'quality':90},
        )
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    