#!/bin/bash

import itertools

#No of test cases
T=long(raw_input())
i=1

while i<=T:

	strings=raw_input().strip().split(" ")
	N=long(strings[0])
	K=long(strings[1])
	
	cards=map(lambda x:long(x), raw_input().strip().split(" "))
	print "Case #"+str(i)+": "+str(sum(map(max,map(set,itertools.combinations(cards,K))))%1000000007L)

	i=i+1

