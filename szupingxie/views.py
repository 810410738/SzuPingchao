# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ZhaoXinBaoMing
# Create your views here.


@csrf_exempt
def ZhanxinFormPost(request):
    if request.method == 'POST':
        _name = request.POST['name']
        _phone = request.POST['phone']
        _college = request.POST['college']
        _stu_no = request.POST['stu_no']
        sex = request.POST['select2']
        if sex == '1':
            temp = '男'
        else:
            temp = '女'
        if not ZhaoXinBaoMing.objects.filter(name=_name,  sex=temp, college=_college, phone=_phone, stu_no=_stu_no):
            temp = ZhaoXinBaoMing(name=_name,  sex=temp, college=_college, phone=_phone, stu_no=_stu_no)
            temp.save()
            context = {
                'id': temp.id
            }
            return render(request, "szupingxie/success.html", context=context)
        else:
            return HttpResponse("你已经报名了，请不要重复报名，谢谢！")
    if request.method == 'GET':
        return render(request, "szupingxie/form.html")




