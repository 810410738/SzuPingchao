from django.db import models

# Create your models here.


class TeenGame1(models.Model):
    name = models.CharField(max_length=10)
    sex = models.CharField(max_length=2)
    employer = models.CharField(max_length=30)
    phone = models.CharField(max_length=11)
    id_card = models.CharField(max_length=20)
