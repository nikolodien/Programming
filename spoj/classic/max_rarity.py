#!/usr/bin/python

n=int(raw_input())
prev=[-1]*n
length=[1]*n
a=map(lambda x:int(x),raw_input().split(" "))

ops=0

max=0;
for i in xrange(1,n):
	if(a[i-1] != a[i]):
		for j in xrange(length[i-1],0,-1):
			ops=ops+1
			if(a[i] not in a[(i-j):i]):
				length[i]=j+1;
				prev[i]=i-1;
				break;
		if(length[i]>max):
			max=length[i];

print max
print "No of operations:"+str(ops)
