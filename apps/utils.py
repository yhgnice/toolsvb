#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Nice... on '2017/3/10 10:16'

import sys

from fabric.api import *

ip = sys.argv[1]
user = sys.argv[2]
port = sys.argv[3]
paswd  = sys.argv[4]
 
 
host = "{user}@{ip}".format(user=user,ip=ip)
paswds  = "{user}@{ip}:{port}:'{paswd}'".format(user=user,ip=ip,port=port,paswd=paswd)
 

print host
print paswds
# env.hosts = ['{hosts}'].format(hosts=host)
# env.passwords = {'{xxxx}'}.format(xxxx=paswds)


if __name__ == '__main__':
	pass
