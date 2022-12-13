from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True)


class Feedback(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField()
    mark = models.IntegerField(default=0)
    authorId = models.ForeignKey('CustomUser', on_delete=models.CASCADE, default=1)


class Record(models.Model):
    id = models.AutoField(primary_key=True)
    service = models.ForeignKey('Service', on_delete=models.CASCADE, default=1)
    date = models.TextField()
    comments = models.TextField()
    authorId = models.ForeignKey('CustomUser', on_delete=models.CASCADE, default=1)

class Service(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    price = models.IntegerField(default=0)