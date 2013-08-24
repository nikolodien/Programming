#!/usr/bin/python

def evaluate(string,base):
	val=0;
	power=1
	for i in range(len(string)-1,-1,-1):
		val=string[i]*power+val
		power=power*base
	return val

T=input()
while(T>0):
	string=list(raw_input())
	codemap={}
	maxnum=1
	numspresent=[1]
	codemap[string[0]]=1
	if(len(string)>1):
		for i in range(1,len(string)):
			if string[i] not in codemap:
				for j in range(0,maxnum):
					if j not in numspresent:
						codemap[string[i]]=j
						numspresent.append(j)
			if string[i] not in codemap:
				maxnum=maxnum+1
				codemap[string[i]]=maxnum
				numspresent.append(maxnum)
	print evaluate(map(lambda x:codemap[x],string),maxnum+1)
	T=T-1
