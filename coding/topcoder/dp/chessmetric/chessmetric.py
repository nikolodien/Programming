#!/bin/usr/python

def updatefrom(cell,offset):
	i,j=cell[0],cell[1]
	# single moves
	# horizontal moves
	if((i-1)>=0):	cells[i-1][j],plto[i-1][j],ancestor[i-1][j]=cells[i-1][j]+cells[i][j]+offset,plto[i][j]+1,(-1,-1)
	if((i+1)<size):	cells[i+1][j],plto[i+1][j],ancestor[i+1][j]=cells[i+1][j]+cells[i][j]+offset,plto[i][j]+1,(-1,-1)
	# vertical moves
	if((j-1)>=0):	cells[i][j-1],plto[i][j-1],ancestor[i][j-1]=cells[i][j-1]+cells[i][j]+offset,plto[i][j]+1,(-1,-1)
	if((j+1)<size):	cells[i][j+1],plto[i][j+1],ancestor[i][j+1]=cells[i][j+1]+cells[i][j]+offset,plto[i][j]+1,(-1,-1)
	# diagonal moves
	if((i-1)>=0 and (j-1)>=0):	cells[i-1][j-1],plto[i-1][j-1],ancestor[i-1][j-1]=cells[i-1][j-1]+cells[i][j]+offset,plto[i][j]+1,(-1,-1)
	if((i+1)<size and (j+1)<size):	cells[i+1][j+1],plto[i+1][j+1],ancestor[i+1][j+1]=cells[i+1][j+1]+cells[i][j]+offset,plto[i][j]+1,(-1,-1)
	if((i-1)>=0 and (j+1)<size):	cells[i-1][j+1],plto[i-1][j+1],ancestor[i-1][j+1]=cells[i-1][j+1]+cells[i][j]+offset,plto[i][j]+1,(-1,-1)
	if((i+1)<size and (j-1)>=0):	cells[i+1][j-1],plto[i+1][j-1],ancestor[i+1][j-1]=cells[i+1][j-1]+cells[i][j]+offset,plto[i][j]+1,(-1,-1)
	# knight moves
	if((i-2)>=0 and (j-1)>=0):	cells[i-2][j-1],plto[i-2][j-1],ancestor[i-2][j-1]=cells[i-2][j-1]+cells[i][j]+offset,plto[i][j]+1,(-1,-1)
	if((i-2)>=0 and (j+1)<size):	cells[i-2][j+1],plto[i-2][j+1],ancestor[i-2][j+1]=cells[i-2][j+1]+cells[i][j]+offset,plto[i][j]+1,(-1,-1)
	if((i+2)<size and (j-1)>=0):	cells[i+2][j-1],plto[i+2][j-1],ancestor[i+2][j-1]=cells[i+2][j-1]+cells[i][j]+offset,plto[i][j]+1,(-1,-1)
	if((i+2)<size and (j+1)<size):	cells[i+2][j+1],plto[i+2][j+1],ancestor[i+2][j+1]=cells[i+2][j+1]+cells[i][j]+offset,plto[i][j]+1,(-1,-1)

	if((i-1)>=0 and (j-2)>=0):	cells[i-1][j-2],plto[i-1][j-2],ancestor[i-1][j-2]=cells[i-1][j-2]+cells[i][j]+offset,plto[i][j]+1,(-1,-1)
	if((i-1)>=0 and (j+2)<size):	cells[i-1][j+2],plto[i-1][j+2],ancestor[i-1][j+2]=cells[i-1][j+2]+cells[i][j]+offset,plto[i][j]+1,(-1,-1)
	if((i+1)<size and (j-2)>=0):	cells[i+1][j-2],plto[i+1][j-2],ancestor[i+1][j-2]=cells[i+1][j-2]+cells[i][j]+offset,plto[i][j]+1,(-1,-1)
	if((i+1)<size and (j+2)<size):	cells[i+1][j+2],plto[i+1][j+2],ancestor[i+1][j+2]=cells[i+1][j+2]+cells[i][j]+offset,plto[i][j]+1,(-1,-1)


