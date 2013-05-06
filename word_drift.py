#!/usr/bin/python

import sys
import os
import subprocess

bedugging = os.getenv('BEDUGGING') == 'yes'

def dprint(message):
	global bedugging
	if bedugging:
		print(message)

def mutate(word):
	global wordfile
	word_length = len(word)
	wordlist = []
	
	# change a character, add a character, remove a character
	alterator = lambda expr: lambda char: expr.replace('?', char)
	alterations = map(alterator, ['[^?]', '', '.?'])

	for i in range(0, len(word))
		for alteration in alterations:
			wordlist.append(word[:i]+alteration(word[i])+word[i+1:])
	wordlist.append(word+'.') # because the infixing doesn't go to 11
	
	for test in wordlist:
		dprint('\t{0}'.format(test))
		subprocess.Popen(['grep', '-E', '-w', test, wordfile]).wait()

# get args
args = sys.argv[1:]
words = []
wordfile = '/usr/share/dict/words'
while len(args) > 0:
	word = args.pop(0)
	if word == '-d':
		wordfile = args.pop(0)
	else:
		words.append(word)

dprint('dictionary: {0}'.format(wordfile))

if len(words) > 0:
	dprint('{0} words from command line'.format(len(words)))
	for word in words:
		mutate(word)
else:
	dprint('interactive mode')
	word = sys.stdin.readline()
	while(len(word) > 0):
		mutate(word)
		word = sys.stdin.readline()



