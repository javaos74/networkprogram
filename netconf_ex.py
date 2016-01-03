#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from ncclient import manager


def get_config(host,user,passwd):
	with manager.connect(host=host, port=22, username=user, password=passwd, 
		hostkey_verify=False, device_params={'name':'nexus'}) as m:
#		c = m.get_config(source='running').data_xml
		c = m.get(filter=('subtree', '<cmd>show running-config</cmd>')).data_xml
		with open("%s.xml" % host, 'w') as f:
			f.write(c)


if __name__ == '__main__':
	get_config('10.72.86.55','admin', sys.argv[1])