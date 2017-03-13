#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Nice... on '2017/3/9 20:32'


from django.conf.urls import url
 
from .views import RebootServices

urlpatterns = [
	# 主机工具
	url(r'^tools/$', RebootServices.as_view(), name="tools"),

]
