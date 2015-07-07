#!/usr/bin/python

N = input()
stamps = map(int,raw_input().split(" "))
if sum(stamps) == (N*(N+1))/2:
	print "YES"
else:
	print "NO"
