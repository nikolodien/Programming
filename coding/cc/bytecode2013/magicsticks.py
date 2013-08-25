#!/usr/bin/python

def getcount(key,i):
	if(i==len(sticks)):
		return 0
	if key in counts:
		return counts[key]
	else:
		count=0
		if key in sticklist:
			count=1
			for subkey in xrange(key+1,key+sticks[key]):
				count = min(count + getcount(subkey,i+1),len(sticks))
				print subkey,count
			counts[key] = count
		return count

i=4
T=input()
counts={}
sticks={}
sticklist=[]
while(T>0):
	N=input()
	while(N>0):
		pair=tuple(map(int,raw_input().split(" ")))
		sticks[pair[0]]=pair[1]
		sticklist.append(pair[0])
		N=N-1
	for key in sticklist:
		print getcount(key,0),
	counts.clear()
	sticks.clear()
	sticklist=[]
	print
	T=T-1
