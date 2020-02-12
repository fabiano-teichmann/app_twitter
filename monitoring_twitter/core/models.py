from django.contrib.auth.models import User
from django.db import models


class Tweet(models.Model):
    date_publish = models.DateTimeField()
    author = models.CharField(max_length=200)
    message = models.CharField(max_length=280)
    hash_tag = models.CharField(max_length=60)


class HashTag(models.Model):
    hash_tag = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
