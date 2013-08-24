#!/usr/bin/python

def stateprob(state,x,y,diamond):
	if(state[x+20][y]==1):
		#State is occupied
		return 0.5*diamond
	else:
		return 0

def modifystate(state):
	placed=False
	x,y=0,0
	while not placed:
		if(state[x+20][y]==0):
			state[x+20][y]=1
		else:
			# Move left or up
			if(state[x-1+20][y]==0):
				state[x-1+20][y]=1
				placed=True
			else:
				if(state[x-1+20][y+1]==0):
					state[x-1+20][y+1]=1
					placed=True
				else:
					if(state[x+20][y+1]==0):
						state[x+20][y+1]=1
						placed=True
					else:
						if(state[x+1+20][y+1]==0):
							state[x+1+20][y+1]=1
							placed=True
						else:
							if(state[x+1+20][y]==0):
								state[x+1+20][y]=1
								placed=True
							else:
								y=y+2

def probability(diamond,n,x,y,state):
	if(diamond<state):
		if(diamond==1 and x>0 and y>0):
			#Find probability at this state for x,y
			prob=stateprob(state,x,y,diamond)		
			#Modify state and call recursively
			newstate = copy.deepcopy(state)
			return prob+modifystate(state,True)
	else:
		return 0

T = int(raw_input())
for case in range(1,T+1):
	inputs=map(lambda x:int(x),raw_input().split(" "))
	N=inputs[0]
	X=inputs[1]
	Y=inputs[2]
	state=[[0]*41]*20
	p=probability(1,N,X,Y,state)	
	print "Case #"+str(case)+": " 
