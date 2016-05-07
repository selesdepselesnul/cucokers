#!/usr/bin/python
import re, sys

def select_mode(mode):
	if mode == '--database':
		return 'CREATE DATABASE'
	elif mode == '--table':
		return 'CREATE TABLE'
	else:
		return ''


mode = sys.argv[1]
source = sys.argv[2]
dest = sys.argv[3]

in_file = open(source, 'r')
text_to_split = in_file.read();
filter_text = text_to_split.split(';')

out_file = open(dest, 'w')

if len(sys.argv) < 3:
	print('arg < 3')
else:
	if select_mode(mode) != '':
		for x in filter_text:
			if select_mode(mode) in x:
				print(x+';')


	
	
