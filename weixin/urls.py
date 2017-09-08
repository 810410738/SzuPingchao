from django.conf.urls import url
from . import views

app_name = 'weixin'
urlpatterns = [
    url(r'^', views.weixin_main),
]