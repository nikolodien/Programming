#!/usr/bin/python

height=[5,4,3,2,1]#input()
bloom=[1,5,10,15,20]#input()
wilt=[5,10,14,20,25]#input()
order=[0]*len(height)

for i in range(0,len(height)):
	for j in range(0,i):
		if(height[j]>height[i]):
			if(wilt[j]<bloom[i] or bloom[j]>wilt[i]):
				order[i]=order[j]+1
			else:
				order[i]=order[j]-1
		else:
			if(wilt[j]<bloom[i] or bloom[j]>wilt[i]):
				order[i]=order[j]-1
			else:
				order[i]=order[j]+1
# partition elements around the one having least
# value in order array

print order
