#include<iostream>

using namespace std;

int main(){
	long T,n,hq1,hq2;
	cin>>T;
	while(T--){
		cin>>n>>hq1>>hq2;
		long graph[n];
		for(int i=0;i<n;i++){
			if((i+1)!=hq1){
				cin>>graph[i];
			}else{
				graph[i]=-1;
			}
		}
		long p=hq2,q=graph[hq2-1],r;
		while(q!=hq1){
			r=graph[q-1];
			graph[q-1]=p;
			p=q;
			q=r;
		}
		graph[q-1]=p;
		graph[hq2-1]=-1;
		for(int i=0;i<n;i++){
			if((i+1)!=hq2){
				cout<<graph[i];
				cout<<" ";
			}
		}
		cout<<"\b";
		cout<<endl;
	}
	return 0;
}
