#!/usr/bin/python

import sys


def deexcelate(items):
	return list(filter(lambda item: len(item)>0 and item != '\x00', items))

def readclipboard_Cygwin():
	clip = open('/dev/clipboard', 'r')
	data = clip.readlines()
	clip.close()
	return deexcelate(data)

def writeclipboard_Cygwin(data):
	clip = open('/dev/clipboard', 'w')
	clip.write(data)
	clip.close()

def readclipboard_win32():
	win32clipboard.OpenClipboard()
	formats = [win32clipboard.CF_TEXT, win32clipboard.CF_UNICODETEXT, win32clipboard.CF_OEMTEXT, win32clipboard.CF_DSPTEXT]
	format = win32clipboard.GetPriorityClipboardFormat(formats)
	if format == -1:
		raise Exception('clipboard empty')
	if format == None:
		raise Exception('no text on clipboard. format = {format}'.format(format=format))
	data = win32clipboard.GetClipboardData(format)
	win32clipboard.CloseClipboard()
	return deexcelate(data.decode('utf-8').strip().split('\n')) # utf-8 encoding is probably not appropriate for all formats, but this application only places ASCII/utf-8 anyway, so fugeddaboudit

def writeclipboard_win32(data):
	win32clipboard.OpenClipboard()
	win32clipboard.EmptyClipboard()
	win32clipboard.SetClipboardText(data, win32clipboard.CF_TEXT)
	win32clipboard.CloseClipboard()

if sys.platform == 'cygwin':
	readclipboard, writeclipboard = readclipboard_Cygwin, writeclipboard_Cygwin
elif sys.platform == 'win32':
	import win32clipboard
	readclipboard, writeclipboard = readclipboard_win32, writeclipboard_win32

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
	}
header = '''var data = {{
'''

footer = '''}}'''

format = '''{t}Util.mkPair("{valuationid}", {version}),
'''
	
# now that we've got all that settled
writeclipboard(process(readclipboard(), format, header, footer, meta))
