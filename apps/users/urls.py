#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Nice... on '2017/3/9 10:43'
from django.conf.urls import url

from .views import LoginView,IndexView

urlpatterns = [
	# 个人信息
	url(r'^login/$', LoginView.as_view(), name="login"),
	url(r'^index/$', IndexView.as_view(), name="index"),
 
]