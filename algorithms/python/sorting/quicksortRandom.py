#!/usr/bin/python

import random

def partition(A,p,r):
	# Here we need a random seed
	pivotIndex=random.randrange(p,r+1,1)
	# exchange A[r] with the random seed generated
	temp=A[pivotIndex]
	A[pivotIndex]=A[r]
	A[r]=temp

	# Now set A[r] as the pivot
	pivot=A[r]
	i=p-1
	for j in range(p,r):
		if(A[j]<pivot):
			i=i+1
			# Exchange A[i] with A[j]
			temp=A[i]
			A[i]=A[j]
			A[j]=temp
	# Now exchange A[i+1] with pivot
	A[r]=A[i+1]
	A[i+1]=pivot			
	return i+1

def quicksort(A,p,r):
	q=partition(A,p,r)
	if(q>p):
		quicksort(A,p,q-1)
	if(q<r):
		quicksort(A,q+1,r)

def main():
	A=[int(a) for a in raw_input().split(" ")]
	quicksort(A,0,len(A)-1)
	print A

if __name__=="__main__":
	main()
