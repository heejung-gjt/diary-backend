from django.db import models
from django.db import models

from core.models import TimeStampable


class User(TimeStampable):
    userid = models.CharField(max_length=32)
    password = models.CharField(max_length=32)

