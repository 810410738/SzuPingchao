# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    if request.method == 'GET':
        return render(request, "birthday/index.html")

def other(request):
    if request.method == 'GET':
        return render(request, "birthday/other.html")




