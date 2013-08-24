#!/usr/bin/python

T = int(raw_input())

while T>0:
	N = int(raw_input())
	ls = [0]*N
	array = map(lambda x:int(x), raw_input().split(" "))
	# Find the smallest element in the array
	smallestIndex = -1
	min = 10**6
	i = 0
	while i<len(array):
		if(array[i]<=min):
			min = array[i]
			smallestIndex = i
		i = i + 1
	newArray = [0]*N
	i = 0
	while i<N:
		newArray[i] = array[smallestIndex]
		smallestIndex = (smallestIndex + 1)%N
		i = i + 1
	#Find the Longest increasing subsequence
	for i in range(0,N):
		ls[i]=1
		for j in range(0,i):
			if(newArray[i]>newArray[j]):
				ls[i] = ls[j] + 1
	largest = -1
	for i in range(0,N):
		if(largest<ls[i]):
			largest = ls[i]
	print largest
	T = T-1
