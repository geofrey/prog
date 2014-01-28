#!/usr/bin/python

import sys
import clipboard
from clipboard import writeclipboard

def deexcelate(items):
	return list(filter(lambda item: len(item)>0 and item != '\x00', items))
readclipboard = lambda: deexcelate(clipboard.readclipboard())

# sanity check
def quicktest():
	for teststring in ['foo', 'bar', '', 'foo\nbar', ' \t    \t\t']:
		writeclipboard(teststring)
		echo = readclipboard()
		if echo != teststring:
			raise Exception('problem - placed text {input}, got {output} back.'.format(input=teststring, output=echo))
	exit()
#quicktest()

meta = {
	'meta': 'data',
	'for': 'substitution into header and footer'
	}
header = 'stuff that goes first'
format = 'what to do with the {element}s from each row of data'
footer = '{meta} that goes last'
#PROTIP: leave these hints here and overwrite them later on down the file

def process(tabular, format, header='', footer='', meta={}):
	labels = tabular[0].strip().split('\t')
	lines = [line.strip().split('\t') for line in tabular[1:]]
	names = {}
	for index in range(len(labels)):
		names[index] = labels[index]
	#names = dict([(index, labels[index]) for index in range(len(labels))])
	# wait...isn't that the same as using the list in the first place?
	
	#rows = [dict([(names[index], line[index]) for index in range(len(line))]) for line in lines]
	rows = []
	for line in lines:
		row = {}
		for index in range(len(line)):
			row[names[index]] = line[index]
		rows.append(row)
	#print(type(tabular))
	#print(tabular)
	#print(labels)
	#print(rows)
	#for row in rows:
	#	print(dict(list(row.items())+list(meta.items())))
	return ''.join([
		header.format(**meta),
		''.join([format.format(**dict(list(row.items())+list(meta.items()))) for row in rows]),
		footer.format(**meta)
		])

meta = {
	't' : '\t',
	'sep': '&'
	}
header = '''http://web.site/form?'''

footer = ''''''

format = '''{name}{sep}{value}'''
	
# now that we've got all that settled
writeclipboard(process(readclipboard(), format, header, footer, meta))
