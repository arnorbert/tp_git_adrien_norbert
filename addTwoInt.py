#!/bin/env python

import sys

def add(a,b):
	sum = a + b
	print(sum)
try:
	a = int( sys.argv[1] )
	b = int( sys.argv[2] )
except IndexError:
	print("Error: You must give 2 numerical arguments.")
	raise (SystemExit)

add(a,b)


