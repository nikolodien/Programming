#!/usr/bin/python

import math

def sol(val):
	no=0
	if(val>0 and val>=a[0]):
		# First find no of solutions of sum length
		lfs,lbs=0,length-1
		while(lfs<length and lbs>=0 and a[lfs]<=a[lbs]):
			plfs,plbs=lfs,lbs
			while(plfs<length):
				while(plbs>=0):
					taken=[0]*length
					fs,bs=0,0
					f,b=plfs,plbs
					while(f<length and b>=0 and a[f]<=a[b]):
						if(fs<val and fs+a[f]<=val and not taken[f]==1):
							fs=fs+a[f]
							taken[f]=1
						if(bs<val and bs+a[b]<=val and not taken[b]==1):
							bs=bs+a[b]
							taken[b]=1
						#print f,b,a[f],a[b],fs,bs
						f,b=f+1,b-1
					# ensure that both the sums are equal and 
					# highest value with frank is less than or
					# equal to the lowest value with bob
					if(fs==val and fs==bs):
						no=no+1
					plbs=plbs-1
				plfs=plfs+1
			lfs,lbs=lfs+1,lbs-1
		no=no+sol(val-1)
	print val,no
	return no

a=list(input())
a=sorted(a)
print a
length=len(a)
print sol(int(math.floor(sum(a)/2)))
#print sol(5)
