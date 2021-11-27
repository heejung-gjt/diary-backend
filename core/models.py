from django.db import models


class TimeStampable(models.Model):
  created_at = models.TextField(blank=True)
  updated_at = models.TextField(blank=True)

  class Meta:
    abstract = True


class Deleteable(models.Model):
  deleted_at = models.BooleanField(default=False)

  class Meta:
    abstract = True

