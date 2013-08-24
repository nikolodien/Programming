#!/usr/bin/python

import math
import sys

left=lambda i:2*i+1
right=lambda i:2*i+2
parent=lambda i:i/2
heap_length=0
MIN_VAL=-sys.maxint-1

def max_heapify(A,i):
	largest=i
	lefti=left(i)
	right=right(i)
	if(lefti<heap_length):
		if(A[largest]<A[lefti]):
			largest=lefti
	if(righti<heap_length):
		if(A[largest]<A[righti]):
			largest=righti
	if(largest!=i):
		# Swap the largest with the root
		temp=A[largest]
		A[largest]=A[i]
		A[i]=tmp
		max_heapify(A,largest)

def heap_extract_max(A):
	# root is the max element
	global heap_length
	max=A[0]
	A[0]=A[heap_length-1]
	heap_length=heap_length-1
	max_heapify(A,0)

def increase_key(A,val,i):
	if(A[i]<val):
		A[i]=val
		# Now we need to maintain the heap property
		while(i>0):
			parenti=parent(i)
			if(A[i]>A[parenti]):
				# swap parenti with i
				tmp=A[i]
				A[i]=A[parenti]
				A[parenti]=tmp
				i=parenti
			else:
				break

def insert_key(A,key):
	global heap_length
	A.append(MIN_VAL)
	heap_length=heap_length+1
	increase_key(A,key,heap_length-1)

def main():
	A=[]
	for key in [int(a) for a in raw_input().split(" ")]:
		insert_key(A,key)
	print A

if __name__=="__main__":
	main()
