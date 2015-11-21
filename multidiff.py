import clipboard
import os
import subprocess
import sys

f = open(r'c:\dev\tools\multidiff.log', 'w')
#f = sys.stdout
def log(msg):
	f.write(msg+'\n')
	f.flush()

def opendiff(left, right):
	subprocess.Popen(['p4merge', left, right])

if len(sys.argv) == 3:
	log('two arguments!')
	if not os.path.exists(sys.argv[1]):
		log('first argument is not a path...')
		exit(1)
	if not os.path.exists(sys.argv[2]):
		log('second argument is not a path...')
		exit(1)
	opendiff(sys.argv[1], sys.argv[2])
	exit(0)

right = sys.argv[1]
log('start with {} passed in'.format(right))
if not os.path.exists(sys.argv[1]):
	log("it's not a path so quit")
	exit(1)

left = clipboard.readclipboard()[0]
log("then we find {} pasted".format(left))
if os.path.exists(left):
	log("that's a path too! launch diff tool.")
	opendiff(left, right)
	log("and clear clipboard")
	clipboard.writeclipboard('')
else:
	log("but that's not a path - put arg on the clipboard instead")
	clipboard.writeclipboard(right)

if f != sys.stdout:
	f.close()

exit(0)

#
