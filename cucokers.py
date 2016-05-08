#!/usr/bin/python
import re, sys
from optparse import OptionParser

def select_mode(options):
	if options.create_database:
		return r"CREATE DATABASE"
	elif options.create_table:
		return r"CREATE TABLE"
	elif options.create_view:
		return r"CREATE.+VIEW"
	elif options.insert_table:
		return r"INSERT INTO.+"
	else:
		return ""


def main():

	parser = OptionParser()
	parser.add_option("", "--src", dest="src",
	                  help="file src", metavar="FILE")

	parser.add_option("", "--dest", dest="dst",
	                  help="file dest", metavar="FILE")

	parser.add_option("", "--i-table",
	                  action="store_true", 
	                  dest="insert_table", default=False,
	                  help="insert table sql query")

	parser.add_option("", "--c-table",
	                  action="store_true", 
	                  dest="create_table", default=False,
	                  help="insert table sql query")

	parser.add_option("", "--c-database",
	                  action="store_true", 
	                  dest="create_database", default=False,
	                  help="create database sql query")

	parser.add_option("", "--c-view",
	                  action="store_true", 
	                  dest="create_view", default=False,
	                  help="create view sql query")


	(options, args) = parser.parse_args()
	
	in_file = open(options.src, 'r')
	text_to_split = in_file.read();
	filter_text = text_to_split.split(';')

	out_file = open(options.dst, 'w')

	if len(sys.argv) < 3:
		print('arg < 3')
	else:
		pattern_reg = select_mode(options)
		if pattern_reg != '':
			pattern = re.compile(pattern_reg)
			for x in filter_text:
				if pattern.search(x):
					out_file.write(x+';')
					print(x+';')	

	print('\n\n\n\n\n\nfinished !')
	print('cucokers v1 by Moch Deden')

if __name__ == '__main__':
	main()
	
