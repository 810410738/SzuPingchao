from django.contrib import admin
from .models import UserInfo
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['number', 'time']
admin.site.register(UserInfo, PostAdmin)