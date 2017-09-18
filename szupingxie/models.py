from django.db import models

# Create your models here.


class ZhaoXinBaoMing(models.Model):
    id = models.AutoField(default=601, primary_key=True)
    name = models.CharField(max_length=10)
    sex = models.CharField(max_length=2)
    college = models.CharField(max_length=30)
    phone = models.CharField(max_length=11)
    stu_no = models.CharField(max_length=20)
    wechat = models.CharField(max_length=30, default=None)
    time = models.DateTimeField(auto_now=True,)
