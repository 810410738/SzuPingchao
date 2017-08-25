from django.conf.urls import url

from . import views

app_name = 'pingchao'
urlpatterns = [
    url(r'^$', views.index),
    url(r'^teen_game_post/$', views.teen_game_post),
    url(r'^(.+)/$', views.other),
]
