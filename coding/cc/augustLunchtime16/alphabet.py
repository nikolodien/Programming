#!/usr/bin/python

readable = {}
for char in list(raw_input()):
	readable[char] = True

N = input()

for i in range(0, N):
	canRead = True
	for char in list(raw_input()):
		if not char in readable:
			canRead = False
			break;
	if canRead:
		print "Yes"
	else:
		print "No"