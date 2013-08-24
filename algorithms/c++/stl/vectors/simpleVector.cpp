#include<iostream>
#include<vector>

using namespace std;

int main(){
	
	vector<int> array = vector<int>(4,0);
	vector<int>::const_iterator ci;

	for(ci=array.begin();ci!=array.end();ci++)
		cout<<*ci<<endl;
	
	for(int i=0;i<4;i++)
		array[i]=i+1;
	
	for(ci=array.begin();ci!=array.end();ci++)
		cout<<*ci<<endl;
}
