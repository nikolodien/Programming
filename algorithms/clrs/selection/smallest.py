#!/usr/bin/python

MAX = 99999
secondMinimum = MAX

def recMinimum(array, i, j):
	global secondMinimum
	minimum, min1, min2 = MAX, MAX, MAX
	if i==j:
		min1 = array[i]
	elif i == j+1:
		min1, min2 = array[i], array[j]
	else:
		mid = (i+j)//2
		min1, min2 = recMinimum(array, i, mid)[0], recMinimum(array, mid+1, j)[0]
	minimum = min(min1, min2)
	secondMinimum = min(secondMinimum, min1 if min1>min2 else min2)
	return minimum, secondMinimum

array = input()
print recMinimum(array, 0 , len(array)-1)