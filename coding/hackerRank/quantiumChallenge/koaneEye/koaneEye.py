#!/usr/bin/python

inp=[]
for i in range(0,6):
	inp.append(list(raw_input()))
for i in range(5,-1,-1):
	print inp[i][2]+inp[i][1]+inp[i][0]
