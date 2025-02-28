from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='news_images/', null=True, blank=True)  

    def __str__(self):
        return self.title