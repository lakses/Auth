from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Forum(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self): 
        return self.title

class Topic(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, related_name='topics')
    title = models.CharField(max_length=255, null=False)  
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):  
        return self.title

class Comment(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='comments',default='cool')
    content = models.TextField(default='cool')  
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  

    def __str__(self):  
        return f'Comment by {self.created_by} on {self.created_at}'
