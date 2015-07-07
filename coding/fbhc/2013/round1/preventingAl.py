#!/usr/bin/python

import sys

sys.setrecursionlimit(10000)

# find gcd
def gcd(num1,num2):
	if(num1<num2):
		return gcd(num2,num1)
	else:
		if(num2==0):
			return num1
		else:
			return gcd(num2,num1%num2)

# check if each pair has gcd K
def check(numbers,K):
	for i in range(0,len(numbers)):
		for j in range(i+1,len(numbers)):
			if(not gcd(numbers[i],numbers[j])==K):
				return False
	return True

def counter(numbers):
	for i in range(0,len(numbers)):
		if(numbers.count(numbers[i])>1):
			return True
	return False

def new(numbers,K):
	print numbers
	if(check(numbers,K)):
		return sum(numbers)
	elif(len(filter(lambda x:x>100,numbers))>1):
		return 100*len(numbers)
	else:
		hgcd=max(map(lambda x:gcd(x[0],x[1]),[(numbers[i],numbers[j]) for i in range(0,len(numbers)) for j in range(i+1,len(numbers))]))
		minimum=100*len(numbers)
		if(hgcd<K):
			for i in range(len(numbers)-1,-1,-1):
				val=minimum
				numbers[i]=numbers[i]+1
				if(not counter(numbers)):
					val=new(numbers,K)
				numbers[i]=numbers[i]-1
				minimum=min(val,minimum)
			for i in range(0,len(numbers)):
				val=minimum
				if(numbers[i]%hgcd==0):
					numbers[i]=numbers[i]+1
					if(not counter(numbers)):
						val=new(numbers,K)
					numbers[i]=numbers[i]-1
				minimum=min(val,minimum)
				if(sum(numbers)>=80*len(numbers)):
					break
		if(minimum==100*len(numbers)):
			return 0
		else:
			return minimum

T=input()
for case in range(1,T+1):
	N,K=map(int,raw_input().split(" "))
	numbers=sorted(map(int,raw_input().split(" ")))
	print "Case #"+str(case)+": "+str(abs(new(numbers,K)-sum(numbers)))
