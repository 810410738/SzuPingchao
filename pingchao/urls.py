from django.conf.urls import url

from . import views

app_name = 'pingchao'
urlpatterns = [
    url(r'^&', views.index),
]
