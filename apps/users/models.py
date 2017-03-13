#!encoding:utf-8
from __future__ import unicode_literals

from django.db import models

 

class UserProfile(models.Model):
	nick_name = models.CharField(max_length=30, verbose_name=u"匿名", default="")
	birday = models.DateField(verbose_name=u"生日", null=True, blank=True)
	gender = models.CharField(choices=(("maile", u"男"), ("female", u"女")), default="female", max_length=10)
	address = models.CharField(max_length=100, default=u"")
	mobile = models.CharField(max_length=11, null=True, blank=True)
	# image = models.ImageField(upload_to="image/%Y/%m", default=u"image/default.png", max_length=100)
	
	class Meta:
		verbose_name = u"用户信息"
		verbose_name_plural = verbose_name
	
	def __unicode__(self):
		return self.username
