#!/usr/bin/python3

#--- lib ---
import sys
import datetime

#--- func ---
def hello():
	now = datetime.datetime.now()
	print('Hello Python! (%s)' % now.strftime('%Y-%m-%d %H:%M:%S'))
	return

#--- main ---
if __name__ == '__main__':
	args = sys.argv
	print('args = %s' % args)
	hello()
