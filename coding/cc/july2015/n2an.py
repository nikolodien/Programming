#!/usr/bin/python

found=False
max=pow(10,10)

def findFirst(num,maxZeros,mult):
    global found
    if found:
        return max
    if num % (pow(10,maxZeros)) == 0:
        found = True
        return num
    else:
        return min(findFirst(num*int(mult),maxZeros,mult+"4"),
        findFirst(num*int(mult),maxZeros,mult+"7"))

T=input()
numbers=map(int,raw_input().split(" "))

for num in numbers:
    found=False
    # First find the maximum number of trailing zeros
    temp,i,j=num,0,0
    while temp>=5 and temp%5==0:
        temp,i=temp//5,i+1
    while temp>=2 and temp%2==0:
        temp,j=temp//2,j+1
    maxZeros=min(i,j)
    if maxZeros == 0:
        print num
    else:
        # Now find the minimum number with maxZeros
        print min(findFirst(num,maxZeros,"4"),
        findFirst(num,maxZeros,"7"))
