#!/usr/bin/python

def na(j,i):
	if((i+1)%length==j):
		return True
	elif(prev[j]!=-1):
		return na(prev[j],i)
	else:
		return False

T=int(raw_input())
while(T>0):
	length=int(raw_input())
	a=map(lambda x:int(x),raw_input().split(" "))
	s=[]
	for num in a:
		s.append(num)
	prev=[-1]*length
	for i in xrange(0,length):
		for j in xrange(i%2,i-1):
			if(not na(j,i)): #circular
				if((s[j]+a[i])>s[i]):
					s[i]=s[j]+a[i]
					prev[i]=j
	print max(s)
	T=T-1
