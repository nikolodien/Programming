#!/usr/bin/python

import math

def primes_sieve(limit):
	limitn = limit+1
	not_prime = [False] * limitn
	primes = []

	for i in range(2, limitn):
		if not_prime[i]:
			continue
		for f in xrange(i*2, limitn, i):
			not_prime[f] = True

		primes.append(i)

	return primes

primelist=primes_sieve(100000/2)

prime_factors=dict()
for num in xrange(2,100001):
	primeFactors=0
	if num in primelist:
		primeFactors=primeFactors+1
	limit=(num/2)+1
	for divisor in primelist:
		if(divisor<limit):
			if(num%divisor==0):
				primeFactors=primeFactors+1
		else:
			break
	prime_factors[num]=primeFactors

T=int(raw_input())

for i in xrange(1,T+1):
	input=map(lambda x:int(x),raw_input().split(" "))
	A=input[0]
	B=input[1]
	K=input[2]
	sol=0
	print "#"+str(i)
	for num in xrange(A,B+1):
		if(prime_factors.get(A)==K):
			sol=sol+1
	print sol	
