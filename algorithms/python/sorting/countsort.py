#!/usr/bin/python

def countsort(A):
	# For count sort we need two other arrays
	# B[1..n] which will store the sorted array 
	# and C[0..k] which will store the counts
	# We need to determine the size of C i.e; the
	# value of k
	k=0;
	for key in A:
		if(key>k):
			k=key
	# Now we have the largest no. of the array in k
	C=[0]*(k+1)
	B=[0]*len(A)

	# Now we proceed with the logic of count sort
	for key in A:
		C[key]=C[key]+1
	for i in xrange(1,k+1,1):
		C[i]=C[i]+C[i-1]
	for key in A:
		B[C[key]-1]=key
		C[key]=C[key]-1
	return B

def main():
	A=[int(a) for a in raw_input().split(" ")]
	B=countsort(A)
	print B

if __name__=="__main__":
	main()
