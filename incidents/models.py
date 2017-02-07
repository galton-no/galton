from django.db import models


class TwitterStatus(models.Model):
    foreign_key = models.CharField(max_length=500)
