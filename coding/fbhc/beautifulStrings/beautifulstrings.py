#!/usr/bin/python
import re

M=int(raw_input())
i=1
p=re.compile('[a-zA-Z]')
while i<=M:
	string=raw_input()	
	string=string.upper()	
	charDict={}
	for ch in string:
		if(p.match(ch)!=None):
			if ch in charDict:
				charDict[ch] = charDict[ch]+1
			else:
				charDict[ch]=1
	sortedList=sorted(charDict,key=charDict.get,reverse=True)
	sum=0
	multiplier=26
	for ch in sortedList:
		sum= sum + multiplier*charDict[ch]
		multiplier=multiplier-1
	print "Case #"+str(i)+": "+str(sum)
	i=i+1;
