#include<iostream>
#include<stdlib.h>
#include<sys/types.h>
#include<unistd.h>
#include<string>

using namespace std;

int global;

int main(){
	int stack=0;
	int id=vfork();
	string name;
	if(id==0){
		// Child process
		stack++;
		global++;
		name="child";
	}else if(id<0){
		name="undefined";
	}else{
		wait();
		stack++;
		global++;
		name="parent";
	}
	cout<<global<<endl;
	cout<<stack<<endl;
	cout<<name<<endl;
	return 0;
}
