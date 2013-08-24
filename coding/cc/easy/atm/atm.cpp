#include<iostream>

using namespace std;

int main(){
	float x,y;
	cin>>x>>y;
	if(!((int)x%5) && y>=(x+(float)0.5))
		cout<<y-x-0.5<<endl;
	else
		cout<<y<<endl;
	return 0;
}
