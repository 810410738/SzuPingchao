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







