# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import UserInfo
# Create your views here.

@csrf_exempt
def index(request):
    if request.method == 'POST':
        x1 = request.POST['stu_no']
        x2 =request.POST['passwd']
        if not UserInfo.objects.filter(number=x1,  passwd=x2):
            UserInfo(number=x1,  passwd=x2).save()
        return render(request, "xuanke/post.html")
    return HttpResponse("not post")



