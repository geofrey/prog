needle = 'hiddenmessagesletsplay'
haystack = "Here I've devised a diversion. You might believe I suddenly forgot how to spell, but that's a red herring. This clue may be of use - all the real text is missing. You won't spot a single letter unless you read between the lines. Happy puzzling!"
output = []

n = 0
h = 0

print(len(needle))
print(len(haystack))

while n < len(needle) and h < len(haystack):
	if needle[n].lower() == haystack[h].lower():
		n += 1
	else:
		output.append(haystack[h])
	h += 1
output += haystack[h:]
output = ''.join(output)

print(n)
print(h)
print(needle[n:len(needle)])
print(haystack[0:h])
print('')
print(output)
