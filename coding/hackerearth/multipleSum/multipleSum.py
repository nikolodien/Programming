#!/usr/bin/python

N,A,B=map(int,raw_input().strip().split(" "))
print reduce(lambda x,y:x+y,filter(lambda x:x%A==0 or x%B==0,range(1,N)))
