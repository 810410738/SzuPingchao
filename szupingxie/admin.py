from django.contrib import admin
from .models import ZhaoXinBaoMing
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'sex', 'college', 'phone', 'stu_no', 'wechat', 'time']

admin.site.register(ZhaoXinBaoMing, PostAdmin)
