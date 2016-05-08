#!/usr/bin/python
import re, sys
from optparse import OptionParser


def select_mode(mode):
	if mode == '--c-database':
		return r"CREATE DATABASE"
	elif mode == '--c-table':
		return r"CREATE TABLE"
	elif mode == '--c-view':
		print('c-view mode')
		return r"CREATE.+VIEW"
	elif mode == '--i-table':
		return r"INSERT INTO.+"
	else:
		return ""


def main():
	params = {
		'mode' : sys.argv[1],
		'src' : sys.argv[2],
		'dest' : sys.argv[3] 
	}

	in_file = open(params['src'], 'r')
	text_to_split = in_file.read();
	filter_text = text_to_split.split(';')

	out_file = open(params['dest'], 'w')

	if len(sys.argv) < 3:
		print('arg < 3')
	else:
		if select_mode(params['mode']) != '':
			pattern_reg = select_mode(params['mode'])
			print(pattern_reg)
			pattern = re.compile(pattern_reg)
			for x in filter_text:
				if pattern.search(x):
					out_file.write(x+';')
					print(x+';')	

	print('\n\n\n\n\n\nfinished !')
	print('cucokers v1 by Moch Deden')

if __name__ == '__main__':
	main()
	
