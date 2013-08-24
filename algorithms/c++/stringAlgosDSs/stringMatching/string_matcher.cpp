#include<iostream>
#include<string>
using namespace std;
int main(){
	string p,t;
	cout<<"Enter pattern\n";
	cin>>p;
	cout<<"Enter string\n";
	cin>>t;
	// First find out the prefix array
	int pi[p.length()];
	pi[0]=-1;
	int i=0,k=-1;
	for(i=1;i<p.length();i++){
		if(k>-1 && p[k+1]!=p[i])
			k=pi[k];			
		if(p[k+1]==p[i])
			k=k+1;
		pi[i]=k;
	}
	cout<<"The prefix array is as always:";
	for(i=0;i<p.length();i++)
		cout<<pi[i]<<" ";
	cout<<endl;
	int q=-1;
	// Now start the matching process
	for(i=0;i<t.length();i++){
		if(q>-1 && p[q+1]!=t[i])
			q=pi[q];
		if(p[q+1]==t[i])
			q=q+1;
		if(q==p.length()-1){
			cout<<"The string matches at "<<i-p.length()+1<<endl;
			q=pi[p.length()-1];	
		}
	}
	return 0;
}
