from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.template import loader, Template
import datetime
from taxApp.getdata.reginf import GetInf
import time
import json
from taxApp.models import Zengzhishui


def hello(request):
	user_list=User.objects.all()
	return render(request, 'table.html',locals())

def add_publisher(request):
	return render(request, 'add_publisher.html', locals())
def table(request):
	user=User.objects.all()
	return redirect(request,'table.html',locals())
def login(request):
	# getinf = GetInf("http://dzswj.szgs.gov.cn/BsfwtWeb/apps/views/login/login.html")
	# driver = getinf.openbrowser()
	# time.sleep(2)
	# driver = getinf.input_infos(driver)
	# time.sleep(1)
	# yzm64,info = getinf.get_yzm64_and_save(driver, './static/img/yzm.jpg')
	return render(request,'login.html',locals())
def index(request):
	return render(request,'index.html',locals())

def chaxun(request):
	return render(request,'chaxun.html',locals())

def fapiao(request):
	return render(request,'fapiao.html',locals())
def taxinf(request):
	return render(request, 'taxinf.html', locals())
def zengzhishui(request):
	if request.method == "POST":
		name1 = request.POST['taxname']
		regadress = request.POST['regadress']
		bussadress = request.POST['bussadress']
		Zengzhishui.objects.create(
            taxname=name1,
            regadress=regadress,
            bussadress=bussadress
        )
		return HttpResponse("添加信息成功！")
	else:
		return render(request, 'zengzhishui.html', locals())
	return render(request, 'zengzhishui.html', locals())