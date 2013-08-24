#!/usr/bin/python
T=int(raw_input())
i=0
no_op=0
while i<T:
	string=list(raw_input().strip())
	cost=0
	while len(string)>0:
		ch=string.pop()
		cost=cost+1
		try:
			string.remove(ch)
		except ValueError:
			no_op
	print cost
	i=i+1
