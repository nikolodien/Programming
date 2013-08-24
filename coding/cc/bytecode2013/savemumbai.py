#!/usr/bin/python

def evaluate(string,base):
	val=0;
	power=1
	#print string,base
	for i in range(len(string)-1,-1,-1):
		val=string[i]*power+val
		#print power,val
		power=power*base
	return val

numbers=['0','1','2','3','4','5','6','7','8','9']
T=input()
while(T>0):
	string=list(raw_input())
	loc=1
	locmap={}
	freqmap={}
	codemap={}
	countofchars=0
	maxnum=0
	numspresent=[]
	for char in string:
		if char in numbers:
			numspresent.append(int(char))
			codemap[char]=int(char)
			if int(char)>maxnum:
				maxnum=int(char)
			continue
		else:
			locmap[char]=loc
			loc=loc+1
			countofchars=countofchars+1
			if char not in freqmap:
				freqmap[char]=1
			else:
				freqmap[char]=freqmap[char]+1
	# if there is no character then just evaluate
	if(countofchars==0):
		print evaluate(map(lambda x:int(x),string),maxnum+1)
	# Now assign codes to the characters
	else:
		# Now sort the map according to the values
		values=sorted(sorted(freqmap,key=locmap.get),key=freqmap.get,reverse=True)
		#print values
		loop=True
		# Assign lowest code possible to the first character
		if string[0] not in numbers:
			# remove this char from values
			values.remove(string[0])
			for code in range(1,maxnum+1):
				if code not in numspresent:
					codemap[string[0]]=code
					numspresent.append(code)
					break
			if string[0] not in codemap:
				maxnum=maxnum+1
				codemap[string[0]]=maxnum
				numspresent.append(maxnum)
		#print values
		# Now just assign codes to character according to the freq
		# most frequent gets the least number
		for key in values:
			if(loop):
				for code in range(0,maxnum+1):
					if code not in numspresent:
						codemap[key]=code
						numspresent.append(code)
			if key not in codemap:	
				loop=False
				maxnum=maxnum+1
				codemap[key]=maxnum
				numspresent.append(maxnum)
		print evaluate(map(lambda x:codemap[x],string),maxnum+1)
	T=T-1
