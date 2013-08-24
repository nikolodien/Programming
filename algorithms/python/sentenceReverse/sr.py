#!/usr/bin/python

def reverse(start,end):
	for i in range(start,start+(end-start)/2+1):
		#swap the two characters
		temp=sentence[i]
		sentence[i]=sentence[start+end-i]
		sentence[start+end-i]=temp

sentence=list(raw_input())
reverse(0,len(sentence)-1)
i=0
while(i<len(sentence)):
	j=i
	while(j<len(sentence)):
		if(sentence[j]==' '):
			break
		j=j+1
	reverse(i,j-1)
	i=j+1

for i in range(0,len(sentence)):
	print sentence[i],
