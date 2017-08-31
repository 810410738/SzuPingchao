from django.db import models

# Create your models here.
class UserInfo(models.Model):
    number = models.CharField(max_length=20)
    passwd = models.CharField(max_length=30)