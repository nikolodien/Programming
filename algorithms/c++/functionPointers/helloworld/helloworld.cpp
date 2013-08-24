#include<iostream>

using namespace std;

void hw(){
	cout<<"Hello World!"<<endl;
}

int main(){
	void (*hwptr)() = hw;
	hw();
	return 0;
}

