#!/usr/bin/python
import copy

def printMatrix(size,matrix):
	for i in range(0,size):
		print matrix[i]

def isConnected(size,costs):
	temp=copy.deepcopy(costs)

	for k in range(0,size):
		for i in range(0,size):
			for j in range(0,size):
				temp[i][j] = temp[i][k] or temp[k][j]
	
	tsum=0
	for i in range(0,size):
		for j in range(0,size):
			tsum=tsum+temp[i][j]
	
	if(tsum==size*size):
		return True
	return False

def atmost(val,matrix,size):
	for i in range(0,size):
		rowSum=0
		for j in range(0,size):
			rowSum=rowSum+matrix[i][j]
		if(rowSum>val):
			return False
	return True

def atleastAndAtmost(val,matrix,size):
	for i in range(0,size):
		rowSum=0,
		for j in range(0,size):
			if(not rowSum==val):
				return False
	return True

def isvalid(size,costs,mangs):
	if(isConnected(size,costs) and atmost(1,costs,size) and atmost(1,mangs,size)):
		return True
	else:
		return False

def mincost(size,costs,mangs):
	if(size<N):
		values=[]
		for i in range(size-1,size+1):
			for j in range(size-1,size+1):
				if(not i==j):
					costs[i][j]=1
					for k in range(0,size+1):
						if(mangs[i][k]==0):
							mangs[i][k]=1
							values.append(mincost(size+1,costs,mangs))
							mangs[i][k]=0
					costs[i][j]=0
		if(len(values)>0):
			return min(values)
	else:
	# Now calculate the total cost for the senate
		if(isvalid(size,costs,mangs)):
			total=0
			for i in range(0,size):
				for j in range(0,size):
					if(costs[i][j]==1):
						total=total+cost[i][j]
					if(mangs[i][j]==1):
						total=total+mang[i][j]
			return total
		else:
			return 99999

N=input()
#First read the two matrices
cost,mang,costs,mangs=[],[],[],[]
for i in range(0,N):
	cost.append(map(lambda x:int(x),raw_input().rstrip().split(" ")))
	costs.append([0]*N)
for i in range(0,N):
	mang.append(map(lambda x:int(x),raw_input().rstrip().split(" ")))
	mangs.append([0]*N)
if(N==1):
	print cost[0][0]+mang[0][0]
else:
	print mincost(1,costs,mangs)
