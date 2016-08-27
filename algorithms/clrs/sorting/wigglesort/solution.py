#!/usr/bin/python

array=input()

less=True

for i in range(0,len(array)-1):
	if less:
		if not array[i]<array[i+1]:
			array[i],array[i+1]=array[i+1],array[i]
	else:
		if not array[i]>array[i+1]:
			array[i],array[i+1]=array[i+1],array[i]
	less = not less
