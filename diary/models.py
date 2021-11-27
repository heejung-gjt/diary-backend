from django.db import models

from user.models import User
from core.models import TimeStampable


class Article(TimeStampable):
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='article')
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.TextField(blank=True)

    class Meta:
        db_table = "articles"
