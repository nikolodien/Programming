#!/usr/bin/python

T=int(raw_input())
i=0
fibs={0:0,1:1}
correct='CORRECT'
incorrect='INCORRECT'

def powLF(n):
    if n == 1:     return (1, 1)
    L, F = powLF(n//2)
    L, F = (L**2 + 5*F**2) >> 1, L*F
    if n & 1:
        return ((L + 5*F)>>1, (L + F) >>1)
    else:
        return (L, F)

def fib(n):
    return powLF(n)[1]

while i<T:
	strings=raw_input().split(" ")
	N=long(strings[0])
	G=int(strings[1])
	M=fib(N+1)
	if G==reduce(lambda x,y:x+1 if y==1 else x, map(lambda x:int(x),list(bin(M % 1000000007))[2:])):
		print correct
	else:
		print incorrect
	i=i+1
