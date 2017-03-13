#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Nice... on '2017/3/7 13:46'
import click


@click.group()
def yhg():
	pass


@click.command()
def ghosts(hostfile='c:\\lists'):
	try:
		with open(hostfile) as f:
			lists = []
			for hosts in f.readlines():
				if hosts.split()[1] not in lists:
					lists.append(hosts.split()[1])
		for Uid, Host in enumerate(lists):
			print Uid, Host
	except Exception, e:
		print  e


@click.command()
def glists(hostfile='c:\\lists'):
	try:
		with open(hostfile) as f:
			hostlists = []
			for hosts in f.readlines():
				# if hosts.split()[1] not in lists:
				hostlists.append(hosts.split())
		for Host in hostlists:
			print Host[0], Host[1]
	except Exception, e:
		print  e


yhg.add_command(ghosts)
yhg.add_command(glists)

if __name__ == '__main__':
	yhg()
