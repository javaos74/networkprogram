#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml
import sys


def load_employee( buf):
	emp = yaml.load( buf)
	print 'Type of emp ' + str(type(emp))
	print emp
	return emp

def print_info( emp):
	print 'name : ' + emp['name']
	print 'job : ' + emp['job']
	print 'type of foods' + str(type( emp['foods']))
	print 'foods = ' + str(emp['foods'])

if __name__ == '__main__':
	with open(sys.argv[1]) as file:
		emp = load_employee( file.read())
#		print_info(emp)
