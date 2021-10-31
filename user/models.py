from behaviors import TimeStampable
from django.db import models
from django.db import models
# from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, PermissionsMixin)


class User(TimeStampable):
    userid = models.CharField(max_length=70)
    password = models.CharField(max_length=200)
    
