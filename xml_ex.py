#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import xml.etree.ElementTree as ET

def parse_xml( file):
	tree = ET.parse( file)
	root = tree.getroot()
	return root


def dump_item( root, item):
	for node in root.findall( item):
		print node.text 

if __name__ == '__main__':
	root = parse_xml( sys.argv[1])
	dump_item( root, './CD/TITLE')
	dump_item( root, './/PRICE')

