#!/usr/bin/python

def evaluate(permuted,pairs):
	total=0
	for pair in pairs:
		total=total+sum(permuted[pair[0]-1:pair[1]])
	return total

T=input()

while(T>0):
	nq=map(int,raw_input().split(" "))
	n,q=nq[0],nq[1]
	numbers=map(int,raw_input().split(" "))
	numbers=sorted(numbers,reverse=True)
	permuted=[0]*n
	fmap,smap={},{}
	pairs=[]
	while(q>0):
		pair=tuple(map(int,raw_input().split(" ")))
		pairs.append(pair)
		if pair[0] not in fmap:
			fmap[pair[0]]=1
		else:
			fmap[pair[0]]=fmap[pair[0]]+1
		if pair[1] not in smap:
			smap[pair[1]]=1
		else:
			smap[pair[1]]=smap[pair[1]]+1
		q=q-1
	if(n==1):
		print n*q
		continue
	rem=n
	# Get the most frequently occuring first number in the pair
	# place largest number there
	maxindex=sorted(sorted(fmap),key=fmap.get,reverse=True)[0]-1
	# print maxindex
	permuted[maxindex]=numbers[0]	
	rem=rem-1
	# Now get the least frequently occuring second number in the pair
	# place the lowest number there
	minindex=sorted(sorted(smap,reverse=True),key=smap.get,reverse=False)[0]-1		
	# print minindex
	if(minindex!=maxindex):
		permuted[minindex]=numbers[n-1]
		rem=rem-1
	# place the remaining numbers
	# print numbers,permuted
	j=1
	if(rem>0):
		i=maxindex+1
		while(i<n and rem>0):
			if(i!=minindex):
				permuted[i]=numbers[j]
				rem=rem-1
				j=j+1
			i=i+1
	# print numbers,permuted,i,j
	if(rem>0):
		i=maxindex-1
		while(i>=0 and rem>0):
			if(i!=minindex):
				permuted[i]=numbers[j]
				rem=rem-1
				j=j+1
			i=i-1
	print evaluate(permuted,pairs)
	T=T-1
