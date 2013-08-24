#!/usr/bin/python

params = raw_input().split(" ")
N = int(params[0])
K = int(params[1])

array=[]
newarray=['.' for i in range(0,N*N)]

n = N

while n > 0:
	array.extend([x for x in raw_input()])
	n = n - 1

# Rotation code

for i in range(0,N):
	for j in range(0,N):
		newarray[j*N + (N-i-1)] = array[i*N + j]

# Gravitation code
# Make use of insertion

for j in range(0,N):
