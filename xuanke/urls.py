from django.conf.urls import url
from . import views

app_name = 'xuanke'
urlpatterns = [
    url(r'^$', views.index),
]