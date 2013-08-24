#!/usr/bin/python

strings=raw_input().split(" ")
#read N and M
N=int(strings[0])
M=int(strings[1])

#chef_country map
ccmap={}
#chef_score map
csmap={}
#country_score map
crsmap={}

while N>0:
	strings=raw_input().split(" ")
	ccmap[strings[0]]=strings[1]
	csmap[strings[0]]=0
	crsmap[strings[1]]=0
	N=N-1

while M>0:
	chef=raw_input()
	csmap[chef]=csmap[chef]+1
	crsmap[ccmap[chef]]=crsmap[ccmap[chef]]+1
	M=M-1

bestChefs=sorted(csmap, key=csmap.get, reverse=True)
iterator=iter(bestChefs)
bestChef=iterator.next()
#highest chef votes
hcv=csmap.get(bestChef)

no_op=0

try:
	chef=iterator.next()
	while(chef!=None):
		if(csmap[chef]<hcv):
			break
		else:
			if(chef<bestChef):
				bestChef=chef
		chef=iterator.next()
except StopIteration:
	no_op

bestCountries=sorted(crsmap, key=crsmap.get, reverse=True)
iterator=iter(bestCountries)
bestCountry=iterator.next()
#highest country votes
hcv=crsmap.get(bestCountry)

try:
	country=iterator.next()
	while(country!=None):
		if(crsmap[country]<hcv):
			break
		else:
			if(country<bestCountry):
				bestCountry=country
		country=iterator.next()
except StopIteration:
	no_op

print bestCountry
print bestChef

