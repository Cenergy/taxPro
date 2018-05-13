"""taxPro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from taxApp import views

urlpatterns = [
    # url(r'^taxApp/$',views.hello),
    # # url(r'^test/(?P<id>\d{2})/(?P<key>\w+)/$', views.test),
    # url(r'^add_publisher/$', views.add_publisher, name='add_publisher'),
    url(r'^index/?', views.index),
    url(r'^table_somename/$', views.table_somename),
    url(r'^biangen/$', views.biangen),
    url(r'^chaxun/$', views.chaxun),
    url(r'^fapiao/$', views.fapiao),
    url(r'^taxinf/$', views.taxinf),
    url(r'^banshui/$', views.banshui),
    url(r'^zengzhishui/$', views.zengzhishui),
    url(r'^login/$', views.login),
    url(r'^', views.find),
]
