#include<iostream>
#include<map>

using namespace std;

typedef signed long long ll;

int main(){
	ll T,c,d;
	cin>>T;
	while(T-->0){
		cin>>c>>d;
		cout<<c*d-c-d<<endl;
	}
}
