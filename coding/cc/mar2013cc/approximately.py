#!/usr/bin/python

divident=103993
divisor=33102
quotient=[]

for i in range(0,10**6):
	if(divident>divisor):
		quotient.append(divident/divisor)
		divident=divident%divisor
	else:
		divident=divident*10
		if(divident>divisor):
			quotient.append(divident/divisor)
			divident=divident%divisor
		else:
			quotient.append(0)
			divident=divident

T = int(raw_input())

for i in range(0,T):
	k = int(raw_input())
	print "3"+("." if k>0 else "")+reduce(lambda x,y:x+str(y),quotient[1:(k+1)],"")

		
		
		
