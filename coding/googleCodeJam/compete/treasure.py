#!/usr/bin/bash

T=int(raw_input())

# key with which the chest can be opened
chestkey={}
# keys found inside the chest
chestkeys={}

def createGraph(start,graph):
	#Connect this to all other chests
	for key in chestkeys[start]:
		if(start not in graph.keys()):
			graph[start] = filter(lambda x:chestkey[x]==key and not x==start,chestkey.keys())
		else:
			graph[start].extend(filter(lambda x:chestkey[x]==key and not x==start,chestkey.keys()))
	#Call this for all other chests
	subgraphs=[]
	if(start in graph.keys()):
		for chest in graph[start]:
			subgraph={}
			createGraph(chest,subgraph)
			if(len(subgraph.keys())==0):
				temp={}
				temp[chest]=None
				subgraphs.append(temp)
			else:
				subgraphs.append(subgraph)
		#Now we have all the subgraphs
		graph[start]=subgraphs	

def traverse(start,graph):
	if(graph[start]==None):
		return [start]
	subpaths=[]
	for subgraph in graph[start]:
		subpaths.append(traverse(subgraph.keys()[0],subgraph))
	path=[start]
	for subpath in subpaths:	
		path.extend(subpath)	
	return path

for case in xrange(1,T+1):
	chestkey={}
	chestkeys={}
	split=raw_input().split(" ")
	K=int(split[0])
	N=int(split[1])
	availablekeys=map(lambda x:int(x),raw_input().split(" "))
	for i in range(1,N+1):
		line=map(lambda x:int(x),raw_input().split(" "))
		k=line[0]
		n=line[1]
		chestkey[i]=k
		chestkeys[i]=[line[2+j] for j in range(0,n)]
	paths=[]
	path=[]
	for i in availablekeys:
		start=-1
		for j in chestkey.keys():
			if(chestkey[j]==i):
				start=j
				graph={}
				path.append(start)
				createGraph(start,graph)
				# Now traverse the graph
				if(len(graph.keys())>0):
					paths.append(traverse(start,graph))
	path=set(path)
	if(len(path)==N):
		paths.append(path)
	if(len(paths)>0):
		print "Case #"+str(case)+": "+reduce(lambda x,y:str(x)+" "+str(y),sorted(paths)[0])
	else:
		print "Case #"+str(case)+": IMPOSSIBLE"
