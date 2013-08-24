#!/usr/bin/python

def minor(i,j,Matrix):
	return [[Matrix[row][col] for col in filter(lambda x:x!=j,range(0,len(Matrix)))] for row in range(i+1,len(Matrix))]

def det(Matrix):
	if len(Matrix) == 2:
		return Matrix[0][0]*Matrix[1][1] - Matrix[0][1]*Matrix[1][0]
	else:
		val = 0
		multiplier = 1
		for j in range(0,len(Matrix)):
			val += multiplier*Matrix[0][j]*det(minor(0,j,Matrix))
			multiplier = multiplier*(-1)
		return val

T = int(raw_input())

while T>0:
	N = int(raw_input())
	M = []
	for i in range(0,N):
		M.append(map(lambda x:int(x),list(raw_input())))
	P = int(raw_input())
	
	# Read the favourite edges and remove them from the graph
	while P>0:
		edge = map(lambda x:int(x),raw_input().split(" "))
		M[edge[0]-1][edge[1]-1] = 0
		M[edge[1]-1][edge[0]-1] = 0
		P = P - 1
	
	# Now calculate the Degree of each node
	D = []
	for i in range(0,N):
		D.append([0]*N)
		D[i][i] = reduce(lambda x,y:x+y,M[i])
	
	# Take difference of Adjacency and Degree matrix
	L = []
	for i in range(0,N):
		L.append([0]*N)
		for j in range(0,N):
			L[i][j] = D[i][j] - M[i][j]
	
	# Calculatate determinant of any minor
	print det(minor(0,0,L))	
	
	T = T-1
