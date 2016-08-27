#!/usr/bin/python

import random

def kthSmallest(array, p, r, i):
	if p==r:
		return array[p]
	else:
		q = randomPartition(array, p, r)
		k = q-p+1
		if i==k:
			return array[q]
		elif i<k:
			return kthSmallest(array,p,q-1,i)
		else:
			return kthSmallest(array,q+1,r,i-k)

def randomPartition(array, p, r):
	# select a random pivot
	pivot = p + int((r-p)*random.random())
	array[pivot],array[r] = array[r],array[pivot]
	# Now perform the usual partition
	i,pivot = p-1,array[r]
	for j in range(p,r):
		if array[j]<pivot:
			i = i + 1
			array[i],array[j]=array[j],array[i]
	# Place the pivot at i + 1
	array[i+1],array[r] = pivot,array[i+1]
	return i+1

array = [5,6,7,1,3,0,4,8,19]
print array
print "K = ",
k = input()
element = kthSmallest(array, 0, len(array)-1, k)
print str(k) + "th Smallest = ",str(element)
