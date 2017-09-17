from django.conf.urls import url
from . import views

app_name = 'szupingxie'
urlpatterns = [
    url(r'^', views.ZhanxinFormPost),
    ]
