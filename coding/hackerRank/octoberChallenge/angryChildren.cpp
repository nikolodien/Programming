#include<iostream>
#include<algorithm>
#include<vector>
#include<limits>

typedef unsigned long long ull;
using namespace std;

int main(){
	ull N,K;
	cin>>N>>K;
	ull candies[N];
	for(ull i=0;i<N;i++){
		cin>>candies[i];
	}
	vector<ull> candiesVector(candies,candies+N);
	sort(candiesVector.begin(),candiesVector.begin()+N);
	ull unfairness=1000000000L;
	for(ull i=0;i<N-K;i++){
		ull min=1000000000L,max=0;
		for(ull j=i;j<i+K;j++){
			if(min>candiesVector[j])min=candiesVector[j];
			if(max<candiesVector[j])max=candiesVector[j];
		}
		if((max-min)<unfairness)unfairness=max-min;
	}
	cout<<unfairness<<endl;
}
