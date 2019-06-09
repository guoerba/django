# -*- coding:utf-8 -*-
import django.http as http
from django.shortcuts import render
import time

def hello(request):
    return http.HttpResponse("Hello World!")

def helloview(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request,'hello.html',context)

def baidu(request):
    return render(request,"baidu.html")

def currenttime(request):
    context = {}
    context['ctime'] = time.asctime(time.localtime(time.time()))
    return render(request,'currenttime.html',context)
    #return http.HttpResponse("当前时间是 {0}".format(time.asctime(time.localtime(time.time()))))