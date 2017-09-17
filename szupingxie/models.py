from django.db import models

# Create your models here.


class ZhaoXinBaoMing(models.Model):
    name = models.CharField(max_length=10)
    sex = models.CharField(max_length=2)
    college = models.CharField(max_length=30)
    phone = models.CharField(max_length=11)
    stu_no = models.CharField(max_length=20)
