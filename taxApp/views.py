from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.template import loader, Template
import datetime
from taxApp.getdata.reginf import GetInf
import time
import json

from taxApp.getdata.input_data_class import InputDataClass
from taxApp.getdata import getData

from taxApp.models import Zengzhishui
from taxApp.models import Biangen
from taxApp.forms import TableinfForm


def hello(request):
	user_list=User.objects.all()
	return render(request, 'table.html',locals())

def add_publisher(request):
	return render(request, 'add_publisher.html', locals())
def table(request):
	user=User.objects.all()
	return redirect(request,'table.html',locals())
def login(request):
	global getinf
	getinf = GetInf("http://dzswj.szgs.gov.cn/BsfwtWeb/apps/views/login/login.html")
	global driver
	driver = getinf.openbrowser()
	time.sleep(2)
	driver = getinf.input_infos(driver)
	time.sleep(1)
	yzm64,info = getinf.get_yzm64_and_save(driver, './static/img/yzm.jpg')
	return render(request,'login.html',locals())
def index(request):
	# if request.method == "POST":
	username = request.POST.get('username')
	password=request.POST.get('password')
	getinf.input_user_passwd(driver,username,password)
	aa=HttpRequest.get_full_path(request)
	bb=aa.split("?,")[1]
	cc = [(int(x),int(y)) for x,y in [x.replace(')','').replace('(','').split(',') for x in bb.split('),(')]]
	global driver1
	driver1=getinf.click_validation(driver,cc)
	time.sleep(2)
	if getinf.check_passed(driver1):
		driver1.find_element_by_xpath('//*[@id="login-form"]/div[5]/a').click()
		time.sleep(3)
		if driver1.current_url=="http://dzswj.szgs.gov.cn/BsfwtWeb/apps/views/login/login.html":
			return HttpResponse("登录失败")
		else:
			return render(request,'index.html',locals())
	else:
		return HttpResponse("验证码错误")

def chaxun(request):
	return render(request,'chaxun.html',locals())

def fapiao(request):
	return render(request,'fapiao.html',locals())
def banshui(request):
	return render(request,'banshui.html',locals())
def taxinf(request):
	autoslide = InputDataClass('you', driver1)
	info_data_gs=getData.get_data_gs(autoslide)
	info_data_ds = getData.get_data_ds(autoslide)
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
def biangen(request):
    if request.method == "POST":
        name1 = request.POST['taxname']
        taxnum = request.POST['taxnum']
        Biangen.objects.create(
            taxname=name1,
            taxnum=taxnum
        )
        return HttpResponse("添加信息成功！")
    else:
        return render(request, 'biangen.html', locals())
    return render(request, 'biangen.html', locals())
def table_somename(request):
    if request.method == "POST":
        name1 = request.POST['taxname']
        taxnum = request.POST['taxnum']
        # 验证。。。
        Tableinf.objects.create(
            taxname=name1,
            taxnum=taxnum
        )
        return HttpResponse("添加信息成功！")
    else:
        publisher_form = TableinfForm()
    return render(request, 'table_somename.html', locals())