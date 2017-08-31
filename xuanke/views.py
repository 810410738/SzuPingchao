# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import UserInfo
# Create your views here.

@csrf_exempt
def index(request):
    if request.method == 'POST':
        UserInfo(number=request.POST['stu_no'],  passwd=request.POST['passwd']).save()
        return render(request, "xuanke/post.html")
    return HttpResponse("not post")



