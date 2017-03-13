# encoding:utf-8
from __future__ import unicode_literals
from  datetime import datetime

from django.db import models


# Create your models here.

class GroupHost(models.Model):
	f_group_id = models.IntegerField(null=False, primary_key=True, verbose_name="平台ID")
	f_group_name = models.CharField(max_length=20, verbose_name=u"平台名称", )
	group_context = models.TextField(max_length=20, default="", verbose_name=u"描述", null=True)
	add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
	
	class Meta:
		verbose_name = u"服务器组"
		verbose_name_plural = verbose_name
	
	def __unicode__(self):
		return self.f_group_name


class HostList(models.Model):
	f_host_id = models.IntegerField(default=0, verbose_name=u"ServerID")
	f_host_domain = models.CharField(max_length=50, verbose_name=u"域名", )
	f_host_lan = models.CharField(max_length=50, verbose_name=u"IP地址")
	f_host_wan = models.CharField(max_length=50, verbose_name=u"wan_IP地址")
	f_host_port = models.IntegerField(default='22', verbose_name=u"ssh")
	f_host_pass = models.CharField(default=u'', verbose_name=u"密码", max_length=20)
	host_context = models.TextField(max_length=100, default=u'', verbose_name=u"描述信息")
	f_groups_id = models.ForeignKey(GroupHost, verbose_name=u"平台ID", null=False)
	add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
	
	class Meta:
		verbose_name = u"主机信息"
		verbose_name_plural = verbose_name
	
	def __unicode__(self):
		return self.f_host_domain