def updateto(cell,length):
	i,j=cell[0],cell[1]
	# single moves
	# horizontal moves
	if((i-1)>=0 and plto[i-1][j]==length):	cells[i][j],plto[i][j],ancestor[i][j]=cells[i-1][j]+cells[i][j],plto[i-1][j]+1,(i-1,j)
	if((i+1)<size and plto[i+1][j]==length):	cells[i][j],plto[i][j],ancestor[i][j]=cells[i+1][j]+cells[i][j],plto[i+1][j]+1,(i+1,j)
	# vertical moves
	if((j-1)>=0 and plto[i][j-1]==length):	cells[i][j],plto[i][j],ancestor[i][j]=cells[i][j-1]+cells[i][j],plto[i][j-1]+1,(i,j-1)
	if((j+1)<size and plto[i][j+1]==length):	cells[i][j],plto[i][j],ancestor[i][j]=cells[i][j+1]+cells[i][j],plto[i][j+1]+1,(i,j+1)
	# diagonal moves
	if((i-1)>=0 and (j-1)>=0 and plto[i-1][j-1]==length):
		cells[i][j],plto[i][j],ancestor[i][j]=cells[i-1][j-1]+cells[i][j],plto[i-1][j-1]+1,(i-1,j-1)
	if((i+1)<size and (j+1)<size and plto[i+1][j+1]==length):
		cells[i][j],plto[i][j],ancestor[i][j]=cells[i+1][j+1]+cells[i][j],plto[i+1][j+1]+1,(i+1,j+1)
	if((i-1)>=0 and (j+1)<size and plto[i-1][j+1]==length):
		cells[i][j],plto[i][j],ancestor[i][j]=cells[i-1][j+1]+cells[i][j],plto[i-1][j+1]+1,(i-1,j+1)
	if((i+1)<size and (j-1)>=0 and plto[i+1][j-1]==length):
		cells[i][j],plto[i][j],ancestor[i][j]=cells[i+1][j-1]+cells[i][j],plto[i+1][j-1]+1,(i+1,j-1)
	# knight moves
	if((i-2)>=0 and (j-1)>=0 and plto[i-2][j-1]==length):
		cells[i][j],plto[i][j],ancestor[i][j]=cells[i-2][j-1]+cells[i][j],plto[i-2][j-1]+1,(i-2,j-1)
	if((i-2)>=0 and (j+1)<size and plto[i-2][j+1]==length):
		cells[i][j],plto[i][j],ancestor[i][j]=cells[i-2][j+1]+cells[i][j],plto[i-2][j+1]+1,(i-2,j+1)
	if((i+2)<size and (j-1)>=0 and plto[i+2][j-1]==length):
		cells[i][j],plto[i][j],ancestor[i][j]=cells[i+2][j-1]+cells[i][j],plto[i+2][j-1]+1,(i+2,j-1)
	if((i+2)<size and (j+1)<size and plto[i+2][j+1]==length):
		cells[i][j],plto[i][j],ancestor[i][j]=cells[i+2][j+1]+cells[i][j],plto[i+2][j+1]+1,(i+2,j+1)

	if((i-1)>=0 and (j-2)>=0 and plto[i-1][j-2]==length):
		cells[i][j],plto[i][j],ancestor[i][j]=cells[i-1][j-2]+cells[i][j],plto[i-1][j-2]+1,(i-1,j-2)
	if((i-1)>=0 and (j+2)<size and plto[i-1][j+2]==length):
		cells[i][j],plto[i][j],ancestor[i][j]=cells[i-1][j+2]+cells[i][j],plto[i-1][j+2]+1,(i-1,j+2)
	if((i+1)<size and (j-2)>=0 and plto[i+1][j-2]==length):
		cells[i][j],plto[i][j],ancestor[i][j]=cells[i+1][j-2]+cells[i][j],plto[i+1][j-2]+1,(i+1,j-2)
	if((i+1)<size and (j+2)<size and plto[i+1][j+2]==length):
		cells[i][j],plto[i][j],ancestor[i][j]=cells[i+1][j+2]+cells[i][j],plto[i+1][j+2]+1,(i+1,j+2)

def display():
	print
	for i in range(0,size):
		print cells[i]
	print
	for i in range(0,size):
		print plto[i]
	print
	for i in range(0,size):
		print ancestor[i]
	print

T=int(raw_input())
while(T>0):
	size=int(raw_input())
	start=raw_input()
	start=(int(start[1]),int(start[3]))
	end=raw_input()
	end=(int(end[1]),int(end[3]))
	moves=int(raw_input())
	
	# Initialize the data structures
	cells,plto,ancestor=[],[],[]
	for i in range(0,size):
		cells.append([0]*size)
		plto.append([0]*size)
		ancestor.append([(-1,-1)]*size)

	# Update all cells reachable from the start cell
	updatefrom(start,1)

	# Update all cells
	for itr in range(0,moves-2):
		for i in range(0,size):
			for j in range(0,size):
				#if(not ((i==start[0] and j==start[1]) or (i==end[0] and j==end[1]))):
				updateto((i,j),itr+1)

	# now update end position
	if(moves>1):
		updateto(end,moves-1)	

	print display()
	# print the result
	print cells[end[0]][end[1]],plto[end[0]][end[1]]

	T=T-1
