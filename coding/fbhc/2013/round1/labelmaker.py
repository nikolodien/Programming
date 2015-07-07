#!/usr/bin/python

T=input()
for case in range(1,T+1):
	L,N=raw_input().split(" ")
	N=int(N)
	powers={}
	powers[0]=1
	prevc,count,power=0,0,1
	
	while(N>count):
		powers[power]=powers[power-1]*len(L)
		prevc=count
		count=count+powers[power]
		power=power+1

	power=power-1	
	count=prevc
	label=""
	while(True):
		power,times=power-1,-1
		while(N>count and power>-1):
			prevc=count
			count=count+powers[power]
			times=times+1
		count=prevc
		if(times==-1):
			break
		label=label+L[times]
	print "Case #"+str(case)+": "+label
