#!/usr/bin/python
import math

def divisorGenerator(n):
	large_divisors = []
	for i in xrange(1, int(math.sqrt(n) + 1)):
		if n % i is 0:
			yield i
			if i is not n / i:
				large_divisors.insert(0, n / i)
	for divisor in large_divisors:
		yield divisor

T=input()
while(T>0):
	print len(filter(lambda x:str(4) in str(x) or str(7) in str(x),divisorGenerator(input())))
	T=T-1
