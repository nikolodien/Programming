#include<iostream>

using namespace std;

typedef unsigned long long ul;

int main(){
	ul T;
	cin>>T;
	while(T-->0){
		ul N,K;
		cin>>N>>K;
		if(N==0 || K==0){
			cout<<"0 0"<<endl;
			continue;
		}
		cout<<N/K<<" ";
		cout<<N%K;
		cout<<endl;
	}
	cout<<endl;
}
