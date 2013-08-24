#!/usr/bin/python

import math

left=lambda i:2*i+1
right=lambda i:2*i+2
parent=lambda i:i/2
heap_length=0

def max_heapify(A,i):
	largest=i
	lefti=left(i)
	righti=right(i)

	if(lefti<heap_length):
		if(A[i]<A[lefti]):
			largest=lefti
	
	if(righti<heap_length):
		if(A[largest]<A[righti]):
			largest=righti
	
	if(largest != i):
		# swap A[i] and A[largest]
		temp = A[i]
		A[i] = A[largest]
		A[largest] = temp
		max_heapify(A,largest)

def build_max_heap(A):
	for i in range(int(math.floor(len(A)/2))-1,-1,-1):
		max_heapify(A,i)

def heap_sort(A):
	global heap_length
	build_max_heap(A)
	for i in range(len(A)-1,0,-1):
		#exchange ith element with root
		temp = A[i]
		A[i] = A[0]
		A[0] = temp
		heap_length = heap_length-1
		max_heapify(A,0)

def main():
	A=[int(a) for a in raw_input().split(" ")]
	global heap_length
	heap_length=len(A)
	heap_sort(A)
	print A

if __name__=="__main__":
	main()
