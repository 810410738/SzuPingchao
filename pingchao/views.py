# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import TeenGame1
# Create your views here.


def index(request):
    return render(request, 'pingchao/index.html')


def other(request, x):
    if request.method == 'GET':
        return render(request, 'pingchao/'+x)


@csrf_exempt
def teen_game_post(request):
    if request.method == 'POST':
        if request.session.get('isApply', False):
            return HttpResponse('你已经报名了！')
        sex = request.POST['select2']
        if sex == '1':
            temp = '男'
        else:
            temp = '女'
        TeenGame1(name=request.POST['name'], sex=temp, employer=request.POST['danwei'], phone=request.POST['phonenumber'],id_card=request.POST['idcard']).save()
        request.session['isApply'] = True
        return render(request, 'pingchao/view/teenGameApply/sueecss.html')

