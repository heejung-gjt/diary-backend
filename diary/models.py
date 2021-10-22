from django.db import models
import time


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.TextField(blank=True)
    created_at = models.TextField(default=time.time())
    updated_at = models.TextField(blank=True)

    def __str__(self):
        return self.title