#!/usr/bin/python

T=int(raw_input())
i=1
while i<=T:
	s=raw_input()
	stack=[]
	previous=''
	errors=0
	frowns=0
	smileys=0
	for ch in s:
		if(ch=='('):
			if(not previous==':'):
				#push on stack
				stack.append(ch)
			else:
				#frown detected
				frowns=frowns+1
		else:
			if (ch==')'):
				if(not previous==':'):
					#pop from stack
					if(len(stack)==0):
						#We cannot pop now
							errors=errors+1
					else:
						stack.pop()
				else:
					#smiley detected
					smileys=smileys+1
		previous=ch
	if( (len(stack)==0 and errors==0) or (len(stack)<smileys) or (frowns==errors)):
		print "Case #"+str(i)+": YES"
	else:
		print "Case #"+str(i)+": NO"
	i=i+1
			
