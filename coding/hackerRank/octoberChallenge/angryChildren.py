N=input()
K=input()
candies=[]
for i in range(0,N):
    candies.append(input())
unfairness=[]
for i in range(0,N-K):
	picked=sorted(candies)[i:i+K]
	unfairness.append(max(picked)-min(picked))
print min(unfairness)
