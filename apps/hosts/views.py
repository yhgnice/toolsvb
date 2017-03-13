#!encoding:utf-8
from django.shortcuts import render,HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.core.urlresolvers import reverse

from hosts.models import HostList

import os
import sys


# Create your views here.



class RebootServices(View):
	def get(self, request):
		all_host = HostList.objects.all()
		return render(request, "tools.html", {'all_host': all_host})
 
	def post(self, request):
		host_id = request.POST.get("select",0)
		js_date = request.POST.get("js_date",0)
		host = HostList.objects.filter(id=int(host_id))
 
		
		# cmd = "fab -f"
		# os.system()
		context = "%s,%s,%s" % (host,host_id,js_date)
		return HttpResponse(context)
		# return HttpResponse('{"status":"fail","msg":"用户未登录"}', content_type='application/json')
		pass
		'''
		def post(self, request):
		user_ask = UserAskForm(request.POST)
		if user_ask.is_valid():
			user_ask = user_ask.save(commit=True)
			return HttpResponse('{"status":"success"}', content_type='application/json')
		else:
			return HttpResponse('{"status":"fail","msg":u"请填写正确信息"}')
		'''
		# check_id = request.POST.get("check_id", 0)
		# name = request.POST.get("name", "")
		# return  HttpResponse(check_id)
		#
 