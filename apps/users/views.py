#!encoding:utf-8
from django.shortcuts import render, HttpResponseRedirect

from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse

from .forms import LoginForm


# Create your views here.


class LoginView(View):
	def get(self, request):
		return render(request, "login.html", {})
	
	def post(self, request):
		# login_form = LoginForm(request.POST)
		# if login_form.is_valid():
		user_name = request.POST.get("username", "")
		pass_word = request.POST.get("password", "")
		user = authenticate(username=user_name, password=pass_word)
		if user is not None:
			login(request, user)
			return HttpResponseRedirect('/users/index')
			# return HttpResponseRedirect(reverse('index'))
		else:
			return render(request, "login.html", {"msg": "用户名或密码错误!"})


class IndexView(View):
	def get(self, request):
		return render(request, "index.html", {})
