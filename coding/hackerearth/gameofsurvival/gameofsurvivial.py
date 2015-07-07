#!/usr/bin/bash

T=input()
while(T>0):
	N=input()
	ssh=sorted(map(int,map(lambda x:x.strip(),raw_input().strip().split(" "))),reverse=True)
	ast=sorted(map(int,map(lambda x:x.strip(),raw_input().strip().split(" "))),reverse=True)
	possible=True
	for i in range(0,len(ssh)):
		if(ast[i]<ssh[i]):
			continue
		else:
			possible=False
			break;
	if(possible):
		print "YES"
	else:
		print "NO"
	T=T-1
