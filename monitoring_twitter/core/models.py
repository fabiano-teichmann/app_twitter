from django.db import models


class Tweet(models.Model):
    date_publish = models.DateTimeField()
    author = models.CharField(max_length=200)
    message = models.CharField(max_length=280)

