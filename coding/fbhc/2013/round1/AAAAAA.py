#!/usr/bin/python

import sys

sys.setrecursionlimit(10000)

def sol(grid,dp,i,j,added):
	ways=0
	if(i>=0 and j>=0 and not grid[i][j]=='#'):
		if(dp[i][j]!=0):
			ways=dp[i][j]
		else:
			count=1
			one,two,three=0,0,0
			if(not added):
				#Try a upwards or a leftwards move
				#For a complete leftwords move, we need to be in the last column
				if(j==0 and i>0 and grid[i-1].count('#')==0):
					added=True
					j=len(grid[i])-1
					one=max(sol(grid,dp,i-1,prevj,False),len(grid[i])+sol(grid,dp,i-2,j,added))
				elif(i==0 and j>0 and [grid[x][j-1] for x in range(0,len(grid))].count('#')==0):
					added=True
					i=len(grid)-1
					two=max(len(grid)+sol(grid,dp,i,j-2,added),sol(grid,dp,0,j-1,added))
				else:
					three=max(sol(grid,dp,i-1,j,added),sol(grid,dp,i,j-1,added))
			else:
				three=max(sol(grid,dp,i-1,j,added),sol(grid,dp,i,j-1,added))
			ways=1+max(one,two,three)
			dp[i][j]=ways
	return ways

T=input()
for case in range(1,T+1):
	N,M=map(int,raw_input().split(" "))
	grid=[]
	dp=[]
	for i in range(0,N):
		grid.append(list(raw_input()))
		dp.append([0]*M)
	print "Case #"+str(case)+": "+str(sol(grid,dp,N-1,M-1,False))			
