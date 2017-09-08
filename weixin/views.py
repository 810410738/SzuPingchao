# -*- coding:utf-8 -*-
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
    # 解析本次请求的 XML 数据
    try:
        wechat_instance.parse_data(data=request.body)
    except ParseError:
        return HttpResponseBadRequest('Invalid XML Data')
         # 获取解析好的微信请求信息
    message = wechat_instance.get_message()

    response = wechat_instance.response_text(
        content=(
            '感谢你的关注'
        )
    )
    if isinstance(message, TextMessage):
        content = message.content.strip()
        if content == '你好':
            reply_text = "Hello World"
        else:
            reply_text = "....."
        response = wechat_instance.response_text(content=reply_text)
    return HttpResponse(response, content_type='application/xml')






