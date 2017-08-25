from django.contrib import admin
from .models import TeenGame1
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['name', 'sex', 'employer', 'phone', 'id_card']

admin.site.register(TeenGame1, PostAdmin)
