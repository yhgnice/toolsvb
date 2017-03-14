#!encoding:utf-8
from django.shortcuts import render, HttpResponse
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
		all_host = HostList.objects.all()
		host_id = request.POST.get("select", 0)
		js_date = request.POST.get("js_date", 0)
		checkbox = request.POST.get("checkbox", 0)
		
		host = all_host.get(id=int(host_id)
		                    )
		
		# example  fab  --password=aj2lovets  -uroot   -H  188.188.1.159  --  "date -s '2018-9-03 12:02'"
		
		if len(js_date) != 1 and int(checkbox) != 0:
			cmd = ''' fab  --password={passwd}  -u{user}  -H {ip}  --  "date -s '{date}';pkill -9 java && /usr/local/aojianservers/gameserver/bin/startup.sh  " '''.format(
				passwd=host.f_host_pass, user=host.f_host_user, ip=host.f_host_domain, date=js_date)
		elif int(checkbox) == 1 and len(js_date) == 1:
			cmd = ''' fab  --password={passwd}  -u{user}  -H {ip}  --  "pkill -9 java && /usr/local/aojianservers/gameserver/bin/startup.sh  " '''.format(
				passwd=host.f_host_pass, user=host.f_host_user, ip=host.f_host_domain)
		else:
			cmd = ''' fab  --password={passwd}  -u{user}  -H {ip}  --  "pkill -9 java && /usr/local/aojianservers/gameserver/bin/startup.sh  " '''.format(
				passwd=host.f_host_pass, user=host.f_host_user, ip=host.f_host_domain)
		
		result = os.system(cmd)
		if result == 0:
			msg = '''<script>alert("修改成功:{0}")</script>'''.format(host.f_host_domain)
			return render(request, "tools.html", {"msg": msg, "all_host": all_host})
		# return HttpResponse('{"status":"success"}', content_type='application/json')
		else:
			return HttpResponse('{"status":"fail","msg":u"%s"}'.format(result))
	
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
