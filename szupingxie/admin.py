from django.contrib import admin
from .models import ZhaoXinBaoMing
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['name', 'sex', 'college', 'phone', 'stu_no']

admin.site.register(ZhaoXinBaoMing, PostAdmin)
