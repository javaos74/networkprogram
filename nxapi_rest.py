#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json 
from flask import jsonify

#aaa_str='{ "aaaUser": {"attributes": { "name": "%s", "pwd": "%s" } } }'
aaa = {
	'aaaUser' : {
		'attributes' : {
			'name': '',
			'pwd': ''
		}
	}
}

eps='http://10.72.86.53/api'

def auth(name,pwd):
	cookie = {}
	aaa['aaaUser']['attributes']['name'] = name
	aaa['aaaUser']['attributes']['pwd'] = pwd
	r = requests.post('http://10.72.86.53/api/aaaLogin.json', data=json.dumps(aaa))
	print r.text
	if r.status_code == 200:
		cookie['APIC-cookie'] = r.cookies['APIC-cookie']
	else:
		cookie['APIC-cookie'] = ''
	return cookie

def list_vlans(cookie, option=''):
	r = requests.get( '%s/mo/sys/fm/ifvlan.json%s' %(eps,option), cookies=cookie)
	if r.status_code == 200:
		print r.text

def list_bds(cookie, option=''):
	r = requests.get( '%s/mo/sys/bd.json%s' %(eps,option), cookies=cookie)
	if r.status_code == 200:
		print r.text

def show_bd(cookie, vlan, option=''):
	r = requests.get( '%s/mo/sys/bd/bd-[vlan-%s].json%s' %(eps,vlan,option), cookies=cookie)
	if r.status_code == 200:
		print r.text
	

def list_phys_intfs( cookie, option=''):
	r = requests.get('http://10.72.86.53/api/mo/sys/intf.json%s' %(option), cookies=cookie)
	if r.status_code == 200 :
		print r.text
	else:
		print r.status_code, r.text

def show_phys_intf( cookie, intf_name, option=''):
	r = requests.get('http://10.72.86.53/api/mo/sys/intf/phys-%s.json%s' %(intf_name,option), cookies=cookie)
	if r.status_code == 200 :
		print jsonify( {'resp': r.text})
	else:
		print r.status_code, r.text
	

if __name__ == '__main__':
	cookie = auth('admin', 'cisco')
	list_phys_intfs( cookie, '?query-target=subtree')
	print '-----------------------'
	show_phys_intf( cookie, '[eth1/21]')
	print '-----------------------'
	list_vlans(cookie, '?query-target=subtree')	
	print '-----------------------'
	list_bds(cookie, '?query-target=subtree')
	print '-----------------------'
	show_bd(cookie, '15', '')
	#\r = requests.get('http://10.72.86.53/api/mo/sys/intf/phys-[eth1/21].json', cookies=cookie)
	#print r.text
