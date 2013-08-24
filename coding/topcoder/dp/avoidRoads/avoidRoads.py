#!/usr/bin/python

def inforbidden(x,y,i,j):	
	return str(x)+" "+str(y)+" "+str(i)+" "+str(j) in forbidden

n=int(raw_input())
m=int(raw_input())
forbidden=raw_input()
points=[]
for i in range(0,n+1):
	points.append([0]*(m+1))
points[0][0]=1
for i in range(0,n+1):
	for j in range(0,m+1):
		if(i>0 and not inforbidden(i-1,j,i,j)):
			points[i][j] = points[i-1][j] + points[i][j]
		if(j>0 and not inforbidden(i,j-1,i,j)):
			points[i][j] = points[i][j-1] + points[i][j]
print points[n][m]
