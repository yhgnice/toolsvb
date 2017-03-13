#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin


class UserProfileAdmin(UserAdmin):
	pass


class BaseSetting(object):
	enable_themes = True
	use_bootswatch = True  # 设置主题


class GlobalSettings(object):
	site_title = "Search Google"
	site_footer = "Google.lnc"
	menu_style = "accordion"  # 设置menu
 
 
 
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)