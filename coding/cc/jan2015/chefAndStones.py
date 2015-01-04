#!/usr/bin/python

T=input()
for test in xrange(1,T+1):
	N,K=map(long,raw_input().split(" "))
	A=map(long,raw_input().split(" "))
	B=map(long,raw_input().split(" "))
	print max([B[i]*(K/A[i]) for i in xrange(0,len(A)) if A[i]>0])
