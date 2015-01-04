#include<iostream>
#include<list>

using namespace std;

typedef union data data;

union data{
	int number;
	char ch;
};

int main(){
	list<int> newlist;
	newlist.push_back(1);
	cout<<newlist.front()<<endl;
	int num;
	void *data = &num;
	cout<<*(int *)data<<endl;
}
