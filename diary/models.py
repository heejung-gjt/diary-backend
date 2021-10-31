import time
from django.db import models
from user.models import User

class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='article')
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.TextField(blank=True)
    created_at = models.TextField(blank=True)
    updated_at = models.TextField(blank=True)

    def __str__(self):
        return self.title