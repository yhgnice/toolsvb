#!encoding:utf-8

import xadmin
 
from models import HostList,GroupHost
 

class HostListAdmin(object):
	list_display = ['f_host_id', 'f_host_domain', 'f_host_lan', 'f_host_wan', 'host_context']
	search_fields = ['f_host_id', 'f_host_domain', 'f_host_lan', 'f_host_wan', 'host_context']
	list_filter =['f_host_id', 'f_host_domain', 'f_host_lan', 'f_host_wan', 'host_context']
	model_icon = 'fa fa-desktop'

class GroupHostAdmin(object):
	list_display = ['f_group_id', 'f_group_name', 'group_context',  ]
	search_fields = ['f_group_id', 'f_group_name', 'group_context',]
	list_filter =['f_group_id', 'f_group_name', 'group_context',]
	model_icon = 'fa fa-desktop'
 
xadmin.site.register(HostList, HostListAdmin)
xadmin.site.register(GroupHost, GroupHostAdmin)
 