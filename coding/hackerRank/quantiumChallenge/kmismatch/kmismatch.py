#!/usr/bin/python

def ismismatch(str1,str2,size):
	mismatch=0
	for i in range(0,size):
		if(not str1[i]==str2[i]):
			mismatch=mismatch+1
		if(mismatch>K):
			return False
	return True

K=input()
S=list(raw_input().rstrip())
length=len(S)
N=length-1

C=0
while(N>0):
	if(K<N):
		strings=[S[i:i+N] for i in range(0,len(S)-N+1)]
		for i in range(0,len(strings)):
			for j in range(i+1,len(strings)):
				if(ismismatch(strings[i],strings[j],N)):
					C=C+1
	else:	
		no=length-N+1
		if(no>1):
			C=C+(no*(no-1))/2
	N=N-1

print C
