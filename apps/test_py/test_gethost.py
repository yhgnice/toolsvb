#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Nice... on '2017/3/7 18:01'

import argparse

try:
	import json
except ImportError:
	import simplejson as json

'''这里是模拟数据，工作上一般该数据都是从数据库或者缓存中读取的'''
'''
mockData = {
	"webservers": {
		"hosts": ["192.168.1.65"],
		"vars": {
			"http_port": 8888,
			"max_clients": 789
		}
	},
	
	"databases": {
		"hosts": ["192.168.1.65"],
		"vars": {
			"action": "Restart MySQL server."
		}
	}
}
'''
'''模拟数据结束'''


def ghosts(hostfile='c:\\lists'):
	try:
		with open(hostfile) as f:
			lists = []
			for hosts in f.readlines():
				if hosts.split()[1] not in lists:
					lists.append(hosts.split()[1])
			return {"nginx": {"hosts": lists, "vers": 'hehe - vars'}}
	except Exception, e:
		print  e


def getList():
	'''get list hosts group'''
	print json.dumps(ghosts(),indent=4, sort_keys=False)


def getVars(host):
	'''Get variables about a specific host'''
	print json.dumps(ghosts[host]["vars"])


if __name__ == "__main__":
	
	parser = argparse.ArgumentParser()
	parser.add_argument('--list', action='store_true', dest='list', help='get all hosts')
	parser.add_argument('--host', action='store', dest='host', help='get all hosts')
	args = parser.parse_args()
	
	if args.list:
		getList()
	
	if args.host:
		getVars(args.host)
