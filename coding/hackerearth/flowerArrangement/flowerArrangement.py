print 'Hello World!'
T=input()
while(T>0):
	arg=list(raw_input())
	error=False
	pr,pry,pryy=False,False,False
	for i in range(0,len(arg)):
		if(arg[i]=='R'):
			pr,pry,pryy=True,False,False
		elif(arg[i]=='Y'):
			if(pr):
				pr=False
				pry=True
			elif(pry):
					pry=False
					pryy=True
			else:
				error=True
				break;
		else:
			error=True
			break;
	if(error):
		print "NO"
	else:
		print "YES"	
	T=T-1
