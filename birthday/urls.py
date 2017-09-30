from django.conf.urls import url
from . import views

app_name = 'birthday'
urlpatterns = [
    url(r'^$', views.index),
    url(r'^cake/$', views.other),
    ]