#!/usr/bin/python

T=input()
for case in range(1,T+1):
	N,K,C=map(int,raw_input().split(" "))
	P=0
	if(N>K):
		P=C+(N-K)
	else:
		P=C
	print "Case #"+str(case)+": "+str(P)
