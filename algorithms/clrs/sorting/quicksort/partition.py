#!/usr/bin/python

array = input()
p,r = 0,len(array)-1

i,j,count= -1,0,0

x = array[r] #pivot

print "Basic partitioning"

while j<r:
	if(array[j]<x):
		i = i+1
		temp = array[i]
		array[i] = array[j]
		array[j] = temp
	elif array[j]==x:
		count=count+1
	j= j + 1
	print array

# swap x with i+1

array[r]=array[i+1]
array[i+1]=x

# move all duplicate elements to the front of the array i+1..r

print "advanced partitioning"

i,j=i+1,r

while j>i+count:
	if array[j]==x:
		array[j]=array[j-1]
	j = j-1

while count>0:
	i,count=i+1,count-1
	array[i]=x

print array

# return i+1,i+count
