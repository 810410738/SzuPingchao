# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseBadRequest
import hashlib
import json
from django.utils.encoding import smart_str
from wechat_sdk import WechatBasic
from wechat_sdk.exceptions import ParseError
from wechat_sdk.messages import TextMessage, VoiceMessage, ImageMessage, VideoMessage, EventMessage
# Create your views here.
wechat_instance = WechatBasic(
    token='test',
    appid='wx68504760f1652652',
    appsecret='af867702558c8c7f62d71ab4e9294c4e',
)
# wechat_instance.create_menu(menu_data={
#     'button': [
#         {
#             'type': 'click',
#             'name': '今日歌曲',
#             'key': 'MUSIC',
#         },
#         {
#             'type': 'click',
#             'name': '简介',
#             'key': 'INTRODUTION',
#         },
#     ]
# })

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

        if isinstance(message, EventMessage):
            if message.type == 'subscribe':
                reply_text = ('欢迎关注jerry的微信号!')
        if isinstance(message, TextMessage):
            content = message.content.strip().encode('utf8')
            if content == "你好":
                reply_text = ("哈哈，你好")
            else:
                reply_text = ("请跟我说你好。。。")

        elif isinstance(message, ImageMessage):
            reply_text = ('这是一张图片，我看不懂~')

        elif isinstance(message, VoiceMessage):
            reply_text = ('这是一段语音，我听不懂~')

        elif isinstance(message, VideoMessage):
            reply_text = ('这是一段视频，我看不懂')
        response = wechat_instance.response_text(content=reply_text)
        return HttpResponse(response, content_type='application/xml')
