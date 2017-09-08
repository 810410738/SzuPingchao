<<<<<<< HEAD
#-*- coding:utf-8 -*-
from django.http.response import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from wechat_sdk import WechatConf
from wechat_sdk import WechatBasic
from wechat_sdk.exceptions import ParseError
from wechat_sdk.messages import (TextMessage, VoiceMessage, ImageMessage, VideoMessage, LinkMessage, LocationMessage, EventMessage, ShortVideoMessage)
conf = WechatConf(
   token='test',
   # appid='YOUR_APPID',
   # appsecret='YOUR_APPSECRET',
)
@csrf_exempt
def wechat_main(request):
   signature = request.GET.get('signature')
   timestamp = request.GET.get('timestamp')
   nonce = request.GET.get('nonce')
   wechat_instance = WechatBasic(conf=conf)
   if not wechat_instance.check_signature(signature=signature, timestamp=timestamp, nonce=nonce):
       return HttpResponseBadRequest('Verify Failed')
   else:
       if request.method == 'GET':
           response = request.GET.get('echostr', 'error')
       else:
           try:
               wechat_instance.parse_data(request.body)
               message = wechat_instance.get_message()
               if isinstance(message, TextMessage):
                   reply_text = 'text'
               elif isinstance(message, VoiceMessage):
                   reply_text = 'voice'
               elif isinstance(message, ImageMessage):
                   reply_text = 'image'
               elif isinstance(message, LinkMessage):
                   reply_text = 'link'
               elif isinstance(message, LocationMessage):
                   reply_text = 'location'
               elif isinstance(message, VideoMessage):
                   reply_text = 'video'
               elif isinstance(message, ShortVideoMessage):
                   reply_text = 'shortvideo'
               else:
                   reply_text = 'other'
               response = wechat_instance.response_text(content=reply_text)
           except ParseError:
               return HttpResponseBadRequest('Invalid XML Data')
       return HttpResponse(response, content_type="application/xml")
=======
>>>>>>> parent of a6ed538... 公众号回复功能（测试）
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseBadRequest
import hashlib
import json
from django.utils.encoding import smart_str
# Create your views here.
WEIXIN_TOKEN = 'test'

@csrf_exempt
def weixin_main(request):
    """
       所有的消息都会先进入这个函数进行处理，函数包含两个功能，
       微信接入验证是GET方法，
       微信正常的收发消息是用POST方法。
       """
    if request.method == 'GET':
        signature = request.GET.get('signature', None)
        timestamp = request.GET.get('timestamp', None)
        nonce = request.GET.get('nonce', None)
        echostr = request.GET.get('echostr', None)
        token = WEIXIN_TOKEN
        if not wechat_instance.check_signature(signature=signature, timestamp=timestamp, nonce=nonce):
            return HttpResponseBadRequest('Verify Failed')

        return HttpResponse(echostr, content_type='text/plain')
    else:
        # 解析本次请求的 XML 数据
        try:
            wechat_instance.parse_data(data=request.body)
        except ParseError:
            return HttpResponseBadRequest('Invalid XML Data')
         # 获取解析好的微信请求信息
        message = wechat_instance.get_message()

        if isinstance(message, TextMessage):
<<<<<<< HEAD


=======
>>>>>>> parent of a6ed538... 公众号回复功能（测试）







