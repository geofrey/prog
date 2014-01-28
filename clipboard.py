import sys

def readclipboard_Cygwin():
	clip = open('/dev/clipboard', 'r')
	data = clip.readlines()
	clip.close()
	return data

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
	return data.decode('utf-8').strip().split('\n') # utf-8 encoding is probably not appropriate for all formats, but this application only places ASCII/utf-8 anyway, so fugeddaboudit

def writeclipboard_win32(data):
	win32clipboard.OpenClipboard()
	win32clipboard.EmptyClipboard()
	win32clipboard.SetClipboardText(data, win32clipboard.CF_TEXT)
	win32clipboard.CloseClipboard()

global readclipboard
global writeclipboard
readclipboard, writeclipboard = None, None

if sys.platform == 'cygwin':
	readclipboard, writeclipboard = readclipboard_Cygwin, writeclipboard_Cygwin
elif sys.platform == 'win32':
	import win32clipboard
	readclipboard, writeclipboard = readclipboard_win32, writeclipboard_win32

